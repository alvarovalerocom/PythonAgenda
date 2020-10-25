# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'agenda.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Downloads/iconfinder_User_group_132235.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(30, 660, 80, 23))
        self.saveButton.setObjectName("saveButton")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(120, 660, 80, 23))
        self.deleteButton.setObjectName("deleteButton")
        self.donateButton = QtWidgets.QPushButton(self.centralwidget)
        self.donateButton.setGeometry(QtCore.QRect(450, 660, 80, 23))
        self.donateButton.setObjectName("donateButton")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(580, 0, 421, 156))
        self.calendarWidget.setObjectName("calendarWidget")
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(30, 170, 57, 15))
        self.nameLabel.setObjectName("nameLabel")
        self.emailLabel = QtWidgets.QLabel(self.centralwidget)
        self.emailLabel.setGeometry(QtCore.QRect(30, 370, 57, 15))
        self.emailLabel.setObjectName("emailLabel")
        self.adressLabel = QtWidgets.QLabel(self.centralwidget)
        self.adressLabel.setGeometry(QtCore.QRect(30, 320, 57, 15))
        self.adressLabel.setObjectName("adressLabel")
        self.phoneLabel = QtWidgets.QLabel(self.centralwidget)
        self.phoneLabel.setGeometry(QtCore.QRect(30, 270, 57, 15))
        self.phoneLabel.setObjectName("phoneLabel")
        self.surnameLabel = QtWidgets.QLabel(self.centralwidget)
        self.surnameLabel.setGeometry(QtCore.QRect(30, 220, 57, 15))
        self.surnameLabel.setObjectName("surnameLabel")
        self.nameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameLineEdit.setGeometry(QtCore.QRect(100, 170, 421, 23))
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.surnameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.surnameLineEdit.setGeometry(QtCore.QRect(100, 220, 421, 23))
        self.surnameLineEdit.setObjectName("surnameLineEdit")
        self.phoneLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.phoneLineEdit.setGeometry(QtCore.QRect(100, 260, 421, 23))
        self.phoneLineEdit.setObjectName("phoneLineEdit")
        self.adressLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.adressLineEdit.setGeometry(QtCore.QRect(100, 310, 421, 23))
        self.adressLineEdit.setObjectName("adressLineEdit")
        self.emailLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.emailLineEdit.setGeometry(QtCore.QRect(100, 360, 421, 23))
        self.emailLineEdit.setObjectName("emailLineEdit")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(100, 410, 431, 211))
        self.textEdit.setObjectName("textEdit")
        self.notesLabel = QtWidgets.QLabel(self.centralwidget)
        self.notesLabel.setGeometry(QtCore.QRect(30, 420, 57, 15))
        self.notesLabel.setObjectName("notesLabel")
        self.notesTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.notesTextEdit.setGeometry(QtCore.QRect(550, 170, 441, 451))
        self.notesTextEdit.setObjectName("notesTextEdit")
        self.saveNotesButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveNotesButton.setGeometry(QtCore.QRect(910, 650, 80, 23))
        self.saveNotesButton.setObjectName("saveNotesButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.saveButton.setText(_translate("MainWindow", "Save"))
        self.deleteButton.setText(_translate("MainWindow", "Delete"))
        self.donateButton.setText(_translate("MainWindow", "Donate"))
        self.nameLabel.setText(_translate("MainWindow", "Name"))
        self.emailLabel.setText(_translate("MainWindow", "Email"))
        self.adressLabel.setText(_translate("MainWindow", "Address"))
        self.phoneLabel.setText(_translate("MainWindow", "Phone"))
        self.surnameLabel.setText(_translate("MainWindow", "Surname"))
        self.notesLabel.setText(_translate("MainWindow", "Notes"))
        self.saveNotesButton.setText(_translate("MainWindow", "Save notes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
