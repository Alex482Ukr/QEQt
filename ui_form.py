# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextBrowser, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.setEnabled(True)
        Widget.resize(705, 503)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setMinimumSize(QSize(705, 503))
        Widget.setMaximumSize(QSize(705, 503))
        self.lineEdit_a = QLineEdit(Widget)
        self.lineEdit_a.setObjectName(u"lineEdit_a")
        self.lineEdit_a.setGeometry(QRect(220, 20, 71, 61))
        font = QFont()
        font.setPointSize(28)
        self.lineEdit_a.setFont(font)
        self.lineEdit_b = QLineEdit(Widget)
        self.lineEdit_b.setObjectName(u"lineEdit_b")
        self.lineEdit_b.setGeometry(QRect(320, 20, 71, 61))
        self.lineEdit_b.setFont(font)
        self.lineEdit_c = QLineEdit(Widget)
        self.lineEdit_c.setObjectName(u"lineEdit_c")
        self.lineEdit_c.setGeometry(QRect(420, 20, 71, 61))
        self.lineEdit_c.setFont(font)
        self.label_d = QLabel(Widget)
        self.label_d.setObjectName(u"label_d")
        self.label_d.setEnabled(False)
        self.label_d.setGeometry(QRect(100, 170, 61, 61))
        self.label_d.setFont(font)
        self.textBrowser_d = QTextBrowser(Widget)
        self.textBrowser_d.setObjectName(u"textBrowser_d")
        self.textBrowser_d.setEnabled(False)
        self.textBrowser_d.setGeometry(QRect(170, 170, 81, 61))
        self.textBrowser_d.setFont(font)
        self.textBrowser_x1 = QTextBrowser(Widget)
        self.textBrowser_x1.setObjectName(u"textBrowser_x1")
        self.textBrowser_x1.setEnabled(False)
        self.textBrowser_x1.setGeometry(QRect(510, 170, 81, 61))
        self.textBrowser_x1.setFont(font)
        self.label_x1 = QLabel(Widget)
        self.label_x1.setObjectName(u"label_x1")
        self.label_x1.setEnabled(False)
        self.label_x1.setGeometry(QRect(440, 170, 61, 61))
        self.label_x1.setFont(font)
        self.label_x2 = QLabel(Widget)
        self.label_x2.setObjectName(u"label_x2")
        self.label_x2.setEnabled(False)
        self.label_x2.setGeometry(QRect(440, 250, 61, 61))
        self.label_x2.setFont(font)
        self.textBrowser_x2 = QTextBrowser(Widget)
        self.textBrowser_x2.setObjectName(u"textBrowser_x2")
        self.textBrowser_x2.setEnabled(False)
        self.textBrowser_x2.setGeometry(QRect(510, 250, 81, 61))
        self.textBrowser_x2.setFont(font)
        self.textBrowser_dsqrt = QTextBrowser(Widget)
        self.textBrowser_dsqrt.setObjectName(u"textBrowser_dsqrt")
        self.textBrowser_dsqrt.setEnabled(False)
        self.textBrowser_dsqrt.setGeometry(QRect(170, 250, 81, 61))
        self.textBrowser_dsqrt.setFont(font)
        self.label_dsqrt = QLabel(Widget)
        self.label_dsqrt.setObjectName(u"label_dsqrt")
        self.label_dsqrt.setEnabled(False)
        self.label_dsqrt.setGeometry(QRect(60, 250, 101, 61))
        self.label_dsqrt.setFont(font)
        self.label_d0 = QLabel(Widget)
        self.label_d0.setObjectName(u"label_d0")
        self.label_d0.setEnabled(True)
        self.label_d0.setGeometry(QRect(260, 170, 61, 61))
        self.label_d0.setFont(font)
        self.textBrowser_multipliers = QTextBrowser(Widget)
        self.textBrowser_multipliers.setObjectName(u"textBrowser_multipliers")
        self.textBrowser_multipliers.setEnabled(False)
        self.textBrowser_multipliers.setGeometry(QRect(130, 370, 461, 61))
        self.textBrowser_multipliers.setFont(font)
        self.pushButton_calc = QPushButton(Widget)
        self.pushButton_calc.setObjectName(u"pushButton_calc")
        self.pushButton_calc.setGeometry(QRect(300, 110, 111, 41))
        self.checkBox_frc = QCheckBox(Widget)
        self.checkBox_frc.setObjectName(u"checkBox_frc")
        self.checkBox_frc.setGeometry(QRect(430, 110, 91, 41))
        font1 = QFont()
        font1.setPointSize(12)
        self.checkBox_frc.setFont(font1)
        self.lineEdit_var = QLineEdit(Widget)
        self.lineEdit_var.setObjectName(u"lineEdit_var")
        self.lineEdit_var.setGeometry(QRect(240, 110, 41, 41))
        font2 = QFont()
        font2.setPointSize(18)
        self.lineEdit_var.setFont(font2)
        self.lineEdit_var.setAlignment(Qt.AlignCenter)
        self.label_var = QLabel(Widget)
        self.label_var.setObjectName(u"label_var")
        self.label_var.setGeometry(QRect(160, 100, 81, 61))
        self.label_var.setFont(font1)
        self.label_var.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.lineEdit_a.setText("")
        self.lineEdit_a.setPlaceholderText(QCoreApplication.translate("Widget", u"a", None))
        self.lineEdit_b.setText("")
        self.lineEdit_b.setPlaceholderText(QCoreApplication.translate("Widget", u"b", None))
        self.lineEdit_c.setText("")
        self.lineEdit_c.setPlaceholderText(QCoreApplication.translate("Widget", u"c", None))
        self.label_d.setText(QCoreApplication.translate("Widget", u"D =", None))
        self.textBrowser_d.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:28pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textBrowser_d.setPlaceholderText("")
        self.textBrowser_x1.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:28pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_x1.setText(QCoreApplication.translate("Widget", u"x\u2081 =", None))
        self.label_x2.setText(QCoreApplication.translate("Widget", u"x\u2082 =", None))
        self.textBrowser_x2.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:28pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textBrowser_dsqrt.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:28pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_dsqrt.setText(QCoreApplication.translate("Widget", u"\u221aD =", None))
        self.label_d0.setText("")
        self.textBrowser_multipliers.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:28pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textBrowser_multipliers.setPlaceholderText(QCoreApplication.translate("Widget", u"Multipliers", None))
        self.pushButton_calc.setText(QCoreApplication.translate("Widget", u"Calculate", None))
        self.checkBox_frc.setText(QCoreApplication.translate("Widget", u"Fractions", None))
        self.lineEdit_var.setText(QCoreApplication.translate("Widget", u"x", None))
        self.lineEdit_var.setPlaceholderText(QCoreApplication.translate("Widget", u"x", None))
        self.label_var.setText(QCoreApplication.translate("Widget", u"Variable", None))
    # retranslateUi

