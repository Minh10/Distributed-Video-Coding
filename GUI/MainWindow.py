# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(870, 625)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 241, 101))
        self.groupBox.setObjectName("groupBox")
        self.Button_camera1 = QtWidgets.QPushButton(self.groupBox)
        self.Button_camera1.setGeometry(QtCore.QRect(10, 20, 221, 31))
        self.Button_camera1.setObjectName("Button_camera1")
        self.Button_camera2 = QtWidgets.QPushButton(self.groupBox)
        self.Button_camera2.setGeometry(QtCore.QRect(10, 60, 221, 31))
        self.Button_camera2.setObjectName("Button_camera2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 120, 241, 111))
        self.groupBox_2.setObjectName("groupBox_2")
        self.Label_savepath = QtWidgets.QLabel(self.groupBox_2)
        self.Label_savepath.setGeometry(QtCore.QRect(10, 70, 141, 21))
        self.Label_savepath.setText("")
        self.Label_savepath.setObjectName("Label_savepath")
        self.Edit_filename = QtWidgets.QLineEdit(self.groupBox_2)
        self.Edit_filename.setGeometry(QtCore.QRect(10, 30, 141, 31))
        self.Edit_filename.setText("")
        self.Edit_filename.setObjectName("Edit_filename")
        self.Button_filename = QtWidgets.QPushButton(self.groupBox_2)
        self.Button_filename.setGeometry(QtCore.QRect(160, 30, 71, 31))
        self.Button_filename.setObjectName("Button_filename")
        self.Button_savepath = QtWidgets.QPushButton(self.groupBox_2)
        self.Button_savepath.setGeometry(QtCore.QRect(160, 70, 71, 28))
        self.Button_savepath.setObjectName("Button_savepath")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 240, 231, 121))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.Button_recording = QtWidgets.QPushButton(self.tab)
        self.Button_recording.setGeometry(QtCore.QRect(10, 10, 101, 31))
        self.Button_recording.setObjectName("Button_recording")
        self.Button_endrecording = QtWidgets.QPushButton(self.tab)
        self.Button_endrecording.setGeometry(QtCore.QRect(120, 10, 101, 31))
        self.Button_endrecording.setText("")
        self.Button_endrecording.setObjectName("Button_endrecording")
        self.Label_mrecordingtime = QtWidgets.QLabel(self.tab)
        self.Label_mrecordingtime.setGeometry(QtCore.QRect(10, 50, 211, 21))
        self.Label_mrecordingtime.setText("")
        self.Label_mrecordingtime.setObjectName("Label_mrecordingtime")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.Button_trigger = QtWidgets.QPushButton(self.tab_2)
        self.Button_trigger.setGeometry(QtCore.QRect(10, 10, 101, 31))
        self.Button_trigger.setObjectName("Button_trigger")
        self.Button_canceltrigger = QtWidgets.QPushButton(self.tab_2)
        self.Button_canceltrigger.setGeometry(QtCore.QRect(120, 10, 101, 31))
        self.Button_canceltrigger.setObjectName("Button_canceltrigger")
        self.Label_trecordingtime = QtWidgets.QLabel(self.tab_2)
        self.Label_trecordingtime.setGeometry(QtCore.QRect(10, 50, 211, 21))
        self.Label_trecordingtime.setText("")
        self.Label_trecordingtime.setObjectName("Label_trecordingtime")
        self.tabWidget.addTab(self.tab_2, "")
        self.video1 = QtWidgets.QLabel(self.centralwidget)
        self.video1.setGeometry(QtCore.QRect(260, 10, 591, 561))
        self.video1.setFrameShape(QtWidgets.QFrame.Box)
        self.video1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.video1.setLineWidth(7)
        self.video1.setText("")
        self.video1.setObjectName("video1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1480, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuWindows = QtWidgets.QMenu(self.menubar)
        self.menuWindows.setObjectName("menuWindows")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuWindows.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "My cameras"))
        self.groupBox.setTitle(_translate("MainWindow", "Devices"))
        self.Button_camera1.setText(_translate("MainWindow", "Camera 1"))
        self.Button_camera2.setText(_translate("MainWindow", "Camera 2"))
        self.groupBox_2.setTitle(_translate("MainWindow", "File recordings"))
        self.Button_filename.setText(_translate("MainWindow", "Set name"))
        self.Button_savepath.setText(_translate("MainWindow", "Set path"))
        self.Button_recording.setText(_translate("MainWindow", "Person"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "AI"))
        self.Button_trigger.setText(_translate("MainWindow", "JPEG"))
        self.Button_canceltrigger.setText(_translate("MainWindow", "H265"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Comp"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuWindows.setTitle(_translate("MainWindow", "Windows"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
