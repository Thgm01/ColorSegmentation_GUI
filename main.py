import sys
from ui.interface import Ui_Form
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2
import numpy as np

color_hsv_lower = np.array([0,0,0])
color_hsv_upper = np.array([255,255,255])


class MainWindow:
    def __init__(self):
        self.hue_lower_value=0
        self.sturation_lower_value=0
        self.value_lower_value=0

        self.hue_upper_value=255
        self.sturation_upper_value=255
        self.value_upper_value=255

        self.main_win = QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.main_win)
        self.ui.verticalSlider_HL.valueChanged.connect(self.hue_change)
        self.ui.verticalSlider_HU.valueChanged.connect(self.hue_change)

        self.ui.verticalSlider_SL.valueChanged.connect(self.saturation_change)
        self.ui.verticalSlider_SU.valueChanged.connect(self.saturation_change)

        self.ui.verticalSlider_VL.valueChanged.connect(self.value_change)
        self.ui.verticalSlider_VU.valueChanged.connect(self.value_change)


        self.Worker1 = Worker1()
        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
        self.Worker1.MaskUpdate.connect(self.MaskUpdateSlot)
        

    def MaskUpdateSlot(self, Mask):
        self.ui.mask.setPixmap(QPixmap.fromImage(Mask))


    def ImageUpdateSlot(self, Image):
        self.ui.frames.setPixmap(QPixmap.fromImage(Image))

        
    
    def hue_change(self):

        self.hue_lower_value = self.ui.verticalSlider_HL.value()
        self.hue_upper_value = self.ui.verticalSlider_HU.value()

        if self.hue_lower_value >= self.hue_upper_value:
            self.hue_lower_value = self.hue_upper_value-1
            self.ui.verticalSlider_HL.setValue(self.hue_lower_value)

        if self.hue_lower_value >= self.hue_upper_value:
            self.hue_upper_value = self.hue_lower_value+1
            self.ui.verticalSlider_HU.setValue(self.hue_upper_value)

        self.ui.number_HU.setText(str(self.hue_upper_value))
        self.ui.number_HL.setText(str(self.hue_lower_value))  

        color_hsv_lower[0] = self.hue_lower_value
        color_hsv_upper[0] = self.hue_upper_value

    def saturation_change(self):
        self.saturation_lower_value = self.ui.verticalSlider_SL.value()
        self.saturation_upper_value = self.ui.verticalSlider_SU.value()

        if self.saturation_lower_value >= self.saturation_upper_value:
            self.saturation_lower_value = self.saturation_upper_value-1
            self.ui.verticalSlider_SL.setValue(self.saturation_lower_value)

        if self.saturation_lower_value >= self.saturation_upper_value:
            self.saturation_upper_value = self.saturation_lower_value+1
            self.ui.verticalSlider_SU.setValue(self.saturation_upper_value)

        self.ui.number_SU.setText(str(self.saturation_upper_value))
        self.ui.number_SL.setText(str(self.saturation_lower_value))

        color_hsv_lower[1] = self.saturation_lower_value
        color_hsv_upper[1] = self.saturation_upper_value
    
    def value_change(self):
        self.value_lower_value = self.ui.verticalSlider_VL.value()
        self.value_upper_value = self.ui.verticalSlider_VU.value()

        if self.value_lower_value >= self.value_upper_value:
            self.value_lower_value = self.value_upper_value-1
            self.ui.verticalSlider_VL.setValue(self.value_lower_value)

        if self.value_lower_value >= self.value_upper_value:
            self.value_upper_value = self.value_lower_value+1
            self.ui.verticalSlider_VU.setValue(self.value_upper_value)

        self.ui.number_VU.setText(str(self.value_upper_value))
        self.ui.number_VL.setText(str(self.value_lower_value))

        color_hsv_lower[2] = self.value_lower_value
        color_hsv_upper[2] = self.value_upper_value


    def show(self):
        self.main_win.show()

class Worker1(QThread):
    ImageUpdate = pyqtSignal(QImage)
    MaskUpdate = pyqtSignal(QImage)

    def run(self, mask=False, hsv_lower=color_hsv_lower, hsv_upper=color_hsv_upper):
        self.ThreadActive = True
        cap = cv2.VideoCapture(0)
        while self.ThreadActive:
            ret, frame = cap.read()
            if ret:

                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                mask = cv2.inRange(hsv, hsv_lower, hsv_upper)
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                FlippedImage = cv2.flip(image, 1)   
                FlippedMask = cv2.flip(mask, 1)   
                 
                ConvertToQtFormat_image = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                ConvertToQtFormat_mask = QImage(FlippedMask.data, FlippedMask.shape[1], FlippedMask.shape[0], QImage.Format_Grayscale8)
                
                pic_img = ConvertToQtFormat_image.scaled(400,300, Qt.KeepAspectRatio)
                pic_mask = ConvertToQtFormat_mask.scaled(400,300, Qt.KeepAspectRatio)

                self.ImageUpdate.emit(pic_img)
                self.MaskUpdate.emit(pic_mask)
                

    def stop(self):
        self.ThreadActive = False
        self.quit()

                


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())