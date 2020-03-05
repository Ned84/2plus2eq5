# -*- coding: utf-8 -*-
"""
OnionSwitch | Easily switch the Tor-Exit-Node Destination Country in
your Tor-Browser.
Copyright (C) 2019  Ned84 ned84@protonmail.com
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import platform

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QFileDialog
from PyQt5.Qt import QApplication

import SSS_Functions as sss

import struct


version = "0.1"

class Fonts():

    def Choose_Fonts(self, bold, size, font_type):
        font = QtGui.QFont()
        font.setFamily(font_type)
        if sss.Secondary_Functions.paramplatform == "Windows":
            if bold is True:
                font.setBold(True)
                font.setWeight(75)
            else:
                pass

            font.setPointSize(size)
        else:
            if bold is True:
                font.setBold(True)
                font.setWeight(75)
            else:
                pass

            font.setPointSize(size + 2)

        return font


class Ui_MainWindow(QtWidgets.QWidget):

    serverconnection = False
    versionnew = ""
    versioncheckdone = False
    firstrun = True

    def __init__(self, *args, **kwargs):
        try:
            super().__init__()

            sss.Secondary_Functions.paramplatform = platform.system()

            # if osf.Functions.paramplatform == "Windows":
            #     osf.Functions.pathtoparam = os.getenv(
            #         'LOCALAPPDATA') + '\\OnionSwitch\\osparam'
            #     osf.Functions.pathtolog = os.getenv(
            #         'LOCALAPPDATA') + '\\OnionSwitch\\logfiles'
            #     osf.Functions.pathtomain = os.getenv(
            #         'LOCALAPPDATA') + '\\OnionSwitch'
            #     osf.Functions.pathseparator = "\\"
            #     osf.Functions.paramlanguagefiles = "\\i18n\\"

            # if osf.Functions.paramplatform == "Linux":
            #     osf.Functions.pathtoparam = os.path.dirname(
            #         os.path.abspath(__file__)) + '/OnionSwitch/osparam'
            #     osf.Functions.pathtolog = os.path.dirname(
            #         os.path.abspath(__file__)) + '/OnionSwitch/logfiles'
            #     osf.Functions.pathtomain = os.path.dirname(
            #         os.path.abspath(__file__)) + '/OnionSwitch'
            #     osf.Functions.pathseparator = "/"
            #     osf.Functions.paramlanguagefiles = "/i18n/"

            # if path.exists(osf.Functions.pathtomain) is False:
            #     os.mkdir(osf.Functions.pathtomain)

            # if path.exists(osf.Functions.pathtoparam) is False:
            #     os.mkdir(osf.Functions.pathtoparam)

            # if path.exists(osf.Functions.pathtolog) is False:
            #     os.mkdir(osf.Functions.pathtolog)

            # if path.exists(
            #         osf.Functions.pathtoparam + osf.Functions.pathseparator +
            #         'Param.json') is False:

            #     with open(
            #         osf.Functions.pathtoparam + osf.Functions.pathseparator +
            #             'Param.json', "w+") as file:

            #         data = [{"Version": version, "Path_to_Tor": "",
            #                 "Update_available": False, "StrictNodes": 1,
            #                  "Platform": "", "StemCheck": False,
            #                  "StemCheck_Time": 10, "Language": ""}]

            #         json.dump(data, file, indent=1, sort_keys=True)

            # if path.exists(
            #     osf.Functions.pathtolog + osf.Functions.pathseparator +
            #         'oslog.txt') is False:

            #     with open(
            #         osf.Functions.pathtolog + osf.Functions.pathseparator +
            #             'oslog.txt', "w+") as file:
            #         pass

            # osf.Functions.GetSettingsFromJson(self)

        except Exception as exc:
            sss.Secondary_Functions.WriteLog(self, exc)
        # try:
        #     def UpdateCheck():
        #         link = ("https://github.com/Ned84/OnionSwitch/blob/master/" +
        #                 "VERSION.md")
        #         url = request.urlopen(link)
        #         readurl = url.read()
        #         text = readurl.decode(encoding='utf-8', errors='ignore')
        #         stringindex = text.find("OnionSwitchVersion")

        #         if stringindex != -1:
        #             Ui_MainWindow.versionnew = text[stringindex +
        #                                             20:stringindex + 23]
        #             Ui_MainWindow.versionnew = \
        #                 Ui_MainWindow.versionnew.replace('_', '.')

        #         if version < Ui_MainWindow.versionnew:
        #             Ui_MainWindow.serverconnection = True
        #             osf.Functions.paramupdateavailable = True
        #             Ui_MainWindow.versioncheckdone = True

        #         else:
        #             Ui_MainWindow.serverconnection = True
        #             osf.Functions.paramupdateavailable = False
        #             Ui_MainWindow.versioncheckdone = True

        #         osf.Functions.WriteSettingsToJson(self)

        #     urlthread = threading.Thread(target=UpdateCheck, daemon=True)
        #     urlthread.start()

        # except Exception:
        #     osf.Functions.paramupdateavailable = False
        #     Ui_MainWindow.versioncheckdone = True

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 300)
        MainWindow.setMinimumSize(QtCore.QSize(500, 300))
        MainWindow.setMaximumSize(QtCore.QSize(500, 300))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.total_shares_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.total_shares_spinBox.setGeometry(QtCore.QRect(10, 60, 42, 22))
        self.total_shares_spinBox.setObjectName("total_shares_spinBox")
        self.min_shares_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.min_shares_spinBox.setGeometry(QtCore.QRect(120, 60, 42, 22))
        self.min_shares_spinBox.setObjectName("min_shares_spinBox")
        self.total_shares_label = QtWidgets.QLabel(self.centralwidget)
        self.total_shares_label.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.total_shares_label.setObjectName("total_shares_label")
        self.min_shares_label = QtWidgets.QLabel(self.centralwidget)
        self.min_shares_label.setGeometry(QtCore.QRect(120, 30, 101, 16))
        self.min_shares_label.setObjectName("min_shares_label")
        self.load_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.load_lineEdit.setGeometry(QtCore.QRect(10, 150, 211, 22))
        self.load_lineEdit.setObjectName("lineEdit")
        self.save_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.save_lineEdit.setGeometry(QtCore.QRect(250, 150, 211, 22))
        self.save_lineEdit.setObjectName("lineEdit_2")
        self.load_Button = QtWidgets.QPushButton(self.centralwidget)
        self.load_Button.setGeometry(QtCore.QRect(130, 180, 93, 28))
        self.load_Button.setObjectName("load_Button")
        self.save_Button = QtWidgets.QPushButton(self.centralwidget)
        self.save_Button.setGeometry(QtCore.QRect(370, 180, 93, 28))
        self.save_Button.setObjectName("save_Button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 26))
        self.menubar.setObjectName("menubar")
        self.menuProgram = QtWidgets.QMenu(self.menubar)
        self.menuProgram.setObjectName("menuProgram")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionWikipedia = QtWidgets.QAction(MainWindow)
        self.actionWikipedia.setObjectName("actionWikipedia")
        self.actionUpdate = QtWidgets.QAction(MainWindow)
        self.actionUpdate.setObjectName("actionUpdate")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.menuProgram.addAction(self.actionSettings)
        self.menuHelp.addAction(self.actionWikipedia)
        self.menuHelp.addAction(self.actionUpdate)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuProgram.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        @pyqtSlot()
        def OpenLoadFilePicker():
            try:
                fileName = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\',"Encrypted File (*.asc)")
                if fileName:
                    self.load_lineEdit.setText(fileName[0])

                sss.Secondary_Functions.Read_Encrypted_File(self, fileName[0])

            except Exception as exc:
                sss.Secondary_Functions.WriteLog(self, exc)

        @pyqtSlot()
        def OpenSaveFilePicker():
            try:
                sss.SSS_Functions.main_share_creation(self)

            except Exception as exc:
                sss.Secondary_Functions.WriteLog(self, exc)

        self.load_Button.clicked.connect(OpenLoadFilePicker)
        self.save_Button.clicked.connect(OpenSaveFilePicker)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.total_shares_label.setText(_translate("MainWindow", "Total Shares"))
        self.min_shares_label.setText(_translate("MainWindow", "Minimum Shares"))
        self.load_Button.setText(_translate("MainWindow", "Load"))
        self.save_Button.setText(_translate("MainWindow", "Save"))
        self.menuProgram.setTitle(_translate("MainWindow", "Program"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionWikipedia.setText(_translate("MainWindow", "Wikipedia"))
        self.actionUpdate.setText(_translate("MainWindow", "Update"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    styles = QtWidgets.QStyleFactory.keys()
    app.setStyle('Fusion')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
