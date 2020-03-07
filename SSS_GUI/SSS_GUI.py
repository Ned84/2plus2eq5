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

import SSS_Functions as sss

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
        def OpenDialogSettings():
            self.window_settings = QtWidgets.QDialog()
            self.window_settings.setWindowFlags(
                self.windowFlags() | QtCore.Qt.CustomizeWindowHint)
            self.window_settings.setWindowFlags(
                self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
            self.window_settings.installEventFilter(self)
            self.ui = Ui_SettingsDialog()
            self.ui.setupUi(self.window_settings)
            self.window_settings.show()

        @pyqtSlot()
        def OpenLoadFilePicker():
            try:
                fileName = QFileDialog.getOpenFileName(
                    self,
                    'Open file',
                    'c:\\',
                    "Encrypted File, Text File (*.asc *.txt)")
                if fileName[0]:
                    self.load_lineEdit.setText(fileName[0])

            except Exception as exc:
                sss.Secondary_Functions.WriteLog(self, exc)

        @pyqtSlot()
        def OpenSaveFilePicker():
            try:
                self.save_lineEdit.setText("")
                sss.SSS_Functions.main_share_creation(self)
                self.save_lineEdit.setText(str(sss.SSS_Functions.secret_out))

            except Exception as exc:
                sss.Secondary_Functions.WriteLog(self, exc)

        @pyqtSlot()
        def TotalSprinBoxChanged():
            sss.SSS_Functions.total_shares = self.total_shares_spinBox.value()

        @pyqtSlot()
        def MinSprinBoxChanged():
            sss.SSS_Functions.min_shares = self.min_shares_spinBox.value()

        self.load_Button.clicked.connect(OpenLoadFilePicker)
        self.save_Button.clicked.connect(OpenSaveFilePicker)
        self.total_shares_spinBox.valueChanged.connect(TotalSprinBoxChanged)
        self.min_shares_spinBox.valueChanged.connect(MinSprinBoxChanged)
        self.actionSettings.triggered.connect(OpenDialogSettings)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.total_shares_label.setText(
            _translate("MainWindow", "Total Shares"))
        self.min_shares_label.setText(
            _translate("MainWindow", "Minimum Shares"))
        self.load_Button.setText(_translate("MainWindow", "Load"))
        self.save_Button.setText(_translate("MainWindow", "Save"))
        self.menuProgram.setTitle(_translate("MainWindow", "Program"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionWikipedia.setText(_translate("MainWindow", "Wikipedia"))
        self.actionUpdate.setText(_translate("MainWindow", "Update"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))


class Ui_SettingsDialog(QtWidgets.QWidget):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.resize(400, 300)
        SettingsDialog.setMinimumSize(QtCore.QSize(400, 300))
        SettingsDialog.setMaximumSize(QtCore.QSize(400, 300))
        _translate = QtCore.QCoreApplication.translate
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            ":/resources/OnionSwitch_Logo.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SettingsDialog.setWindowIcon(icon)
        font = Fonts.Choose_Fonts(self, False, 10, "Arial")
        self.cancel_Button = QtWidgets.QPushButton(SettingsDialog)
        self.cancel_Button.setGeometry(QtCore.QRect(300, 260, 90, 28))
        self.cancel_Button.setObjectName("cancel_Button")
        self.ok_Button = QtWidgets.QPushButton(SettingsDialog)
        self.ok_Button.setGeometry(QtCore.QRect(200, 260, 90, 28))
        self.ok_Button.setObjectName("ok_Button")
        self.main_listWidget = QtWidgets.QListWidget(SettingsDialog)
        self.main_listWidget.setGeometry(QtCore.QRect(0, 0, 150, 300))
        self.main_listWidget.setObjectName("main_listview")
        self.main_listWidget.setFont(font)
        self.main_listWidget.addItem(_translate(
            "SettingsDialog", "General"))
        self.main_listWidget.setStyleSheet(
            "background-color: qlineargradient("
            "spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgb("
            "0, 0, 0), stop:1 rgb(60, 60, 60));")
        self.main_listWidget.item(0).setForeground(QtCore.Qt.white)

        self.general_groupbox = QtWidgets.QGroupBox(SettingsDialog)
        self.general_groupbox.setGeometry(QtCore.QRect(150, 0, 250, 300))
        self.general_groupbox.setObjectName("general_groupbox")
        self.general_groupbox.setStyleSheet(
            "QGroupBox#general_groupbox {background-color: qlineargradient("
            "spread:pad, x1:1, y1:0, x2:, y2:1, stop:0 rgb("
            "60, 60, 60), stop:1 rgb(60,60,60))};")
        self.general_groupbox.setObjectName("general_groupbox")
        self.choose_mersenne_prime_groupbox = QtWidgets.QGroupBox(
            self.general_groupbox)
        self.choose_mersenne_prime_groupbox.setObjectName(
            "choose_mersenne_prime_groupbox")
        self.choose_mersenne_prime_groupbox.setGeometry(0, 0, 250, 110)
        self.choose_mersenne_Label = QtWidgets.QLabel(
            self.choose_mersenne_prime_groupbox)
        self.choose_mersenne_Label.setGeometry(QtCore.QRect(10, 10, 171, 21))
        self.choose_mersenne_Label.setFont(font)
        self.choose_mersenne_Label.setObjectName("choose_mersenne_Label")
        self.choose_mersenne_Label.setStyleSheet("color:white")
        self.mersenne_comboBox = QtWidgets.QComboBox(
            self.choose_mersenne_prime_groupbox)
        self.mersenne_comboBox.setObjectName("mersenne_comboBox")
        self.mersenne_comboBox.setGeometry(QtCore.QRect(12, 40, 230, 22))
        self.mersenne_comboBox.addItem("Default")

        for number in sss.SSS_Functions.prime_array:
            self.mersenne_comboBox.addItem(str(number))

        self.language_groupbox = QtWidgets.QGroupBox(self.general_groupbox)
        self.language_groupbox.setObjectName("language_groupbox")
        self.language_groupbox.setGeometry(0, 105, 250, 80)
        self.language_Label = QtWidgets.QLabel(self.language_groupbox)
        self.language_Label.setObjectName("language_Label")
        self.language_Label.setGeometry(QtCore.QRect(12, 10, 100, 21))
        self.language_Label.setFont(font)
        self.language_Label.setStyleSheet("color: white")
        self.language_comboBox = QtWidgets.QComboBox(self.language_groupbox)
        self.language_comboBox.setObjectName("language_comboBox")
        self.language_comboBox.setGeometry(QtCore.QRect(12, 40, 230, 22))

        self.ok_Button.raise_()
        self.cancel_Button.raise_()

        self.retranslateUi(SettingsDialog)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

        self.cancel_Button.clicked.connect(SettingsDialog.close)

    def retranslateUi(self, SettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        SettingsDialog.setWindowTitle(_translate(
            "SettingsDialog", "Settings"))
        self.ok_Button.setText(_translate("SettingsDialog", "OK"))
        self.cancel_Button.setText(_translate("SettingsDialog", "Cancel"))
        self.language_Label.setText(_translate(
            "SettingsDialog", "Language:"))
        self.choose_mersenne_Label.setText(_translate(
            "SettingsDialog", "Prime Encryption:"))


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
