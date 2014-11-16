#! /usr/bin/env python3
# coding=utf-8
import os
import sys
from PyQt5 import QtWidgets, QtCore
from ui.id3_editor_ui import Ui_Form


class myUi_Form(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.openButton.clicked.connect(self.openFile)
        self.closeButton.clicked.connect(self.close)
        self.saveButton.clicked.connect(lambda: print("saved..."))


    def openFile(self):
        print(QtCore.QCoreApplication.translate("Form", "Opening File..."))
        self.titleLineEdit.setText("title")
        self.artistLineEdit.setText("artist")
        self.albumLineEdit.setText("album")
        self.yearLineEdit.setText("year")


def main():
    app = QtWidgets.QApplication(sys.argv)

    translator = QtCore.QTranslator()
    translator.load(os.path.join("lang", "language_" + QtCore.QLocale.system().name()))
    app.installTranslator(translator)

    ui = myUi_Form()
    ui.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
