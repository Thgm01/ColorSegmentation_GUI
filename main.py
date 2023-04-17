import sys
from ui.interface import Ui_Form
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

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


    def show(self):
        self.main_win.show()
                


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())