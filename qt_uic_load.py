#! /usr/bin/env python3
# coding=utf-8

from PyQt5 import uic, QtWidgets, QtCore
import sys
import os


def openFile(widget):
    print(QtCore.QCoreApplication.translate("Form", "Opening File..."))
    widget.titleLineEdit.setText("title")
    widget.artistLineEdit.setText("artist")
    widget.albumLineEdit.setText("album")
    widget.yearLineEdit.setText("year")


def main():
    app = QtWidgets.QApplication(sys.argv)

    translator = QtCore.QTranslator()
    translator.load(os.path.join("lang", "language_" + QtCore.QLocale.system().name()))
    app.installTranslator(translator)

    ui = uic.loadUi(os.path.join("ui", "id3_editor.ui"))
    ui.closeButton.clicked.connect(ui.close)
    ui.openButton.clicked.connect(lambda: openFile(ui))
    ui.saveButton.clicked.connect(lambda: print("saved..."))
    ui.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()