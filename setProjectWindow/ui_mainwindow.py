# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setProjectMainWindowOooCpU.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_setProjectWindow(object):
    def setupUi(self, setProjectWindow):
        if not setProjectWindow.objectName():
            setProjectWindow.setObjectName(u"setProjectWindow")
        setProjectWindow.resize(369, 371)
        setProjectWindow.setMinimumSize(QSize(369, 371))
        self.verticalLayout_2 = QVBoxLayout(setProjectWindow)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.set_project_main_tab = QTabWidget(setProjectWindow)
        self.set_project_main_tab.setObjectName(u"set_project_main_tab")
        self.createManualProjectTab = QWidget()
        self.createManualProjectTab.setObjectName(u"createManualProjectTab")
        self.verticalLayout_7 = QVBoxLayout(self.createManualProjectTab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.groupBox = QGroupBox(self.createManualProjectTab)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.plateNameLabel = QLabel(self.groupBox)
        self.plateNameLabel.setObjectName(u"plateNameLabel")

        self.horizontalLayout_2.addWidget(self.plateNameLabel)

        self.plateNameInput = QLabel(self.groupBox)
        self.plateNameInput.setObjectName(u"plateNameInput")

        self.horizontalLayout_2.addWidget(self.plateNameInput)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.line_3 = QFrame(self.groupBox)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frameRangeLabel = QLabel(self.groupBox)
        self.frameRangeLabel.setObjectName(u"frameRangeLabel")
        self.frameRangeLabel.setMinimumSize(QSize(90, 0))
        self.frameRangeLabel.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_3.addWidget(self.frameRangeLabel)

        self.first_frame_label = QLabel(self.groupBox)
        self.first_frame_label.setObjectName(u"first_frame_label")

        self.horizontalLayout_3.addWidget(self.first_frame_label)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.fpsInfoLabel = QLabel(self.groupBox)
        self.fpsInfoLabel.setObjectName(u"fpsInfoLabel")
        self.fpsInfoLabel.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_4.addWidget(self.fpsInfoLabel)

        self.fpsInput = QLabel(self.groupBox)
        self.fpsInput.setObjectName(u"fpsInput")

        self.horizontalLayout_4.addWidget(self.fpsInput)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.formatLabel = QLabel(self.groupBox)
        self.formatLabel.setObjectName(u"formatLabel")
        self.formatLabel.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_5.addWidget(self.formatLabel)

        self.formatInput = QLabel(self.groupBox)
        self.formatInput.setObjectName(u"formatInput")

        self.horizontalLayout_5.addWidget(self.formatInput)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.startAtLabelA = QLabel(self.groupBox)
        self.startAtLabelA.setObjectName(u"startAtLabelA")
        self.startAtLabelA.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_18.addWidget(self.startAtLabelA)

        self.startAtInputA = QLabel(self.groupBox)
        self.startAtInputA.setObjectName(u"startAtInputA")

        self.horizontalLayout_18.addWidget(self.startAtInputA)


        self.verticalLayout_4.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.colorSpaceLabel = QLabel(self.groupBox)
        self.colorSpaceLabel.setObjectName(u"colorSpaceLabel")
        self.colorSpaceLabel.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_8.addWidget(self.colorSpaceLabel)

        self.colorspaceComboBox = QComboBox(self.groupBox)
        self.colorspaceComboBox.setObjectName(u"colorspaceComboBox")
        self.colorspaceComboBox.setEnabled(True)

        self.horizontalLayout_8.addWidget(self.colorspaceComboBox)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)


        self.verticalLayout_8.addLayout(self.verticalLayout_4)


        self.verticalLayout_7.addWidget(self.groupBox)

        self.label_2 = QLabel(self.createManualProjectTab)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_7.addWidget(self.label_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.set_project_main_tab.addTab(self.createManualProjectTab, "")
        self.createAutoProjectTab = QWidget()
        self.createAutoProjectTab.setObjectName(u"createAutoProjectTab")
        self.verticalLayout_3 = QVBoxLayout(self.createAutoProjectTab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_2 = QGroupBox(self.createAutoProjectTab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.plateNameLabel_2 = QLabel(self.groupBox_2)
        self.plateNameLabel_2.setObjectName(u"plateNameLabel_2")

        self.horizontalLayout_9.addWidget(self.plateNameLabel_2)

        self.plateNameInput_2 = QLabel(self.groupBox_2)
        self.plateNameInput_2.setObjectName(u"plateNameInput_2")

        self.horizontalLayout_9.addWidget(self.plateNameInput_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.line = QFrame(self.groupBox_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frameRangeLabel_2 = QLabel(self.groupBox_2)
        self.frameRangeLabel_2.setObjectName(u"frameRangeLabel_2")
        self.frameRangeLabel_2.setMinimumSize(QSize(90, 0))
        self.frameRangeLabel_2.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_10.addWidget(self.frameRangeLabel_2)

        self.inFrameBoxM = QLineEdit(self.groupBox_2)
        self.inFrameBoxM.setObjectName(u"inFrameBoxM")
        self.inFrameBoxM.setEnabled(True)

        self.horizontalLayout_10.addWidget(self.inFrameBoxM)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_10.addWidget(self.label_5)

        self.outFrameBoxM = QLineEdit(self.groupBox_2)
        self.outFrameBoxM.setObjectName(u"outFrameBoxM")
        self.outFrameBoxM.setEnabled(True)

        self.horizontalLayout_10.addWidget(self.outFrameBoxM)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.frameLastFirstOpLabel = QLabel(self.groupBox_2)
        self.frameLastFirstOpLabel.setObjectName(u"frameLastFirstOpLabel")
        self.frameLastFirstOpLabel.setMinimumSize(QSize(90, 0))
        self.frameLastFirstOpLabel.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_13.addWidget(self.frameLastFirstOpLabel)

        self.beforeComboBox = QComboBox(self.groupBox_2)
        self.beforeComboBox.setObjectName(u"beforeComboBox")

        self.horizontalLayout_13.addWidget(self.beforeComboBox)

        self.afterComboBox = QComboBox(self.groupBox_2)
        self.afterComboBox.setObjectName(u"afterComboBox")

        self.horizontalLayout_13.addWidget(self.afterComboBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.fpsInfoLabel_2 = QLabel(self.groupBox_2)
        self.fpsInfoLabel_2.setObjectName(u"fpsInfoLabel_2")
        self.fpsInfoLabel_2.setMinimumSize(QSize(90, 0))
        self.fpsInfoLabel_2.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_11.addWidget(self.fpsInfoLabel_2)

        self.fps_comboBox = QComboBox(self.groupBox_2)
        self.fps_comboBox.addItem("")
        self.fps_comboBox.addItem("")
        self.fps_comboBox.addItem("")
        self.fps_comboBox.addItem("")
        self.fps_comboBox.addItem("")
        self.fps_comboBox.addItem("")
        self.fps_comboBox.addItem("")
        self.fps_comboBox.addItem("")
        self.fps_comboBox.addItem("")
        self.fps_comboBox.addItem("")
        self.fps_comboBox.addItem("")
        self.fps_comboBox.addItem("")
        self.fps_comboBox.addItem("")
        self.fps_comboBox.setObjectName(u"fps_comboBox")

        self.horizontalLayout_11.addWidget(self.fps_comboBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.startFrameLabel = QLabel(self.groupBox_2)
        self.startFrameLabel.setObjectName(u"startFrameLabel")
        self.startFrameLabel.setMinimumSize(QSize(90, 0))
        self.startFrameLabel.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_16.addWidget(self.startFrameLabel)

        self.start_at_comboBox = QComboBox(self.groupBox_2)
        self.start_at_comboBox.addItem("")
        self.start_at_comboBox.addItem("")
        self.start_at_comboBox.addItem("")
        self.start_at_comboBox.setObjectName(u"start_at_comboBox")

        self.horizontalLayout_16.addWidget(self.start_at_comboBox)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_16.addWidget(self.label_4)

        self.startFrameInput = QLineEdit(self.groupBox_2)
        self.startFrameInput.setObjectName(u"startFrameInput")

        self.horizontalLayout_16.addWidget(self.startFrameInput)


        self.verticalLayout_5.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.frameRangeLabel_3 = QLabel(self.groupBox_2)
        self.frameRangeLabel_3.setObjectName(u"frameRangeLabel_3")
        self.frameRangeLabel_3.setMinimumSize(QSize(90, 0))
        self.frameRangeLabel_3.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_12.addWidget(self.frameRangeLabel_3)

        self.inFormatM = QLineEdit(self.groupBox_2)
        self.inFormatM.setObjectName(u"inFormatM")
        self.inFormatM.setEnabled(True)

        self.horizontalLayout_12.addWidget(self.inFormatM)

        self.outFormatM = QLineEdit(self.groupBox_2)
        self.outFormatM.setObjectName(u"outFormatM")
        self.outFormatM.setEnabled(True)

        self.horizontalLayout_12.addWidget(self.outFormatM)


        self.verticalLayout_5.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.colorSpaceLabel_2 = QLabel(self.groupBox_2)
        self.colorSpaceLabel_2.setObjectName(u"colorSpaceLabel_2")
        self.colorSpaceLabel_2.setMaximumSize(QSize(90, 16777215))

        self.horizontalLayout_15.addWidget(self.colorSpaceLabel_2)

        self.colorspaceComboBox_2 = QComboBox(self.groupBox_2)
        self.colorspaceComboBox_2.setObjectName(u"colorspaceComboBox_2")
        self.colorspaceComboBox_2.setCurrentText(u"")

        self.horizontalLayout_15.addWidget(self.colorspaceComboBox_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_15)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.label_3 = QLabel(self.createAutoProjectTab)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.set_project_main_tab.addTab(self.createAutoProjectTab, "")
        self.infoProjectTab = QWidget()
        self.infoProjectTab.setObjectName(u"infoProjectTab")
        self.verticalLayout_10 = QVBoxLayout(self.infoProjectTab)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.groupBox_3 = QGroupBox(self.infoProjectTab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_12 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")

        self.verticalLayout_11.addWidget(self.label)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_3)


        self.verticalLayout_12.addLayout(self.verticalLayout_11)


        self.verticalLayout_9.addWidget(self.groupBox_3)


        self.verticalLayout_10.addLayout(self.verticalLayout_9)

        self.set_project_main_tab.addTab(self.infoProjectTab, "")

        self.verticalLayout.addWidget(self.set_project_main_tab)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(setProjectWindow)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.cancelProjectButton = QPushButton(setProjectWindow)
        self.cancelProjectButton.setObjectName(u"cancelProjectButton")

        self.horizontalLayout.addWidget(self.cancelProjectButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(setProjectWindow)
        self.cancelProjectButton.clicked.connect(setProjectWindow.close)

        self.set_project_main_tab.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(setProjectWindow)
    # setupUi

    def retranslateUi(self, setProjectWindow):
        setProjectWindow.setWindowTitle(QCoreApplication.translate("setProjectWindow", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("setProjectWindow", u"Selected Plate/Shot Details", None))
        self.plateNameLabel.setText(QCoreApplication.translate("setProjectWindow", u"Plate / Shot Name:", None))
        self.plateNameInput.setText(QCoreApplication.translate("setProjectWindow", u"Plate Name", None))
        self.frameRangeLabel.setText(QCoreApplication.translate("setProjectWindow", u"Frame Range:", None))
        self.first_frame_label.setText(QCoreApplication.translate("setProjectWindow", u"Frames-in out", None))
        self.fpsInfoLabel.setText(QCoreApplication.translate("setProjectWindow", u"FPS:", None))
        self.fpsInput.setText(QCoreApplication.translate("setProjectWindow", u"Fps value", None))
        self.formatLabel.setText(QCoreApplication.translate("setProjectWindow", u"Format:", None))
        self.formatInput.setText(QCoreApplication.translate("setProjectWindow", u"format info", None))
        self.startAtLabelA.setText(QCoreApplication.translate("setProjectWindow", u"Start at: ", None))
        self.startAtInputA.setText(QCoreApplication.translate("setProjectWindow", u"Start at input", None))
        self.colorSpaceLabel.setText(QCoreApplication.translate("setProjectWindow", u"Colorspace:", None))
        self.label_2.setText(QCoreApplication.translate("setProjectWindow", u"<html><head/><body><p>In this tab you can set the all settings from selected read node.</p><p>Just one selection change to Colorspace if you want.</p></body></html>", None))
        self.set_project_main_tab.setTabText(self.set_project_main_tab.indexOf(self.createManualProjectTab), QCoreApplication.translate("setProjectWindow", u"Auto Set Project", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("setProjectWindow", u"Input Specific Options", None))
        self.plateNameLabel_2.setText(QCoreApplication.translate("setProjectWindow", u"Plate Name:", None))
        self.plateNameInput_2.setText(QCoreApplication.translate("setProjectWindow", u"Plate Name", None))
        self.frameRangeLabel_2.setText(QCoreApplication.translate("setProjectWindow", u"Frame Range:", None))
        self.label_5.setText(QCoreApplication.translate("setProjectWindow", u"to", None))
        self.frameLastFirstOpLabel.setText(QCoreApplication.translate("setProjectWindow", u"Before / After:", None))
        self.fpsInfoLabel_2.setText(QCoreApplication.translate("setProjectWindow", u"FPS:", None))
        self.fps_comboBox.setItemText(0, QCoreApplication.translate("setProjectWindow", u"Select", None))
        self.fps_comboBox.setItemText(1, QCoreApplication.translate("setProjectWindow", u"8", None))
        self.fps_comboBox.setItemText(2, QCoreApplication.translate("setProjectWindow", u"10", None))
        self.fps_comboBox.setItemText(3, QCoreApplication.translate("setProjectWindow", u"12", None))
        self.fps_comboBox.setItemText(4, QCoreApplication.translate("setProjectWindow", u"12.50", None))
        self.fps_comboBox.setItemText(5, QCoreApplication.translate("setProjectWindow", u"15", None))
        self.fps_comboBox.setItemText(6, QCoreApplication.translate("setProjectWindow", u"23.976", None))
        self.fps_comboBox.setItemText(7, QCoreApplication.translate("setProjectWindow", u"24", None))
        self.fps_comboBox.setItemText(8, QCoreApplication.translate("setProjectWindow", u"25", None))
        self.fps_comboBox.setItemText(9, QCoreApplication.translate("setProjectWindow", u"29.97", None))
        self.fps_comboBox.setItemText(10, QCoreApplication.translate("setProjectWindow", u"30", None))
        self.fps_comboBox.setItemText(11, QCoreApplication.translate("setProjectWindow", u"48", None))
        self.fps_comboBox.setItemText(12, QCoreApplication.translate("setProjectWindow", u"50", None))

        self.startFrameLabel.setText(QCoreApplication.translate("setProjectWindow", u"Frame", None))
        self.start_at_comboBox.setItemText(0, QCoreApplication.translate("setProjectWindow", u"start at", None))
        self.start_at_comboBox.setItemText(1, QCoreApplication.translate("setProjectWindow", u"expression", None))
        self.start_at_comboBox.setItemText(2, QCoreApplication.translate("setProjectWindow", u"offset", None))

        self.label_4.setText(QCoreApplication.translate("setProjectWindow", u"is", None))
        self.frameRangeLabel_3.setText(QCoreApplication.translate("setProjectWindow", u"Format:", None))
        self.colorSpaceLabel_2.setText(QCoreApplication.translate("setProjectWindow", u"Colorspace:", None))
        self.label_3.setText(QCoreApplication.translate("setProjectWindow", u"Set all settings manually. ", None))
        self.set_project_main_tab.setTabText(self.set_project_main_tab.indexOf(self.createAutoProjectTab), QCoreApplication.translate("setProjectWindow", u"Manual Set Project", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("setProjectWindow", u"Content", None))
        self.label.setText(QCoreApplication.translate("setProjectWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">For more information:</span></p><p>www.fatihunal.net/setproject (How to use tihs script)</p><p>fatihunal1989@gmail.com</p><p>www.fatihunal.net</p><p><br/></p></body></html>", None))
        self.set_project_main_tab.setTabText(self.set_project_main_tab.indexOf(self.infoProjectTab), QCoreApplication.translate("setProjectWindow", u"About", None))
        self.pushButton.setText(QCoreApplication.translate("setProjectWindow", u"Set Project", None))
        self.cancelProjectButton.setText(QCoreApplication.translate("setProjectWindow", u"Close", None))
    # retranslateUi

