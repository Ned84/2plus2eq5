# -*- coding: utf-8 -*-
"""
*** Two Plus Two Eq 5 ***
"Easily share secrets in parts and reconstruct them again from
an minimum amount of parts.
Easily switch the Tor-Exit-Node Destination Country in
your Tor-Browser.
GUI Copyright (C) 2020  Ned84 ned84@protonmail.com
For further information visit:
https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing

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

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QFileDialog
from PyQt5.Qt import QApplication


import twotwofive_Functions as twotwofive
import twotwofive_Resources

import gnupg
from pathlib import Path
import os
import webbrowser
import threading
from urllib import request
from os import path
import subprocess

version = "0.1"


class Fonts():

    def Choose_Fonts(self, bold, size, font_type):
        font = QtGui.QFont()
        font.setFamily(font_type)
        if twotwofive.Secondary_Functions.platform == "Windows":
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


class Ui_MainWindow(QtWidgets.QMainWindow):

    # Update Parameter
    serverconnection = False
    versionnew = ""
    firstrun = True
    update_avail = False

    only_gui_vis = True

    gpg_pub_keyring = []
    gpg_priv_keyring = []
    usr_path = str(Path.home())

    # Settings parameter
    auto_update = False
    use_gpg_encrypt = False
    use_gpg_sign = False
    gpg_chosen_public_key = "No Key chosen"
    gpg_chosen_private_key = "No Key chosen"

    test = twotwofive.Secondary_Functions.platform

    gpg_path = ""
    language = ""

    twotwofive_Resources.qInitResources()

    def __init__(self, *args, **kwargs):
        super().__init__()

        param_details = twotwofive.Secondary_Functions.Init_Param_GUI(
            self, version, Ui_MainWindow.gpg_path)

        if twotwofive.Secondary_Functions.platform == "Windows":
            Ui_MainWindow.gpg_path = Ui_MainWindow.usr_path + '\\AppData\\Roaming\\gnupg'
        else:
            Ui_MainWindow.gpg_path = Ui_MainWindow.usr_path + '/.gnupg'

        Ui_MainWindow.auto_update = param_details['Auto_Update']
        Ui_MainWindow.update_avail = param_details['Update_available']
        Ui_MainWindow.use_gpg_encrypt = param_details['Use_GPG_Encr']
        Ui_MainWindow.use_gpg_sign = param_details['Use_GPG_Sign']
        if param_details['GPG_Path'] != "":
            Ui_MainWindow.gpg_path = param_details['GPG_Path']
        Ui_MainWindow.language = param_details['Language']

        try:
            def UpdateCheck():
                link = ("https://github.com/Ned84/"
                        "2plus2eq5/blob/master/"
                        "VERSION.md")
                url = request.urlopen(link)
                readurl = url.read()
                text = readurl.decode(encoding='utf-8', errors='ignore')

                stringindex = text.find("2plus2eq5-Version")

                if stringindex != -1:
                    Ui_MainWindow.versionnew = text[stringindex +
                                                    19:]
                    Ui_MainWindow.versionnew = \
                        Ui_MainWindow.versionnew.replace('_', '.')

                if version < Ui_MainWindow.versionnew:
                    Ui_MainWindow.serverconnection = True
                    Ui_MainWindow.update_avail = True

                else:
                    Ui_MainWindow.serverconnection = True
                    Ui_MainWindow.update_avail = False

                param_details = []
                param_details.append(Ui_MainWindow.auto_update)
                param_details.append(version)
                param_details.append(Ui_MainWindow.update_avail)
                param_details.append(Ui_MainWindow.use_gpg_encrypt)
                param_details.append(Ui_MainWindow.use_gpg_sign)
                param_details.append(twotwofive.Secondary_Functions.platform)
                param_details.append(Ui_MainWindow.gpg_path)
                param_details.append(Ui_MainWindow.language)

                twotwofive.Secondary_Functions.WriteSettingsToJson(
                    self, param_details)

            if Ui_MainWindow.auto_update is True:
                urlthread = threading.Thread(target=UpdateCheck, daemon=True)
                urlthread.start()

        except Exception:
            Ui_MainWindow.update_avail = False

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 300)
        MainWindow.setMinimumSize(QtCore.QSize(350, 300))
        MainWindow.setMaximumSize(QtCore.QSize(350, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Logo/SSS_Logo.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 350, 500))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setObjectName("tabWidget")
        if twotwofive.Secondary_Functions.platform == "Windows":
            font = "8pt Arial"
        else:
            font = "10pt Arial"
        stylesheet = """
        QTabBar::tab:selected {color: white;}
        QTabBar::tab { height: 25px; width: 175px;
        background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:, y2:1,
        stop:0 rgb(0,200,0), stop:1 rgb(0,250,0));
        font: """ + font + """;
        color : qlineargradient(spread:pad, x1:1, y1:0, x2:, y2:1,
        stop:0 rgb(50,50,50), stop:1 rgb(150,150,150));
        selection-background-color: rgb(255, 255, 255);}
        """
        self.tabWidget.setStyleSheet(stylesheet)
        self.create_tab = QtWidgets.QWidget()
        self.create_tab.setObjectName("create_tab")
        self.create_tab.setStyleSheet(
            "QWidget#create_tab {background-color: "
            "qlineargradient(spread:pad, x1:1, y1:0, x2:,"
            "y2:1, stop:0 rgb("
            "200,200,200), stop:1 rgb(253,253,253));}")
        self.tabWidget.addTab(self.create_tab, "")

        self.combine_tab = QtWidgets.QWidget()
        self.combine_tab.setObjectName("combine_tab")
        self.combine_tab.setStyleSheet(
            "QWidget#combine_tab {background-color: qlineargradient("
            "spread:pad, x1:1, y1:0, x2:, y2:1, stop:0 rgb("
            "200,200,200), stop:1 rgb(253,253,253));}")
        self.tabWidget.addTab(self.combine_tab, "")
        self.total_shares_spinBox = QtWidgets.QSpinBox(self.create_tab)
        self.total_shares_spinBox.setGeometry(QtCore.QRect(150, 30, 42, 22))
        self.total_shares_spinBox.setObjectName("total_shares_spinBox")
        self.min_shares_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.min_shares_spinBox.setGeometry(QtCore.QRect(10, 55, 42, 22))
        self.min_shares_spinBox.setObjectName("min_shares_spinBox")
        self.total_shares_label = QtWidgets.QLabel(self.create_tab)
        self.total_shares_label.setGeometry(QtCore.QRect(150, 10, 110, 16))
        self.total_shares_label.setObjectName("total_shares_label")
        self.total_shares_label.setFont(
            Fonts.Choose_Fonts(self, False, 10, "Arial"))
        self.min_shares_label = QtWidgets.QLabel(self.centralwidget)
        self.min_shares_label.setGeometry(
            QtCore.QRect(10, 35, 125, 16))
        self.min_shares_label.setObjectName("min_shares_label")
        self.min_shares_label.setFont(Fonts.Choose_Fonts(
            self, False, 10, "Arial"))
        self.load_lineEdit = QtWidgets.QLineEdit(self.create_tab)
        self.load_lineEdit.setGeometry(QtCore.QRect(10, 150, 211, 22))
        self.load_lineEdit.setObjectName("load_lineEdit")
        self.load_lineEdit.setReadOnly(True)
        self.load_Button = QtWidgets.QPushButton(self.create_tab)
        self.load_Button.setGeometry(QtCore.QRect(130, 180, 93, 28))
        self.load_Button.setObjectName("load_Button")
        self.save_lineEdit = QtWidgets.QLineEdit(self.combine_tab)
        self.save_lineEdit.setGeometry(QtCore.QRect(10, 150, 211, 22))
        self.save_lineEdit.setObjectName("save_lineEdit")
        self.save_lineEdit.setReadOnly(True)
        self.save_Button = QtWidgets.QPushButton(self.combine_tab)
        self.save_Button.setGeometry(QtCore.QRect(130, 180, 93, 28))
        self.save_Button.setObjectName("save_Button")
        self.combine_start_Button = QtWidgets.QPushButton(self.combine_tab)
        self.combine_start_Button.setGeometry(QtCore.QRect(240, 180, 93, 28))
        self.combine_start_Button.setObjectName("combine_start_Button")
        self.create_start_Button = QtWidgets.QPushButton(self.create_tab)
        self.create_start_Button.setGeometry(QtCore.QRect(240, 180, 93, 28))
        self.create_start_Button.setObjectName("create_start_Button")
        self.choose_mersenne_Label = QtWidgets.QLabel(
            self.create_tab)
        self.choose_mersenne_Label.setGeometry(QtCore.QRect(10, 60, 171, 21))
        self.choose_mersenne_Label.setFont(
            Fonts.Choose_Fonts(self, False, 10, "Arial"))
        self.choose_mersenne_Label.setObjectName("choose_mersenne_Label")
        self.mersenne_comboBox = QtWidgets.QComboBox(
            self.create_tab)
        self.mersenne_comboBox.setObjectName("mersenne_comboBox")
        self.mersenne_comboBox.setGeometry(QtCore.QRect(10, 80, 230, 22))
        self.mersenne_comboBox.addItem("Default")
        for number in twotwofive.SSS_Functions.prime_array:
            self.mersenne_comboBox.addItem(str(number))

        self.combine_mersenne_Label = QtWidgets.QLabel(
            self.combine_tab)
        self.combine_mersenne_Label.setGeometry(QtCore.QRect(10, 60, 171, 21))
        self.combine_mersenne_Label.setFont(
            Fonts.Choose_Fonts(self, False, 10, "Arial"))
        self.combine_mersenne_Label.setObjectName("combine_mersenne_Label")
        self.combine_mersenne_comboBox = QtWidgets.QComboBox(
            self.combine_tab)
        self.combine_mersenne_comboBox.setObjectName(
            "combine_mersenne_comboBox")
        self.combine_mersenne_comboBox.setGeometry(
            QtCore.QRect(10, 80, 230, 22))
        for number in twotwofive.SSS_Functions.prime_array:
            self.combine_mersenne_comboBox.addItem(str(number))

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
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.tabWidget.setCurrentWidget(self.tabWidget.findChild(
            QtWidgets.QWidget, "create_tab"))

        self.total_shares_spinBox.setValue(twotwofive.SSS_Functions.total_shares)
        self.min_shares_spinBox.setValue(twotwofive.SSS_Functions.min_shares)

        if Ui_MainWindow.update_avail is True:
            self.statusbar.showMessage("Update available. Help -> Update")

        @pyqtSlot()
        def OpenLoadFilePicker():
            try:
                self.statusbar.showMessage("")
                fileName = QFileDialog.getOpenFileName(
                    self,
                    'Open file',
                    'c:\\',
                    "Encrypted File, Text File (*.asc *.txt)")
                if fileName[0]:
                    self.load_lineEdit.setText(fileName[0])

            except Exception as exc:
                twotwofive.Secondary_Functions.WriteLog(self, exc)

        @pyqtSlot()
        def OpenSaveFilePicker():
            try:
                self.statusbar.showMessage("")
                chosen_filenames = ""

                fileNames = QFileDialog.getOpenFileNames(
                    self,
                    'Save Files',
                    'c:\\',
                    "Share Files (*.share)")

                i = 0
                for files in fileNames[0]:
                    i += 1

                if i >= self.min_shares_spinBox.value():
                    if fileNames[0]:
                        twotwofive.Secondary_Functions.share_fileNames = fileNames
                        for name in fileNames[0]:
                            chosen_filenames += name + " "
                        self.save_lineEdit.setText(chosen_filenames)
                else:
                    self.statusbar.showMessage(
                        "Loaded Shares have to be >= minimum shares")

            except Exception as exc:
                twotwofive.Secondary_Functions.WriteLog(self, exc)

        @pyqtSlot()
        def Start_Creating_Shares():
            try:
                succeeded = True
                self.statusbar.showMessage("")
                if(self.load_lineEdit.text() != ""):
                    if self.min_shares_spinBox.value() <=\
                         self.total_shares_spinBox.value():

                        if Ui_MainWindow.use_gpg_encrypt is True and\
                           Ui_MainWindow.use_gpg_sign is True:
                            if Ui_MainWindow.gpg_chosen_private_key !=\
                               "No Key chosen" and\
                                Ui_MainWindow.gpg_chosen_public_key !=\
                               "No Key chosen":
                                twotwofive.Secondary_Functions.Sign_Encrypt_File(
                                    self, Ui_MainWindow.gpg_path,
                                    self.load_lineEdit.text(),
                                    Ui_MainWindow.gpg_chosen_private_key,
                                    Ui_MainWindow.gpg_chosen_public_key)
                            else:
                                self.statusbar.showMessage(
                                    "Private or public key not specified")
                                succeeded = False
                        else:

                            if Ui_MainWindow.use_gpg_encrypt is True:
                                if Ui_MainWindow.gpg_chosen_public_key !=\
                                   "No Key chosen":
                                    twotwofive.Secondary_Functions.Encrypt_File(
                                        self,
                                        Ui_MainWindow.gpg_path,
                                        self.load_lineEdit.text(),
                                        Ui_MainWindow.gpg_chosen_public_key)
                                else:
                                    self.statusbar.showMessage(
                                        "Public key not specified")
                                    succeeded = False
                            if Ui_MainWindow.use_gpg_sign is True:
                                if Ui_MainWindow.gpg_chosen_private_key !=\
                                   "No Key chosen":
                                    twotwofive.Secondary_Functions.Sign_File(
                                        self,
                                        Ui_MainWindow.gpg_path,
                                        self.load_lineEdit.text(),
                                        Ui_MainWindow.gpg_chosen_private_key)
                                else:
                                    self.statusbar.showMessage(
                                        "Private key not specified")
                                    succeeded = False

                        if succeeded is True:
                            if Ui_MainWindow.use_gpg_encrypt is True or\
                               Ui_MainWindow.use_gpg_sign is True:
                                file = twotwofive.Secondary_Functions.Read_File(
                                    self, self.load_lineEdit.text() + '.asc')
                            else:
                                file = twotwofive.Secondary_Functions.Read_File(
                                    self, self.load_lineEdit.text())

                            shares = twotwofive.SSS_Functions.Share_Creation(
                                self,
                                file,
                                self.mersenne_comboBox.currentText())
                            path = self.load_lineEdit.text()
                            path = path[:path.rfind('/')]

                            if twotwofive.Secondary_Functions.Save_Shares(
                                    self,
                                    path,
                                    shares,
                                    twotwofive.SSS_Functions.security_lvl,
                                    self.min_shares_spinBox.value(),
                                    self.total_shares_spinBox.value()) is True:
                                self.statusbar.showMessage(
                                    "Shares successfully created")
                                if twotwofive.Secondary_Functions.platform == "Windows":
                                    os.startfile(path + "/Shares")
                                else:
                                    subprocess.Popen(["xdg-open", path + "/Shares"])
                    else:
                        self.statusbar.showMessage(
                            "Min. shares have to be less than total")
                        succeeded = False
                else:
                    self.statusbar.showMessage("Error: No file to load")
                    succeeded = False

            except Exception as exc:
                twotwofive.Secondary_Functions.WriteLog(self, exc)

        @pyqtSlot()
        def Start_Combining_Shares():
            try:
                self.statusbar.showMessage("")
                if(self.save_lineEdit.text() != ""):
                    shares = twotwofive.Secondary_Functions.Load_Shares(
                        self,
                        twotwofive.Secondary_Functions.share_fileNames)

                    path = twotwofive.Secondary_Functions.share_fileNames[0][0]
                    path = str(path)
                    path = path[:path.rfind('/')]

                    if twotwofive.SSS_Functions.Share_Combining(
                            self, self.combine_mersenne_comboBox.currentText(),
                            self.min_shares_spinBox.value(),
                            shares,
                            path):
                        self.statusbar.showMessage(
                            "Shares successfully combined")

                        if twotwofive.Secondary_Functions.platform == "Windows":
                            os.startfile(path)
                        else:
                            subprocess.Popen(["xdg-open", path])
                    else:
                        self.statusbar.showMessage(
                            "Error: Shares not combined")
                else:
                    self.statusbar.showMessage("Error: No shares to load")
            except Exception as exc:
                twotwofive.Secondary_Functions.WriteLog(self, exc)

        @pyqtSlot()
        def TotalSprinBoxChanged():
            self.statusbar.showMessage("")
            twotwofive.SSS_Functions.total_shares = self.total_shares_spinBox.value()

        @pyqtSlot()
        def MinSprinBoxChanged():
            self.statusbar.showMessage("")
            twotwofive.SSS_Functions.min_shares = self.min_shares_spinBox.value()

        @pyqtSlot()
        def OpenDialogAbout():
            self.statusbar.showMessage("")
            if Ui_MainWindow.only_gui_vis is True:
                Ui_MainWindow.only_gui_vis = False
                self.window = QtWidgets.QDialog()
                self.window.setWindowFlags(
                    self.windowFlags() | QtCore.Qt.CustomizeWindowHint)
                self.window.setWindowFlags(
                    self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
                self.window.installEventFilter(self)
                self.ui = Ui_AboutDialog()
                self.ui.setupUi(self.window)
                self.window.finished.connect(DialogAboutClosed)
                self.window.show()

        def DialogAboutClosed():
            Ui_MainWindow.only_gui_vis = True

        @pyqtSlot()
        def OpenDialogUpdate():
            self.statusbar.showMessage("")
            if Ui_MainWindow.only_gui_vis is True:
                Ui_MainWindow.only_gui_vis = False
                self.window = QtWidgets.QDialog()
                self.window.setWindowFlags(
                    self.windowFlags() | QtCore.Qt.CustomizeWindowHint)
                self.window.setWindowFlags(
                    self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
                self.window.installEventFilter(self)
                self.ui = Ui_UpdateDialog()
                self.ui.setupUi(self.window)
                self.window.finished.connect(DialogUpdateClosed)
                self.window.show()

        def DialogUpdateClosed():
            Ui_MainWindow.only_gui_vis = True

        @pyqtSlot()
        def OpenDialogSettings():
            if Ui_MainWindow.only_gui_vis is True:
                Ui_MainWindow.only_gui_vis = False
                self.statusbar.showMessage("")
                self.window_settings = QtWidgets.QDialog()
                self.window_settings.setWindowFlags(
                    self.windowFlags() | QtCore.Qt.CustomizeWindowHint)
                self.window_settings.setWindowFlags(
                    self.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
                self.window_settings.installEventFilter(self)
                self.ui = Ui_SettingsDialog()
                self.ui.setupUi(self.window_settings)
                self.window_settings.finished.connect(DialogSettingsClosed)
                self.window_settings.show()

        def DialogSettingsClosed():
            Ui_MainWindow.only_gui_vis = True

        @pyqtSlot()
        def Wiki_Clipboard():
            clip = QApplication.clipboard()
            clip.clear(mode=clip.Clipboard)
            clip.setText("https://en.wikipedia.org/wiki/"
                         "Shamir%27s_Secret_Sharing",
                         mode=clip.Clipboard)
            self.statusbar.showMessage(
                "URL to Wikipedia: SSS is saved to clipboard")

        @pyqtSlot()
        def Changed_Mersenne_Combobox():
            self.statusbar.showMessage("")
            if self.mersenne_comboBox.currentText() != "Default":
                if int(self.mersenne_comboBox.currentText()) > 1400000:
                    self.statusbar.showMessage(
                        "High Encryption Lvls can take a while to process")

        self.load_Button.clicked.connect(OpenLoadFilePicker)
        self.create_start_Button.clicked.connect(Start_Creating_Shares)
        self.total_shares_spinBox.valueChanged.connect(TotalSprinBoxChanged)
        self.min_shares_spinBox.valueChanged.connect(MinSprinBoxChanged)
        self.actionSettings.triggered.connect(OpenDialogSettings)
        self.save_Button.clicked.connect(OpenSaveFilePicker)
        self.combine_start_Button.clicked.connect(Start_Combining_Shares)
        self.actionAbout.triggered.connect(OpenDialogAbout)
        self.actionWikipedia.triggered.connect(Wiki_Clipboard)
        self.actionUpdate.triggered.connect(OpenDialogUpdate)
        self.mersenne_comboBox.currentTextChanged.connect(
            Changed_Mersenne_Combobox)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "2 + 2 = 5"))
        self.total_shares_label.setText(
            _translate("MainWindow", "Total Shares"))
        self.min_shares_label.setText(
            _translate("MainWindow", "Minimum Shares"))
        self.load_Button.setText(_translate("MainWindow", "Load"))
        self.save_Button.setText(_translate("MainWindow", "Load"))
        self.create_start_Button.setText(_translate("MainWindow", "Start"))
        self.combine_start_Button.setText(_translate("MainWindow", "Start"))
        self.menuProgram.setTitle(_translate("MainWindow", "Program"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionWikipedia.setText(_translate("MainWindow", "Wikipedia"))
        self.actionUpdate.setText(_translate("MainWindow", "Update"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.create_tab), _translate("MainWindow", "Create"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.combine_tab), _translate("MainWindow", "Combine"))
        self.choose_mersenne_Label.setText(_translate(
            "SettingsDialog", "Encryption Level:"))
        self.combine_mersenne_Label.setText(_translate(
            "SettingsDialog", "Encryption Level:"))


class Ui_SettingsDialog(QtWidgets.QWidget):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.resize(400, 300)
        SettingsDialog.setMinimumSize(QtCore.QSize(400, 300))
        SettingsDialog.setMaximumSize(QtCore.QSize(400, 300))
        _translate = QtCore.QCoreApplication.translate
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            ":/Logo/SSS_Logo.png"),
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
        self.main_listWidget.addItem(_translate(
            "SettingsDialog", "GPG"))
        self.main_listWidget.setStyleSheet(
            "background-color: qlineargradient("
            "spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgb("
            "0, 0, 0), stop:1 rgb(60, 60, 60));")
        self.main_listWidget.item(0).setForeground(QtCore.Qt.white)
        self.main_listWidget.item(1).setForeground(QtCore.Qt.white)

        self.general_groupbox = QtWidgets.QGroupBox(SettingsDialog)
        self.general_groupbox.setGeometry(QtCore.QRect(150, 0, 250, 300))
        self.general_groupbox.setObjectName("general_groupbox")
        self.general_groupbox.setStyleSheet(
            "QGroupBox#general_groupbox {background-color: qlineargradient("
            "spread:pad, x1:1, y1:0, x2:, y2:1, stop:0 rgb("
            "60, 60, 60), stop:1 rgb(60,60,60))};")
        self.general_groupbox.setObjectName("general_groupbox")
        self.language_groupbox = QtWidgets.QGroupBox(self.general_groupbox)
        self.language_groupbox.setObjectName("language_groupbox")
        self.language_groupbox.setGeometry(0, 0, 250, 80)
        self.language_Label = QtWidgets.QLabel(self.language_groupbox)
        self.language_Label.setObjectName("language_Label")
        self.language_Label.setGeometry(QtCore.QRect(12, 10, 100, 21))
        self.language_Label.setFont(font)
        self.language_Label.setStyleSheet("color: white")
        self.language_comboBox = QtWidgets.QComboBox(self.language_groupbox)
        self.language_comboBox.setObjectName("language_comboBox")
        self.language_comboBox.setGeometry(QtCore.QRect(12, 40, 230, 22))
        self.language_comboBox.addItem("English")

        self.auto_update_groupbox = QtWidgets.QGroupBox(self.general_groupbox)
        self.auto_update_groupbox.setGeometry(QtCore.QRect(0, 70, 250, 100))
        self.auto_update_groupbox.setObjectName("auto_update_groupbox")
        self.auto_update_groupbox.setStyleSheet(
            "QGroupBox#auto_update_groupbox {"
            "background-color: qlineargradient("
            "spread:pad, x1:1, y1:0, x2:, y2:1, stop:0 rgb("
            "60, 60, 60), stop:1 rgb(60,60,60))};")
        self.auto_update_CheckBox = QtWidgets.QCheckBox(
            self.auto_update_groupbox)
        self.auto_update_CheckBox.setGeometry(QtCore.QRect(12, 15, 190, 21))
        self.auto_update_CheckBox.setFont(font)
        self.auto_update_CheckBoxLabel = QtWidgets.QLabel(
            self.auto_update_groupbox)
        self.auto_update_CheckBoxLabel.setObjectName(
            "auto_update_CheckBoxLabel")
        self.auto_update_CheckBoxLabel.setGeometry(35, 15, 190, 21)
        self.auto_update_CheckBoxLabel.setFont(font)
        self.auto_update_CheckBoxLabel.setStyleSheet("color: white")

        self.use_gpg_encrypt_Checkbox = QtWidgets.QCheckBox(
            self.auto_update_groupbox)
        self.use_gpg_encrypt_Checkbox.setGeometry(
            QtCore.QRect(12, 40, 190, 21))
        self.use_gpg_encrypt_Checkbox.setFont(font)
        self.use_gpg_encrypt_CheckboxLabel = QtWidgets.QLabel(
            self.auto_update_groupbox)
        self.use_gpg_encrypt_CheckboxLabel.setObjectName(
            "use_gpg_encrypt_CheckboxLabel")
        self.use_gpg_encrypt_CheckboxLabel.setGeometry(35, 40, 190, 21)
        self.use_gpg_encrypt_CheckboxLabel.setFont(font)
        self.use_gpg_encrypt_CheckboxLabel.setStyleSheet("color: white")

        self.use_gpg_sign_Checkbox = QtWidgets.QCheckBox(
            self.auto_update_groupbox)
        self.use_gpg_sign_Checkbox.setGeometry(QtCore.QRect(12, 65, 190, 21))
        self.use_gpg_sign_Checkbox.setFont(font)
        self.use_gpg_sign_CheckboxLabel = QtWidgets.QLabel(
            self.auto_update_groupbox)
        self.use_gpg_sign_CheckboxLabel.setObjectName(
            "use_gpg_sign_CheckboxLabel")
        self.use_gpg_sign_CheckboxLabel.setGeometry(35, 65, 190, 21)
        self.use_gpg_sign_CheckboxLabel.setFont(font)
        self.use_gpg_sign_CheckboxLabel.setStyleSheet("color: white")

        self.gpg_groupbox = QtWidgets.QGroupBox(SettingsDialog)
        self.gpg_groupbox.setGeometry(QtCore.QRect(150, 0, 250, 300))
        self.gpg_groupbox.setObjectName("gpg_groupbox")
        self.gpg_groupbox.setStyleSheet(
            "QGroupBox#gpg_groupbox {background-color: qlineargradient("
            "spread:pad, x1:1, y1:0, x2:, y2:1, stop:0 rgb("
            "60, 60, 60), stop:1 rgb(60,60,60))};")
        self.gpg_groupbox.setObjectName("gpg_groupbox")
        self.gpg_groupbox.hide()

        self.gpg_public_groupbox = QtWidgets.QGroupBox(
            self.gpg_groupbox)
        self.gpg_public_groupbox.setObjectName(
            "gpg_public_groupbox")
        self.gpg_public_groupbox.setGeometry(0, 0, 250, 70)
        self.gpg_public_Label = QtWidgets.QLabel(
            self.gpg_public_groupbox)
        self.gpg_public_Label.setGeometry(QtCore.QRect(10, 10, 171, 21))
        self.gpg_public_Label.setFont(font)
        self.gpg_public_Label.setObjectName("gpg_public_Label")
        self.gpg_public_Label.setStyleSheet("color:white")
        self.gpg_public_comboBox = QtWidgets.QComboBox(
            self.gpg_public_groupbox)
        self.gpg_public_comboBox.setObjectName("gpg_public_comboBox")
        self.gpg_public_comboBox.setGeometry(QtCore.QRect(12, 40, 230, 22))
        self.gpg_public_comboBox.addItem("")

        self.gpg_private_groupbox = QtWidgets.QGroupBox(
            self.gpg_groupbox)
        self.gpg_private_groupbox.setObjectName(
            "gpg_private_groupbox")
        self.gpg_private_groupbox.setGeometry(0, 65, 250, 70)
        self.gpg_private_Label = QtWidgets.QLabel(
            self.gpg_private_groupbox)
        self.gpg_private_Label.setGeometry(QtCore.QRect(10, 10, 171, 21))
        self.gpg_private_Label.setFont(font)
        self.gpg_private_Label.setObjectName("gpg_private_Label")
        self.gpg_private_Label.setStyleSheet("color:white")
        self.gpg_private_comboBox = QtWidgets.QComboBox(
            self.gpg_private_groupbox)
        self.gpg_private_comboBox.setObjectName("gpg_private_comboBox")
        self.gpg_private_comboBox.setGeometry(QtCore.QRect(12, 40, 230, 22))
        self.gpg_private_comboBox.addItem("")

        self.gpg_path_groupbox = QtWidgets.QGroupBox(
            self.gpg_groupbox)
        self.gpg_path_groupbox.setObjectName(
            "gpg_path_groupbox")
        self.gpg_path_groupbox.setGeometry(0, 130, 250, 105)
        self.gpg_path_Label = QtWidgets.QLabel(
            self.gpg_path_groupbox)
        self.gpg_path_Label.setGeometry(QtCore.QRect(10, 10, 171, 21))
        self.gpg_path_Label.setFont(font)
        self.gpg_path_Label.setObjectName("gpg_path_Label")
        self.gpg_path_Label.setStyleSheet("color:white")
        self.gpg_path_lineedit = QtWidgets.QLineEdit(
            self.gpg_path_groupbox)
        self.gpg_path_lineedit.setObjectName("gpg_path_lineedit")
        self.gpg_path_lineedit.setGeometry(QtCore.QRect(12, 40, 230, 22))
        self.gpg_path_lineedit.setText("")
        self.gpg_path_lineedit.setReadOnly(True)
        self.gpg_choose_Button = QtWidgets.QPushButton(self.gpg_path_groupbox)
        self.gpg_choose_Button.setGeometry(QtCore.QRect(150, 70, 90, 28))
        self.gpg_choose_Button.setObjectName("gpg_choose_Button")

        try:
            # List keyrings
            gpg = gnupg.GPG(gnupghome=Ui_MainWindow.gpg_path)
            public_keys = gpg.list_keys()
            private_keys = gpg.list_keys(True)

            Ui_MainWindow.gpg_pub_keyring = []
            Ui_MainWindow.gpg_priv_keyring = []
            self.gpg_public_comboBox.clear()
            self.gpg_private_comboBox.clear()

            self.gpg_public_comboBox.addItem("No Key chosen")
            self.gpg_private_comboBox.addItem("No Key chosen")

            for sub, value in vars(public_keys).items():
                if sub == "uids":
                    for id in value:
                        Ui_MainWindow.gpg_pub_keyring.append(id)

            for sub, value in vars(private_keys).items():
                if sub == "uids":
                    for id in value:
                        Ui_MainWindow.gpg_priv_keyring.append(id)

            if len(Ui_MainWindow.gpg_priv_keyring) == 0:
                self.gpg_private_comboBox.clear()
                self.gpg_private_comboBox.addItem("No Keys found")

            if len(Ui_MainWindow.gpg_pub_keyring) == 0:
                self.gpg_public_comboBox.clear()
                self.gpg_public_comboBox.addItem("No Keys found")
        except Exception as exc:
            twotwofive.Secondary_Functions.WriteLog(self, exc)

        self.ok_Button.raise_()
        self.cancel_Button.raise_()

        self.auto_update_CheckBox.setChecked(Ui_MainWindow.auto_update)
        self.use_gpg_encrypt_Checkbox.setChecked(Ui_MainWindow.use_gpg_encrypt)
        self.use_gpg_sign_Checkbox.setChecked(Ui_MainWindow.use_gpg_sign)

        for i, key in enumerate(Ui_MainWindow.gpg_pub_keyring):
            self.gpg_public_comboBox.addItem(key)
            if key == Ui_MainWindow.gpg_chosen_public_key:
                self.gpg_public_comboBox.setCurrentIndex(i + 1)

        if Ui_MainWindow.gpg_chosen_public_key == "":
            self.gpg_public_comboBox.setCurrentIndex(0)

        for i, key in enumerate(Ui_MainWindow.gpg_priv_keyring):
            self.gpg_private_comboBox.addItem(key)
            if key == Ui_MainWindow.gpg_chosen_private_key:
                self.gpg_private_comboBox.setCurrentIndex(i + 1)

        if Ui_MainWindow.gpg_chosen_public_key == "":
            self.gpg_public_comboBox.setCurrentIndex(0)

        self.gpg_path_lineedit.setText(Ui_MainWindow.gpg_path)

        self.retranslateUi(SettingsDialog)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

        @pyqtSlot()
        def Main_SelectionChanged():

            if self.main_listWidget.currentItem().text() == "General" or\
                    self.main_listWidget.currentItem().text() == "Allgemein":
                self.gpg_groupbox.hide()
                self.general_groupbox.show()
                self.ok_Button.raise_()
                self.cancel_Button.raise_()

            if self.main_listWidget.currentItem().text() == "GPG":
                self.general_groupbox.hide()
                self.gpg_groupbox.show()
                self.ok_Button.raise_()
                self.cancel_Button.raise_()

        def auto_update_CheckBoxLabel_clicked():
            self.auto_update_CheckBox.setChecked(
                self.auto_update_CheckBox.isChecked() ^ True)

        def use_gpg_encrypt_CheckBoxLabel_clicked():
            self.use_gpg_encrypt_Checkbox.setChecked(
                self.use_gpg_encrypt_Checkbox.isChecked() ^ True)

        def use_gpg_sign_CheckBoxLabel_clicked():
            self.use_gpg_sign_Checkbox.setChecked(
                self.use_gpg_sign_Checkbox.isChecked() ^ True)

        @pyqtSlot()
        def OkPressed():
            Ui_MainWindow.auto_update = self.auto_update_CheckBox.isChecked()
            Ui_MainWindow.gpg_chosen_public_key =\
                self.gpg_public_comboBox.currentText()
            Ui_MainWindow.gpg_chosen_private_key =\
                self.gpg_private_comboBox.currentText()
            Ui_MainWindow.gpg_path = self.gpg_path_lineedit.text()
            Ui_MainWindow.use_gpg_encrypt =\
                self.use_gpg_encrypt_Checkbox.isChecked()
            Ui_MainWindow.use_gpg_sign = self.use_gpg_sign_Checkbox.isChecked()
            Ui_MainWindow.language = self.language_comboBox.currentText()

            param_details = []
            param_details.append(Ui_MainWindow.auto_update)
            param_details.append(version)
            param_details.append(Ui_MainWindow.update_avail)
            param_details.append(Ui_MainWindow.use_gpg_encrypt)
            param_details.append(Ui_MainWindow.use_gpg_sign)
            param_details.append(twotwofive.Secondary_Functions.platform)
            param_details.append(Ui_MainWindow.gpg_path)
            param_details.append(Ui_MainWindow.language)

            twotwofive.Secondary_Functions.WriteSettingsToJson(self, param_details)
            SettingsDialog.close()

        @pyqtSlot()
        def ChooseGPGPath():
            try:
                dial_path = QFileDialog.getExistingDirectory(
                    self, "Select Tor Directory")
                if dial_path:
                    if path.exists(
                        dial_path +
                        twotwofive.Secondary_Functions.path_separator +
                        'pubring.kbx'
                         ) is True:

                        self.gpg_path_lineedit.setText(dial_path)

                        # List keyrings
                        gpg = gnupg.GPG(gnupghome=dial_path)
                        public_keys = gpg.list_keys()
                        private_keys = gpg.list_keys(True)

                        Ui_MainWindow.gpg_pub_keyring = []
                        Ui_MainWindow.gpg_priv_keyring = []
                        self.gpg_public_comboBox.clear()
                        self.gpg_private_comboBox.clear()

                        self.gpg_public_comboBox.addItem("No Key chosen")
                        self.gpg_private_comboBox.addItem("No Key chosen")

                        for sub, value in vars(public_keys).items():
                            if sub == "uids":
                                for id in value:
                                    Ui_MainWindow.gpg_pub_keyring.append(id)

                        for sub, value in vars(private_keys).items():
                            if sub == "uids":
                                for id in value:
                                    Ui_MainWindow.gpg_priv_keyring.append(id)

                        if len(Ui_MainWindow.gpg_priv_keyring) == 0:
                            self.gpg_private_comboBox.clear()
                            self.gpg_private_comboBox.addItem("No Keys found")

                        if len(Ui_MainWindow.gpg_pub_keyring) == 0:
                            self.gpg_public_comboBox.clear()
                            self.gpg_public_comboBox.addItem("No Keys found")

                        for i, key in enumerate(Ui_MainWindow.gpg_pub_keyring):
                            self.gpg_public_comboBox.addItem(key)
                            if key == Ui_MainWindow.gpg_chosen_public_key:
                                self.gpg_public_comboBox.setCurrentIndex(i + 1)

                        if Ui_MainWindow.gpg_chosen_public_key == "":
                            self.gpg_public_comboBox.setCurrentIndex(0)

                        for i, key in enumerate(
                             Ui_MainWindow.gpg_priv_keyring):
                            self.gpg_private_comboBox.addItem(key)
                            if key == Ui_MainWindow.gpg_chosen_private_key:
                                self.gpg_private_comboBox.setCurrentIndex(
                                    i + 1)

                        if Ui_MainWindow.gpg_chosen_public_key == "":
                            self.gpg_public_comboBox.setCurrentIndex(0)

            except Exception as exc:
                twotwofive.Secondary_Functions.WriteLog(self, exc)

        self.ok_Button.clicked.connect(OkPressed)
        self.cancel_Button.clicked.connect(SettingsDialog.close)
        self.main_listWidget.currentItemChanged.connect(Main_SelectionChanged)
        clickable_Label(self.auto_update_CheckBoxLabel).connect(
            auto_update_CheckBoxLabel_clicked)
        clickable_Label(self.use_gpg_encrypt_CheckboxLabel).connect(
            use_gpg_encrypt_CheckBoxLabel_clicked)
        clickable_Label(self.use_gpg_sign_CheckboxLabel).connect(
            use_gpg_sign_CheckBoxLabel_clicked)
        self.gpg_choose_Button.clicked.connect(ChooseGPGPath)

    def retranslateUi(self, SettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        SettingsDialog.setWindowTitle(_translate(
            "SettingsDialog", "Settings"))
        self.ok_Button.setText(_translate("SettingsDialog", "OK"))
        self.cancel_Button.setText(_translate("SettingsDialog", "Cancel"))
        self.language_Label.setText(_translate(
            "SettingsDialog", "Language:"))
        self.gpg_public_Label.setText(_translate(
            "SettingsDialog", "GPG Public Keys:"))
        self.auto_update_CheckBoxLabel.setText(_translate(
            "SettingsDialog", "Auto Update Check"))
        self.use_gpg_encrypt_CheckboxLabel.setText(_translate(
            "SettingsDialog", "Use GPG Encryption"))
        self.use_gpg_sign_CheckboxLabel.setText(_translate(
            "SettingsDialog", "Use GPG Signing"))
        self.gpg_private_Label.setText(_translate(
            "SettingsDialog", "GPG Signing Keys:"))
        self.gpg_path_Label.setText(_translate(
            "SettingsDialog", "GPG Path:"))
        self.gpg_choose_Button.setText(_translate(
            "SettingsDialog", "Open"))


def clickable_Label(widget):

    class Filter(QtCore.QObject):
        clicked = QtCore.pyqtSignal()

        def eventFilter(self, obj, event):

            if obj == widget:
                if event.type() == QtCore.QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                        return True

            return False

    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked


class Ui_AboutDialog(QtWidgets.QWidget):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        AboutDialog.resize(400, 250)
        AboutDialog.setMinimumSize(QtCore.QSize(400, 250))
        AboutDialog.setMaximumSize(QtCore.QSize(400, 250))
        AboutDialog.setStyleSheet(
            "QDialog#AboutDialog {background-color: qlineargradient("
            "spread:pad, x1:1, y1:0, x2:, y2:1, stop:0 rgb("
            "200,200,200), stop:1 rgb(253,253,253));}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            ":/Logo/SSS_Logo.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AboutDialog.setWindowIcon(icon)
        self.closeButton = QtWidgets.QPushButton(AboutDialog)
        self.closeButton.setGeometry(QtCore.QRect(290, 210, 93, 28))
        self.closeButton.setObjectName("closeButton")
        self.ned84_logo_frame = QtWidgets.QFrame(AboutDialog)
        self.ned84_logo_frame.setGeometry(QtCore.QRect(10, 50, 141, 131))
        self.ned84_logo_frame.setStyleSheet(
            "image: url(:/Logo/SSS_Logo.png);")
        self.ned84_logo_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ned84_logo_frame.setObjectName("sss_logo_frame")
        self.label = QtWidgets.QLabel(AboutDialog)
        self.label.setGeometry(QtCore.QRect(190, 20, 200, 31))
        font = Fonts.Choose_Fonts(self, True, 10, "Arial")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(AboutDialog)
        self.label_2.setGeometry(QtCore.QRect(190, 50, 190, 130))
        font = Fonts.Choose_Fonts(self, False, 8, "Arial")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.trans = QtCore.QTranslator(self)

        self.retranslateUi(AboutDialog)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

        @pyqtSlot()
        def Close_About():
            AboutDialog.close()

        self.closeButton.clicked.connect(Close_About)

    def retranslateUi(self, AboutDialog):
        _translate = QtCore.QCoreApplication.translate
        AboutDialog.setWindowTitle(_translate("AboutDialog", "About"))
        self.closeButton.setText(_translate("AboutDialog", "Close"))
        self.label.setText(_translate(
            "AboutDialog", "2 + 2 = 5"))
        string_1 = "Version: "
        string_2 = (_translate("AboutDialog",
                               "Easily share secrets in parts\n"
                               "and reconstruct them again from\n"
                               "an minimum amount of parts.\n"
                               "GUI Copyright (C) 2020  Ned84\n"
                               "ned84@protonmail.com"))

        self.label_2.setText(string_1 + version + "\n" +
                             "\n" +
                             string_2)


class Ui_UpdateDialog(QtWidgets.QWidget):
    def setupUi(self, UpdateDialog):
        UpdateDialog.setObjectName("UpdateDialog")
        UpdateDialog.resize(400, 250)
        UpdateDialog.setMinimumSize(QtCore.QSize(400, 250))
        UpdateDialog.setMaximumSize(QtCore.QSize(400, 250))
        UpdateDialog.setStyleSheet(
            "QDialog#UpdateDialog {background-color: qlineargradient("
            "spread:pad, x1:1, y1:0, x2:, y2:1, stop:0 rgb("
            "200,200,200), stop:1 rgb(253,253,253));}")
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/Logo/SSS_Logo.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UpdateDialog.setWindowIcon(icon)
        self.cancelButton = QtWidgets.QPushButton(UpdateDialog)
        self.cancelButton.setGeometry(QtCore.QRect(290, 210, 93, 28))
        self.cancelButton.setObjectName("Cancel")
        self.updateButton = QtWidgets.QPushButton(UpdateDialog)
        self.updateButton.setGeometry(QtCore.QRect(180, 210, 93, 28))
        self.updateButton.setObjectName("updateButton")
        self.SSS_logo_frame = QtWidgets.QFrame(UpdateDialog)
        self.SSS_logo_frame.setGeometry(QtCore.QRect(10, 50, 141, 131))
        self.SSS_logo_frame.setStyleSheet(
            "image: url(:/Logo/SSS_Logo.png);")
        self.SSS_logo_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SSS_logo_frame.setObjectName("SSS_logo_frame")
        self.label = QtWidgets.QLabel(UpdateDialog)
        self.label.setGeometry(QtCore.QRect(200, 20, 280, 31))
        self.label2 = QtWidgets.QLabel(UpdateDialog)
        self.label2.setGeometry(QtCore.QRect(170, 60, 301, 131))
        self.label3 = QtWidgets.QLabel(UpdateDialog)
        self.label3.setGeometry(QtCore.QRect(170, 60, 301, 131))
        self.label4 = QtWidgets.QLabel(UpdateDialog)
        self.label4.setGeometry(QtCore.QRect(170, 60, 301, 131))
        font = Fonts.Choose_Fonts(self, True, 12, "Arial")
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.trans = QtCore.QTranslator(self)

        self.retranslateUi(UpdateDialog)
        QtCore.QMetaObject.connectSlotsByName(UpdateDialog)

        Ui_MainWindow.update_avail = False

        param_details = []
        param_details.append(Ui_MainWindow.auto_update)
        param_details.append(version)
        param_details.append(Ui_MainWindow.update_avail)
        param_details.append(Ui_MainWindow.use_gpg_encrypt)
        param_details.append(Ui_MainWindow.use_gpg_sign)
        param_details.append(twotwofive.Secondary_Functions.platform)
        param_details.append(Ui_MainWindow.gpg_path)
        param_details.append(Ui_MainWindow.language)

        twotwofive.Secondary_Functions.WriteSettingsToJson(self, param_details)

        @pyqtSlot()
        def StartUpdateProc():
            Ui_MainWindow.update_avail = False
            webbrowser.open(
                'https://github.com/Ned84/2plus2eq5/releases')

        @pyqtSlot()
        def Close_Update():
            UpdateDialog.close()

        self.cancelButton.clicked.connect(Close_Update)

        self.updateButton.clicked.connect(StartUpdateProc)

    def retranslateUi(self, UpdateDialog):
        _translate = QtCore.QCoreApplication.translate
        UpdateDialog.setWindowTitle(_translate("UpdateDialog", "Update"))
        self.cancelButton.setText(_translate("UpdateDialog", "Cancel"))
        self.updateButton.setText(_translate("UpdateDialog", "Update"))
        self.label.setText(_translate(
            "UpdateDialog", "2 + 2 = 5"))

        self.label3.setText(_translate(
            "UpdateDialog", "No connection to Github."))
        font = Fonts.Choose_Fonts(self, False, 9, "Arial")
        self.label3.setFont(font)
        string1 = (_translate("UpdateDialog", "Current Version: "))
        string2 = (_translate("UpdateDialog", "New Version: "))
        string3 = (_translate("UpdateDialog", "No Update available."))
        string4 = (_translate(
            "UpdateDialog", "Do you want to Update\nthis Program?"))

        self.label2.setText(
            string1 + version + "\n"
            "\n"
            + string2 + Ui_MainWindow.versionnew + "\n"
            "\n"
            + string4)

        self.label4.setText(string1 + version + "\n"
                            "\n"
                            + string2 + Ui_MainWindow.versionnew + "\n"
                            "\n"
                            + string3)

        self.label4.setFont(font)

        self.label2.setFont(font)

        if Ui_MainWindow.serverconnection is False:
            self.updateButton.setEnabled(False)
            self.label2.hide()
            self.label4.hide()
            self.label3.show()
        else:
            if Ui_MainWindow.update_avail is True:
                self.updateButton.setEnabled(True)
                self.label2.show()
                self.label4.hide()
                self.label3.hide()
            else:
                self.updateButton.setEnabled(False)
                self.label2.hide()
                self.label4.show()
                self.label3.hide()


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
