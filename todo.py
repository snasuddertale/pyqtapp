#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from PyQt5.QtWidgets import QApplication, QWidget
from gui import Ui_Widget


class Zadania(QWidget, Ui_Widget):

    def __init__(self, parent=None):
        super(Zadania, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    okno = Zadania()
    okno.show()
    okno.move(350, 200)
    sys.exit(app.exec_())
