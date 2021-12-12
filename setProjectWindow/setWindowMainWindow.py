import importlib
from ui_mainwindow import Ui_setProjectWindow
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
import sys
import nuke
import nukescripts

class mainWindowSetProject(QWidget, Ui_setProjectWindow):
    def __init__(self):
        super(mainWindowSetProject, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Set Project From Read Node")
        
        #CENTRAL VARIABLES
        snds = nuke.selectedNodes()
        sn = nuke.selectedNode()
        nr = nuke.root()

        #MANUAL SET PROJECT AREA
        get_node_name = sn["name"].value()
        get_file_name = sn["file"].value().split("/")[-1]
        file_and_node_name = get_node_name + " - " + get_file_name
        for ba_operations in snds:
            self.beforeComboBox.addItems(ba_operations.knob("before").values())
            self.afterComboBox.addItems(ba_operations.knob("before").values())
        
        self.plateNameInput_2.setText(file_and_node_name)
        self.plateNameInput.setText(file_and_node_name)
        for colorspaces in snds:
            self.colorspaceComboBox_2.addItems(colorspaces.knob("colorspace").values())


        #AUTO SET PROJECT AREA
        self.colorspaceComboBox.addItems(colorspaces.knob("colorspace").values())

        if "input/frame_rate" in sn.metadata():
            self.fpsInput.setText((str(sn.metadata()["input/frame_rate"])[0:6]))
        else:
            self.fpsInput.setText("Still Frame")
        
        read_node_w_format =  (sn["format"].value().width()) 
        read_node_h_format =  (sn["format"].value().height()) 
        get_read_format = str(read_node_w_format) + " " +"x"+ " " + str(read_node_h_format) + " " + "Pixels"

        first_frame_plate = sn["first"].value()
        last_frame_plate = sn["last"].value()
        frame_count_plate = first_frame_plate - last_frame_plate 
        read_first_last = str(first_frame_plate) + " - " + str(last_frame_plate) + " / "+"(" + str(frame_count_plate).replace("-", "")+")" + " " + "Frame"
        before_after_proc = sn["before"].value() + " - " + sn["after"].value()
               
        self.first_frame_label.setText(str(read_first_last))
        self.formatInput.setText(get_read_format)
        self.startAtLabelA.setText("Start / End:")
        self.startAtInputA.setText(before_after_proc)

        def setAutoSettings():
            nr["first_frame"].setValue(first_frame_plate)
            nr["last_frame"].setValue(last_frame_plate)

            if "input/frame_rate" in sn.metadata():
                nr["fps"].setValue(sn.metadata()["input/frame_rate"])
            else:
                pass
            sn["colorspace"].setValue(self.colorspaceComboBox.currentText())
            #create new format
            create_size_option = str(read_node_w_format) + " " + str(read_node_h_format) + " " + str(get_file_name)
            nr["format"].setValue(nuke.addFormat(create_size_option))

        def setManualSettings():#Manual Signals
            #frame range settings
            if self.inFrameBoxM.text() == "":
                print("Last frame settings is empty.")
            elif self.outFrameBoxM.text() =="":
                print("First frame settings is empty.")
            else:
                nr["first_frame"].setValue(int(self.inFrameBoxM.text()))
                nr["last_frame"].setValue(int(self.outFrameBoxM.text()))
                print ("First frame = ",self.inFrameBoxM.text())
                print ("Last frme = ", self.outFrameBoxM.text())
            #Before -  after settings
            try:
                sn["before"].setValue(self.beforeComboBox.currentText())
                print("before proccess: ", sn["before"].value() )
                print("after process: ", sn["after"].value() )
                sn["after"].setValue(self.afterComboBox.currentText())
            except:
                print ("Before and after has no changed.")
            
            #FPS Settings
            try:
                nr["fps"].setValue(float(self.fps_comboBox.currentText()))
                print("FPS: ", nr["fps"].value())
            except:
                print("FPS: False input.")

            old_frame_mode = sn["frame_mode"].value()
            #Frame start settings
            try:
                sn["frame_mode"].setValue(str(self.start_at_comboBox.currentText()))
                print ("Frame start is:", old_frame_mode," > ", self.start_at_comboBox.currentText())
            except:
                print ("Start frame is not changed")

            if self.startFrameInput.text() != "":
                sn["frame"].setValue(str(self.startFrameInput.text()))
            else:
                print("Start frame expression is empty.")

            #Set Colorspace settings
            try:
                old_color_space = sn["colorspace"].value()
                sn["colorspace"].setValue(str(self.colorspaceComboBox_2.currentText()))
                print ("Colorspace changed:",old_color_space,">", sn["colorspace"].value())
            except:
                print ("Colorspace is not changed!")

            #Create new format manually!
            try:
                old_size_format_w = nr.format().width()
                old_size_format_h = nr.format().height()
                create_size_option_m = str(self.inFormatM.text()) + " " + str(self.outFormatM.text()) + " " + str(get_file_name)
                nr["format"].setValue(nuke.addFormat(create_size_option_m))
                new_size_format_w = nr.format().width()
                new_size_format_h = nr.format().height()
                print ("Old Size format:",old_size_format_w, old_size_format_h)
                print ("New size format:",new_size_format_w, new_size_format_h )

            except:
                print("There is a problem about format size.")


        def setButtonActivePanel():
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setWindowTitle("Set project: Last check")
            msgBox.setText('You are changed some settings. Are you sure?')
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

            retVal = msgBox.exec_()
            if retVal == QMessageBox.Ok:
                if self.set_project_main_tab.currentIndex() == 1:
                    setManualSettings()
                    print(" ")
                    print("Manual settings Selected")
                elif self.set_project_main_tab.currentIndex() == 0:
                    setAutoSettings()
                    print(" ")
                    print("Auto Settings Selected")
                else:
                    print(" ")
                    print("Nothing selected!")
                print("OK")
                self.close()

            else:
                print ("Nothing be changed from Set Project Window, Canceled.")
        self.pushButton.clicked.connect(setButtonActivePanel)

def standalone(): #If start with standalone version
    app.QApplication(sys.argv)
    panel = mainWindowSetProject()
    panel.show()
    app.exec_()

def start(): #If start with Nuke
    start.panel = mainWindowSetProject()
    start.panel.show()

