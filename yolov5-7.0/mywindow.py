# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mywindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(974, 476)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.input = QLabel(self.centralwidget)
        self.input.setObjectName(u"input")
        self.input.setGeometry(QRect(30, 20, 341, 261))
        self.input.setScaledContents(True)
        self.input.setAlignment(Qt.AlignCenter)
        self.ouput = QLabel(self.centralwidget)
        self.ouput.setObjectName(u"ouput")
        self.ouput.setGeometry(QRect(410, 20, 361, 261))
        self.ouput.setScaledContents(True)
        self.ouput.setAlignment(Qt.AlignCenter)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(380, 10, 21, 281))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.det_img = QPushButton(self.centralwidget)
        self.det_img.setObjectName(u"det_img")
        self.det_img.setGeometry(QRect(40, 320, 281, 51))
        self.det_video = QPushButton(self.centralwidget)
        self.det_video.setObjectName(u"det_video")
        self.det_video.setGeometry(QRect(470, 320, 281, 51))
        self.det_img_2 = QPushButton(self.centralwidget)
        self.det_img_2.setObjectName(u"det_img_2")
        self.det_img_2.setGeometry(QRect(70, 380, 231, 41))
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(823, 0, 20, 451))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.check_rep = QCheckBox(self.centralwidget)
        self.check_rep.setObjectName(u"check_rep")
        self.check_rep.setGeometry(QRect(850, 20, 111, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.input.setText(QCoreApplication.translate("MainWindow", u"\u539f\u59cb\u8f93\u5165", None))
        self.ouput.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b\u7ed3\u679c", None))
        self.det_img.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u68c0\u6d4b", None))
        self.det_video.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u68c0\u6d4b", None))
        self.det_img_2.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u68c0\u6d4b(\u5feb\u901f\uff09", None))
        self.check_rep.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210\u62a5\u544a", None))
    # retranslateUi

