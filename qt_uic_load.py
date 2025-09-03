#! /usr/bin/env python3
# coding=utf-8

from PyQt5 import uic, QtWidgets, QtCore
import sys
import os


def openFile(widget):
    """
    Placeholder for opening a file.
    """
    print(QtCore.QCoreApplication.translate("Form", "Opening File..."))
    widget.titleLineEdit.setText("title")
    widget.artistLineEdit.setText("artist")
    widget.albumLineEdit.setText("album")
    widget.yearLineEdit.setText("year")


def main():
    """
    Main function to run the application.
    """
    app = QtWidgets.QApplication(sys.argv)

    # Load translations
    translator = QtCore.QTranslator()
    translator.load(os.path.join("lang", "language_" + QtCore.QLocale.system().name()))
    app.installTranslator(translator)

    # Load the UI from the .ui file
    ui = uic.loadUi(os.path.join("ui", "id3_editor.ui"))
    ui.closeButton.clicked.connect(ui.close)
    ui.openButton.clicked.connect(lambda: openFile(ui))
    ui.saveButton.clicked.connect(lambda: print("saved..."))
    ui.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()