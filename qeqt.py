# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

from quadratic_equations import *

from fractions import Fraction as Frc
from decimal import Decimal as Dec

VERSION = '1.0' 

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        def btn_click():
            self.ui.label_d.setEnabled(False)
            self.ui.textBrowser_d.setEnabled(False)
            self.ui.label_d0.setEnabled(False)
            self.ui.label_dsqrt.setEnabled(False)
            self.ui.textBrowser_dsqrt.setEnabled(False)
            self.ui.label_x1.setEnabled(False)
            self.ui.textBrowser_x1.setEnabled(False)
            self.ui.label_x2.setEnabled(False)
            self.ui.textBrowser_x2.setEnabled(False)
            self.ui.textBrowser_multipliers.setEnabled(False)
            self.ui.label_d0.setText('')

            a = int(self.ui.lineEdit_a.text())
            b = int(self.ui.lineEdit_b.text())
            c = int(self.ui.lineEdit_c.text())
            frac = self.ui.checkBox_frc.isChecked()
            var = self.ui.lineEdit_var.text() if self.ui.lineEdit_var.text() else 'x'

            self.ui.label_x1.setText(f'{var}₁ =')
            self.ui.label_x2.setText(f'{var}₂ =')

            ans = discriminant(a, b, c, func=(Frc if frac else Dec), full_output=True)

            self.ui.label_d.setEnabled(True)
            self.ui.textBrowser_d.setEnabled(True)
            self.ui.label_d0.setEnabled(True)

            self.ui.textBrowser_d.setText(str(ans['discr']))

            if ans['discr'] < 0:
                self.ui.label_d0.setText('< 0')
            else:
                self.ui.label_dsqrt.setEnabled(True)
                self.ui.textBrowser_dsqrt.setEnabled(True)
                self.ui.label_x1.setEnabled(True)
                self.ui.textBrowser_x1.setEnabled(True)

                self.ui.textBrowser_dsqrt.setText(str(ans['Dsqrt']).strip('.0'))

                if ans['discr'] > 0:
                    self.ui.label_d0.setText('> 0')
                    self.ui.label_x2.setEnabled(True)
                    self.ui.textBrowser_x2.setEnabled(True)

                    self.ui.textBrowser_x1.setText(str(ans['Xs'][0]).strip('.0'))
                    self.ui.textBrowser_x2.setText(str(ans['Xs'][1]).strip('.0'))
                else:
                    self.ui.label_d0.setText('= 0')
                    self.ui.textBrowser_x1.setText(str(ans['Xs'][0]).strip('.0'))
                
                self.ui.textBrowser_multipliers.setEnabled(True)
                self.ui.textBrowser_multipliers.setText(to_multipliers(a, ans['Xs'], var=var))

        self.ui.pushButton_calc.clicked.connect(btn_click)
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
