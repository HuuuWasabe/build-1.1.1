# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'junkntradeZnoewS.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu

import icons_rc
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(942, 528)
        MainWindow.setStyleSheet(u"* {\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"#header {\n"
"	background-color:  rgb(45, 60, 81);\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"#centralwidget {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(44, 0, 		    		134, 255), stop:1 rgba(28, 124, 31, 255));\n"
"	border-radius: 20px;\n"
"	\n"
"}\n"
"\n"
"#sideMenu {\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"}\n"
"\n"
"QLabel {\n"
"	color: #fff\n"
"}\n"
"QPushButton {\n"
"	padding: 10px;\n"
"	background-color: rgb(85, 85, 127);\n"
"	border-radius: 5px;\n"
"	color: #fff;\n"
"}\n"
"\n"
"#mainMenu {\n"
"	background-color: #1f232a;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(30, 215, 96);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 60))
        self.header.setMaximumSize(QSize(16777215, 70))
        self.header.setFrameShape(QFrame.Box)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 50))
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(20, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setMinimumSize(QSize(0, 30))
        self.menuBtn.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.menuBtn.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.menuBtn)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignLeft)

        self.frame_3 = QFrame(self.header)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.appname = QLabel(self.frame_3)
        self.appname.setObjectName(u"appname")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setWeight(75)
        self.appname.setFont(font1)
        self.appname.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.appname)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.header, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sideMenu = QCustomSlideMenu(self.frame_2)
        self.sideMenu.setObjectName(u"sideMenu")
        sizePolicy.setHeightForWidth(self.sideMenu.sizePolicy().hasHeightForWidth())
        self.sideMenu.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.sideMenu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 0, 15, 15)
        self.appIcon = QFrame(self.sideMenu)
        self.appIcon.setObjectName(u"appIcon")
        self.appIcon.setFrameShape(QFrame.StyledPanel)
        self.appIcon.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.appIcon)

        self.frame_4 = QFrame(self.sideMenu)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(150, 0))
        self.frame_4.setMaximumSize(QSize(150, 16777215))
        font2 = QFont()
        font2.setKerning(True)
        self.frame_4.setFont(font2)
        self.frame_4.setFrameShape(QFrame.Box)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 15, 0, 0)
        self.profileBtn = QPushButton(self.frame_4)
        self.profileBtn.setObjectName(u"profileBtn")
        self.profileBtn.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.profileBtn.setIcon(icon1)
        self.profileBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.profileBtn)

        self.redeemBtn = QPushButton(self.frame_4)
        self.redeemBtn.setObjectName(u"redeemBtn")
        self.redeemBtn.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/shopping-bag.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.redeemBtn.setIcon(icon2)
        self.redeemBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.redeemBtn)

        self.junkBtn = QPushButton(self.frame_4)
        self.junkBtn.setObjectName(u"junkBtn")
        self.junkBtn.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.junkBtn.setIcon(icon3)
        self.junkBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.junkBtn)

        self.rewardBtn = QPushButton(self.frame_4)
        self.rewardBtn.setObjectName(u"rewardBtn")
        self.rewardBtn.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.rewardBtn.setIcon(icon4)
        self.rewardBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.rewardBtn)


        self.verticalLayout_2.addWidget(self.frame_4, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout.addWidget(self.sideMenu)

        self.mainMenu = QFrame(self.frame_2)
        self.mainMenu.setObjectName(u"mainMenu")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.mainMenu.sizePolicy().hasHeightForWidth())
        self.mainMenu.setSizePolicy(sizePolicy2)
        self.verticalLayout_5 = QVBoxLayout(self.mainMenu)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.mainMenu)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.profile = QWidget()
        self.profile.setObjectName(u"profile")
        self.verticalLayout_6 = QVBoxLayout(self.profile)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_5 = QFrame(self.profile)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 30))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.profileTitle = QLabel(self.frame_5)
        self.profileTitle.setObjectName(u"profileTitle")
        self.profileTitle.setFont(font1)

        self.horizontalLayout_6.addWidget(self.profileTitle, 0, Qt.AlignHCenter)


        self.verticalLayout_6.addWidget(self.frame_5)

        self.widget_5 = QWidget(self.profile)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_7 = QVBoxLayout(self.widget_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.details = QFrame(self.widget_5)
        self.details.setObjectName(u"details")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.details.sizePolicy().hasHeightForWidth())
        self.details.setSizePolicy(sizePolicy3)
        self.details.setFrameShape(QFrame.StyledPanel)
        self.details.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.details)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.columnA = QFrame(self.details)
        self.columnA.setObjectName(u"columnA")
        self.columnA.setMaximumSize(QSize(150, 16777215))
        self.columnA.setFrameShape(QFrame.StyledPanel)
        self.columnA.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.columnA)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, -1, 9, -1)
        self.label = QLabel(self.columnA)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout_9.addWidget(self.label)

        self.label_2 = QLabel(self.columnA)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_9.addWidget(self.label_2)

        self.label_6 = QLabel(self.columnA)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalLayout_9.addWidget(self.label_6)

        self.label_8 = QLabel(self.columnA)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.verticalLayout_9.addWidget(self.label_8)

        self.label_7 = QLabel(self.columnA)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.verticalLayout_9.addWidget(self.label_7)

        self.label_9 = QLabel(self.columnA)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.verticalLayout_9.addWidget(self.label_9)


        self.horizontalLayout_4.addWidget(self.columnA, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.details)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"QLabel {\n"
"	background-color: #b8b8b8;\n"
"	border-radius: 10px;\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.memID = QLabel(self.frame_7)
        self.memID.setObjectName(u"memID")
        self.memID.setFont(font)

        self.verticalLayout_8.addWidget(self.memID)

        self.usrName = QLabel(self.frame_7)
        self.usrName.setObjectName(u"usrName")
        self.usrName.setFont(font)

        self.verticalLayout_8.addWidget(self.usrName)

        self.fName = QLabel(self.frame_7)
        self.fName.setObjectName(u"fName")
        self.fName.setFont(font)

        self.verticalLayout_8.addWidget(self.fName)

        self.lName = QLabel(self.frame_7)
        self.lName.setObjectName(u"lName")
        self.lName.setFont(font)

        self.verticalLayout_8.addWidget(self.lName)

        self.contNum = QLabel(self.frame_7)
        self.contNum.setObjectName(u"contNum")
        self.contNum.setFont(font)

        self.verticalLayout_8.addWidget(self.contNum)

        self.emailAdd = QLabel(self.frame_7)
        self.emailAdd.setObjectName(u"emailAdd")
        self.emailAdd.setFont(font)

        self.verticalLayout_8.addWidget(self.emailAdd)


        self.horizontalLayout_4.addWidget(self.frame_7)


        self.verticalLayout_7.addWidget(self.details)

        self.logout = QFrame(self.widget_5)
        self.logout.setObjectName(u"logout")
        self.logout.setMaximumSize(QSize(16777215, 55))
        self.logout.setFrameShape(QFrame.StyledPanel)
        self.logout.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.logout)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.logOut = QPushButton(self.logout)
        self.logOut.setObjectName(u"logOut")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.logOut.setIcon(icon5)

        self.horizontalLayout_5.addWidget(self.logOut)

        self.updBtn = QPushButton(self.logout)
        self.updBtn.setObjectName(u"updBtn")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.updBtn.setIcon(icon6)

        self.horizontalLayout_5.addWidget(self.updBtn)


        self.verticalLayout_7.addWidget(self.logout, 0, Qt.AlignHCenter)


        self.verticalLayout_6.addWidget(self.widget_5)

        self.stackedWidget.addWidget(self.profile)
        self.redeem = QWidget()
        self.redeem.setObjectName(u"redeem")
        self.label_3 = QLabel(self.redeem)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(180, 90, 251, 111))
        font3 = QFont()
        font3.setPointSize(30)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_3.setFont(font3)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.redeem)
        self.shops = QWidget()
        self.shops.setObjectName(u"shops")
        self.label_4 = QLabel(self.shops)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(190, 90, 331, 111))
        self.label_4.setFont(font3)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.shops)
        self.rsystem = QWidget()
        self.rsystem.setObjectName(u"rsystem")
        self.verticalLayout_10 = QVBoxLayout(self.rsystem)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_6 = QFrame(self.rsystem)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(260, 150, 271, 71))
        self.label_5.setFont(font3)

        self.verticalLayout_10.addWidget(self.frame_6)

        self.stackedWidget.addWidget(self.rsystem)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.mainMenu)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuBtn.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.appname.setText(QCoreApplication.translate("MainWindow", u"Junk N' Trade", None))
        self.profileBtn.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.redeemBtn.setText(QCoreApplication.translate("MainWindow", u"Redeem", None))
        self.junkBtn.setText(QCoreApplication.translate("MainWindow", u"Junk Shops", None))
        self.rewardBtn.setText(QCoreApplication.translate("MainWindow", u"Reward System", None))
        self.profileTitle.setText(QCoreApplication.translate("MainWindow", u"PROFILE", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Member ID:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Username:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"First Name:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Last name:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Contact No.:", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Email Address:", None))
        self.memID.setText("")
        self.usrName.setText("")
        self.fName.setText("")
        self.lName.setText("")
        self.contNum.setText("")
        self.emailAdd.setText("")
        self.logOut.setText(QCoreApplication.translate("MainWindow", u"LOG OUT", None))
        self.updBtn.setText(QCoreApplication.translate("MainWindow", u"UPDATE PROFILE", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"REDEEM", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"JUNK SHOPS", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"REWARDS", None))
    # retranslateUi

