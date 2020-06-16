from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import random

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1295, 715)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1295, 715))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(5, 1, 1281, 551))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton_6 = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(400, 560, 221, 71))
        self.pushButton_6.setGeometry(QtCore.QRect(140, 560, 221, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.pushButton.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(660, 560, 221, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.pushButton_2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(910, 580, 161, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(1090, 580, 171, 31))
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(200, 20, 821, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 151, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(9, 0, 108))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(9, 0, 108))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_4.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(20, 160, 151, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(90, 115, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 115, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_5.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(20, 230, 151, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(9, 0, 108))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(9, 0, 108))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_6.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(20, 300, 151, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(90, 115, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 115, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_7.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 90, 821, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(200, 160, 821, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(200, 230, 821, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(200, 300, 821, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(640, 360, 381, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.pushButton_3.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setGeometry(QtCore.QRect(20, 380, 401, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(153, 153, 153))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(153, 153, 153))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_13.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_8 = QtWidgets.QLabel(self.tab_3)
        self.label_8.setGeometry(QtCore.QRect(20, 20, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(200, 20, 821, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_4.setGeometry(QtCore.QRect(640, 70, 381, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.pushButton_4.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_14 = QtWidgets.QLabel(self.tab_3)
        self.label_14.setGeometry(QtCore.QRect(20, 90, 401, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(153, 153, 153))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(153, 153, 153))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_14.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_9 = QtWidgets.QLabel(self.tab_4)
        self.label_9.setGeometry(QtCore.QRect(20, 20, 1261, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(9, 0, 108))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(9, 0, 108))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_9.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.tab_4)
        self.label_10.setGeometry(QtCore.QRect(20, 70, 1261, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(9, 0, 108))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(9, 0, 108))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_10.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.tab_4)
        self.label_11.setGeometry(QtCore.QRect(20, 140, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_7.setGeometry(QtCore.QRect(230, 140, 371, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_5.setGeometry(QtCore.QRect(620, 140, 171, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(9, 0, 108))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(9, 0, 108))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.pushButton_5.setPalette(palette)
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_12 = QtWidgets.QLabel(self.tab_4)
        self.label_12.setGeometry(QtCore.QRect(680, 190, 101, 31))
        self.label_12.setObjectName("label_12")
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1295, 21))
        self.menubar.setObjectName("menubar")
        self.menuLearn_Word = QtWidgets.QMenu(self.menubar)
        self.menuLearn_Word.setObjectName("menuLearn_Word")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCreated_by_AliTunahanGuner = QtWidgets.QAction(MainWindow)
        self.actionCreated_by_AliTunahanGuner.setObjectName("actionCreated_by_AliTunahanGuner")

        self.veritabani()

        sorgu2 = "SELECT * FROM game where english = ?"
        self.cursor.execute(sorgu2, ("start",))
        acaba = self.cursor.fetchall()
        if len(acaba) > 0:
            pass
        else:
            sorgu = "INSERT INTO game VALUES(?,?,?,?,?)"

            self.cursor.execute(sorgu, (
                "start", "to begin doing something.", "He started smoking when he was eighteen.",
                "If a business, organization, etc starts, it begins to exist, and if you start it, you make it begin to exist.",
                "She started her own computer business."))
            self.baglanti.commit()
        self.ilksoru1 = "to begin doing something."
        self.ilksoru2 = "If a business, organization, etc starts, it begins to exist, and if you start it, you make it begin to exist."
        self.ilkcevap = "start"
        self.pushButton_5.clicked.connect(self.tryyourself)

        self.tabWidget.setCurrentIndex(0)
        sorgu = "SELECT * FROM game"
        self.cursor.execute(sorgu)
        deger = self.cursor.fetchall()
        self.bos0 = " "
        self.bos1 = " "
        self.bos2 = " "
        self.bos3 = " "
        self.bos4 = " "
        sorgu3 = "SELECT * FROM spot"
        self.cursor.execute(sorgu3)
        spot = self.cursor.fetchall()

        self.maa = spot[0][1]

        self.k = self.maa
        self.m = 0

        self.bos0 = deger[self.maa][self.m]
        self.kelime = len(deger)
        self.pushButton_6.clicked.connect(self.trigger3)
        self.pushButton.clicked.connect(self.trigger)#okey
        self.pushButton_2.clicked.connect(self.trigger2)#okey
        self.pushButton_3.clicked.connect(self.addword) #okey
        self.pushButton_4.clicked.connect(self.deleteword) #okey


        self.menuLearn_Word.addAction(self.actionCreated_by_AliTunahanGuner)
        self.menubar.addAction(self.menuLearn_Word.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def trigger3(self):
        sorgu = "SELECT * FROM game"
        self.cursor.execute(sorgu)
        deger = self.cursor.fetchall()
        self.k -= 1
        if self.k == -1:
            self.k = len(deger)-1
        self.m = 0
        self.bos1 = " "
        self.bos2 = deger[self.k][0]
        self.bos3 = " "
        self.bos4 = " "
        renk1 = "#e20000"
        renk2 = "#e20000"
        renk3 = "#e20000"
        renk4 = "#e20000"
        boyut = "75pt"
        self.label.setText("Which Word: " + "{}".format(self.k + 1))
        self.savespot(self.k)
        self.textBrowser.setText("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:"+boyut+"; color:"+renk1+"; vertical-align:sub;\">"+self.bos1+"</span></p></body></html>\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:"+boyut+"; color:"+renk2+"; vertical-align:sub;\">"+self.bos2+"</span></p></body></html>\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:"+boyut+"; color:"+renk3+"; vertical-align:sub;\">"+self.bos3+"</span></p></body></html>\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:"+boyut+"; color:"+renk4+"; vertical-align:sub;\">"+self.bos4+"</span></p></body></html>\n")


    def yesil(self):
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_12.setPalette(palette)
    def kirmizi(self):
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_12.setPalette(palette)

    def tryyourself(self):
        if self.ilksoru1 == "to begin doing something.":
            if self.lineEdit_7.text() == "start":
                self.yesil()
                self.label_12.setText("True !")
                #self.label_14.setText("")
                sorgu = "SELECT * FROM game"
                self.cursor.execute(sorgu)
                liste = self.cursor.fetchall()
                m = len(liste)
                a = random.randrange(0, m)
                self.ilksoru1 = liste[a][1]
                self.ilksoru2 = liste[a][3]
                self.ilkcevap = liste[a][0]
                self.label_9.setText("1. " +self.ilksoru1)
                self.label_10.setText("2. " +self.ilksoru2)
                self.lineEdit_7.clear()
            else:
                self.kirmizi()
                self.label_12.setText("False !")
                #self.label_13.setText("")
                self.lineEdit_7.clear()
        elif (self.ilkcevap==self.lineEdit_7.text()):
            #self.label_14.setText("")
            self.yesil()
            self.label_12.setText("True !")
            sorgu = "SELECT * FROM game"
            self.cursor.execute(sorgu)
            liste = self.cursor.fetchall()
            m = len(liste)
            a = random.randrange(0, m)
            self.ilksoru1 = liste[a][1]
            self.ilksoru2 = liste[a][3]
            self.ilkcevap = liste[a][0]
            self.label_9.setText("1. " +self.ilksoru1)
            self.label_10.setText("2. " +self.ilksoru2)
            self.lineEdit_7.clear()
        else:
            self.kirmizi()
            self.label_12.setText("False !")
            #self.label_13.setText("")
            self.lineEdit_7.clear()

    def savespot(self,x):
        sorgu = "Update spot SET deger =? WHERE savespot=?"
        self.cursor.execute(sorgu,(x,"savespot"))
        self.baglanti.commit()
    def veritabani(self):
        self.baglanti = sqlite3.connect("dictionary_game.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "CREATE TABLE IF NOT EXISTS game(english TEXT,meaning TEXT,meaning2 TEXT,meaning3 TEXT,meaning4 TEXT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()
        sorgu2 = "CREATE TABLE IF NOT EXISTS spot(savespot TEXT, deger INT)"
        self.cursor.execute(sorgu2)
        self.baglanti.commit()
        sorgu4 = "SELECT * FROM spot"
        self.cursor.execute(sorgu4)
        a = self.cursor.fetchall()

        if len(a)>0:
            pass
        else:
            sorgu3 = "INSERT INTO spot VALUES(?,?)"
            self.cursor.execute(sorgu3,("savespot",0))

    def addword(self): #okey
        sorgu1 = "SELECT * FROM game where english = ?"
        self.cursor.execute(sorgu1, (self.lineEdit.text(),))
        acaba = self.cursor.fetchall()
        if len(acaba) > 0:
            self.label_13.setText("Word already exist!")
        else:
            a = self.lineEdit.text()
            a = a.strip(" ")
            sorgu2 = "INSERT INTO game VALUES(?,?,?,?,?)"
            self.cursor.execute(sorgu2,(a,self.lineEdit_2.text(),self.lineEdit_3.text(),self.lineEdit_4.text(),self.lineEdit_5.text()))
            self.baglanti.commit()
            self.label_13.setText("Adding successful!")
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit_4.clear()
            self.lineEdit_5.clear()



            sorgu3 = "SELECT * FROM game"
            self.cursor.execute(sorgu3)
            deger = self.cursor.fetchall()
            self.label_2.setText("Word Counter: "+"{}".format(len(deger)))

    def deleteword(self): #tamam
        sorgu = "DELETE FROM game where english=?"

        sorgu2 = "SELECT * FROM game where english = ?"
        self.cursor.execute(sorgu2,(self.lineEdit_6.text(),))
        acaba = self.cursor.fetchall()
        if len(acaba) > 0:
            if self.lineEdit_6.text()=="start":
                self.label_14.setText("Cannot delete!")
            else:
                self.cursor.execute(sorgu, (self.lineEdit_6.text(),))
                self.baglanti.commit()
                self.label_14.setText("Deleting successful!")
                self.lineEdit_6.clear()
                sorgu3 = "SELECT * FROM game"
                self.cursor.execute(sorgu3)
                deger = self.cursor.fetchall()
                self.label_2.setText("Word Counter: " + "{}".format(len(deger)))
                self.k = len(deger) - 2

                sorgu = "Update spot SET deger =? WHERE savespot=?"
                self.cursor.execute(sorgu, (0, "savespot"))
                self.baglanti.commit()
        else:

            self.label_14.setText("There is no such word in database!")

    def trigger(self): #tamam
        sorgu = "SELECT * FROM game"
        self.cursor.execute(sorgu)
        deger = self.cursor.fetchall()
        self.m +=1
        if self.m%2 == 0:
            self.bos1 = " "
            self.bos2 = deger[self.k][0]
            self.bos3 = " "
            self.bos4 = " "
            renk1 = "#e20000"
            renk2 = "#e20000"
            renk3 = "#e20000"
            renk4 = "#e20000"
            boyut1 = "75pt"
            boyut2 = "75pt"
        else:
            if deger[self.k][1] == "" and deger[self.k][3]== "":
                self.bos1 = deger[self.k][1]
                self.bos3 = deger[self.k][3]
            elif deger[self.k][1] != "" and deger[self.k][3] == "":
                self.bos1 = "1.  " + deger[self.k][1]
                self.bos3 = deger[self.k][3]
            elif deger[self.k][1] == "" and deger[self.k][3] != "":
                self.bos1 = deger[self.k][1]
                self.bos3 = "2.  " + deger[self.k][3]
            elif deger[self.k][1] != "" and deger[self.k][3] != "":
                self.bos1 = "1.  " + deger[self.k][1]
                self.bos3 = "2.  " + deger[self.k][3]

            self.bos2 = deger[self.k][2]
            self.bos4 = deger[self.k][4]
            renk1 = "#09006c"
            renk2 = "#5a73ff"
            renk3 = "#09006c"
            renk4 = "#5a73ff"
            boyut1 = "50pt"
            boyut2 = "45pt"

        self.textBrowser.setText("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:"+boyut1+"; color:"+renk1+"; vertical-align:sub;\">"+self.bos1+"</span></p></body></html>\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:"+boyut2+"; color:"+renk2+"; vertical-align:sub;\">"+self.bos2+"</span></p></body></html>\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:"+boyut1+"; color:"+renk3+"; vertical-align:sub;\">"+self.bos3+"</span></p></body></html>\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:"+boyut2+"; color:"+renk4+"; vertical-align:sub;\">"+self.bos4+"</span></p></body></html>\n")

    def trigger2(self): #tamam
        sorgu = "SELECT * FROM game"
        self.cursor.execute(sorgu)
        deger = self.cursor.fetchall()
        self.k += 1
        if self.k == len(deger):
            self.k = 0
        self.m = 0
        self.bos1 = " "
        self.bos2 = deger[self.k][0]
        self.bos3 = " "
        self.bos4 = " "
        renk1 = "#e20000"
        renk2 = "#e20000"
        renk3 = "#e20000"
        renk4 = "#e20000"
        boyut = "75pt"
        self.label.setText("Which Word: "+"{}".format(self.k+1))
        self.savespot(self.k)
        self.textBrowser.setText("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:"+boyut+"; color:"+renk1+"; vertical-align:sub;\">"+self.bos1+"</span></p></body></html>\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:"+boyut+"; color:"+renk2+"; vertical-align:sub;\">"+self.bos2+"</span></p></body></html>\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:"+boyut+"; color:"+renk3+"; vertical-align:sub;\">"+self.bos3+"</span></p></body></html>\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:"+boyut+"; color:"+renk4+"; vertical-align:sub;\">"+self.bos4+"</span></p></body></html>\n")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Learn English Vocabulary"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:75pt; color:#e20000; vertical-align:sub;\">"+self.bos1+"</span></p></body></html>\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:75pt; color:#e20000; vertical-align:sub;\">"+self.bos0+"</span></p></body></html>\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:75pt; color:#e20000; vertical-align:sub;\">"+self.bos3+"</span></p></body></html>\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:75pt; color:#e20000; vertical-align:sub;\">"+self.bos4+"</span></p></body></html>\n"))
        self.pushButton.setText(_translate("MainWindow", "DEFINITION"))
        self.pushButton_6.setText(_translate("MainWindow", "BACK"))
        self.pushButton_2.setText(_translate("MainWindow", "SKIP"))
        self.label.setText(_translate("MainWindow", "Which Word: "+"{}".format(self.k+1)))
        self.label_2.setText(_translate("MainWindow", "Word Counter: "+str(self.kelime)))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Learn Word"))
        self.label_3.setText(_translate("MainWindow", "English Word: "))
        self.label_4.setText(_translate("MainWindow", "Meaning 1:"))
        self.label_5.setText(_translate("MainWindow", "Sentence 1:"))
        self.label_6.setText(_translate("MainWindow", "Meaning 2:"))
        self.label_7.setText(_translate("MainWindow", "Sentence 2:"))
        self.pushButton_3.setText(_translate("MainWindow", "ADD WORD"))
        self.label_13.setText(_translate("MainWindow", ""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Add Word"))
        self.label_8.setText(_translate("MainWindow", "English Word: "))
        self.pushButton_4.setText(_translate("MainWindow", "DELETE WORD"))
        self.label_14.setText(_translate("MainWindow", ""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Delete Word"))
        self.label_9.setText(_translate("MainWindow", "1. {}".format(self.ilksoru1)))
        self.label_10.setText(_translate("MainWindow", "2. {}".format(self.ilksoru2)))
        self.label_11.setText(_translate("MainWindow", "What is this word?"))
        self.pushButton_5.setText(_translate("MainWindow", "TRY"))
        self.label_12.setText(_translate("MainWindow", ""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Try Yourself"))
        self.menuLearn_Word.setTitle(_translate("MainWindow", "About"))
        self.actionCreated_by_AliTunahanGuner.setText(_translate("MainWindow", "created by AliTunahanGuner"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
