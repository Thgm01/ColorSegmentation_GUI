# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("HSV GUI")
        Form.resize(786, 690)
        self.verticalSlider_HU = QtWidgets.QSlider(Form)
        self.verticalSlider_HU.setGeometry(QtCore.QRect(80, 110, 16, 160))
        self.verticalSlider_HU.setMinimum(1)
        self.verticalSlider_HU.setMaximum(255)
        self.verticalSlider_HU.setProperty("value", 255)
        self.verticalSlider_HU.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_HU.setObjectName("verticalSlider_HU")
        self.verticalSlider_SU = QtWidgets.QSlider(Form)
        self.verticalSlider_SU.setGeometry(QtCore.QRect(140, 110, 16, 160))
        font = QtGui.QFont()
        font.setItalic(False)
        font.setStrikeOut(False)
        self.verticalSlider_SU.setFont(font)
        self.verticalSlider_SU.setMinimum(1)
        self.verticalSlider_SU.setMaximum(255)
        self.verticalSlider_SU.setProperty("value", 255)
        self.verticalSlider_SU.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_SU.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.verticalSlider_SU.setObjectName("verticalSlider_SU")
        self.verticalSlider_VU = QtWidgets.QSlider(Form)
        self.verticalSlider_VU.setGeometry(QtCore.QRect(196, 110, 20, 160))
        self.verticalSlider_VU.setMinimum(1)
        self.verticalSlider_VU.setMaximum(255)
        self.verticalSlider_VU.setProperty("value", 255)
        self.verticalSlider_VU.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_VU.setObjectName("verticalSlider_VU")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(110, 30, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Arimo")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 280, 67, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(140, 280, 67, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(200, 280, 67, 17))
        self.label_5.setObjectName("label_5")
        self.number_HU = QtWidgets.QLabel(Form)
        self.number_HU.setGeometry(QtCore.QRect(80, 90, 51, 17))
        self.number_HU.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.number_HU.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.number_HU.setObjectName("number_HU")
        self.number_SU = QtWidgets.QLabel(Form)
        self.number_SU.setGeometry(QtCore.QRect(140, 90, 51, 17))
        self.number_SU.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.number_SU.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.number_SU.setObjectName("number_SU")
        self.number_VU = QtWidgets.QLabel(Form)
        self.number_VU.setGeometry(QtCore.QRect(200, 90, 51, 17))
        self.number_VU.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.number_VU.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.number_VU.setObjectName("number_VU")
        self.verticalSlider_HL = QtWidgets.QSlider(Form)
        self.verticalSlider_HL.setGeometry(QtCore.QRect(80, 420, 16, 160))
        self.verticalSlider_HL.setMaximum(255)
        self.verticalSlider_HL.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_HL.setObjectName("verticalSlider_HL")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(110, 340, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Arimo")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(200, 590, 67, 17))
        self.label_6.setObjectName("label_6")
        self.number_SL = QtWidgets.QLabel(Form)
        self.number_SL.setGeometry(QtCore.QRect(140, 400, 51, 17))
        self.number_SL.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.number_SL.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.number_SL.setObjectName("number_SL")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(80, 590, 67, 17))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(140, 590, 67, 17))
        self.label_8.setObjectName("label_8")
        self.number_VL = QtWidgets.QLabel(Form)
        self.number_VL.setGeometry(QtCore.QRect(200, 400, 51, 17))
        self.number_VL.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.number_VL.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.number_VL.setObjectName("number_VL")
        self.verticalSlider_SL = QtWidgets.QSlider(Form)
        self.verticalSlider_SL.setGeometry(QtCore.QRect(140, 420, 16, 160))
        font = QtGui.QFont()
        font.setItalic(False)
        font.setStrikeOut(False)
        self.verticalSlider_SL.setFont(font)
        self.verticalSlider_SL.setMaximum(255)
        self.verticalSlider_SL.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_SL.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.verticalSlider_SL.setObjectName("verticalSlider_SL")
        self.verticalSlider_VL = QtWidgets.QSlider(Form)
        self.verticalSlider_VL.setGeometry(QtCore.QRect(196, 420, 20, 160))
        self.verticalSlider_VL.setMaximum(255)
        self.verticalSlider_VL.setProperty("value", 0)
        self.verticalSlider_VL.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_VL.setObjectName("verticalSlider_VL")
        self.number_HL = QtWidgets.QLabel(Form)
        self.number_HL.setGeometry(QtCore.QRect(80, 400, 51, 17))
        self.number_HL.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.number_HL.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.number_HL.setObjectName("number_HL")
        self.frames = QtWidgets.QLabel(Form)
        self.frames.setGeometry(QtCore.QRect(300, 30, 400, 300))
        self.frames.setText("")
        self.frames.setPixmap(QtGui.QPixmap("../../Downloads/sem_camera.png"))
        self.frames.setScaledContents(True)
        self.frames.setWordWrap(False)
        self.frames.setObjectName("frames")
        self.mask = QtWidgets.QLabel(Form)
        self.mask.setGeometry(QtCore.QRect(300, 350, 400, 300))
        self.mask.setText("")
        self.mask.setPixmap(QtGui.QPixmap("../../Downloads/sem_camera.png"))
        self.mask.setScaledContents(True)
        self.mask.setObjectName("mask")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Upper"))
        self.label_3.setText(_translate("Form", "H"))
        self.label_4.setText(_translate("Form", "S"))
        self.label_5.setText(_translate("Form", "V"))
        self.number_HU.setText(_translate("Form", "255"))
        self.number_SU.setText(_translate("Form", "255"))
        self.number_VU.setText(_translate("Form", "255"))
        self.label_2.setText(_translate("Form", "Lower"))
        self.label_6.setText(_translate("Form", "V"))
        self.number_SL.setText(_translate("Form", "0"))
        self.label_7.setText(_translate("Form", "H"))
        self.label_8.setText(_translate("Form", "S"))
        self.number_VL.setText(_translate("Form", "0"))
        self.number_HL.setText(_translate("Form", "0"))
