#! /usr/bin/env python3
# coding=utf-8
import os
import sys
from PyQt5 import QtWidgets, QtCore
from ui.id3_editor_ui import Ui_Form


class myUi_Form(QtWidgets.QWidget, Ui_Form):
    """
    Main application window.

    This class inherits from QWidget and the UI definition from Ui_Form.
    It sets up the UI and connects signals to slots.
    """
    def __init__(self):
        """
        Initializes the UI and connects signals to slots.
        """
        super().__init__()
        self.setupUi(self)
        self.openButton.clicked.connect(self.openFile)
        self.closeButton.clicked.connect(self.close)
        self.saveButton.clicked.connect(lambda: print("saved..."))


    def openFile(self):
        """
        Placeholder for opening a file.
        """
        print(QtCore.QCoreApplication.translate("Form", "Opening File..."))
        self.titleLineEdit.setText("title")
        self.artistLineEdit.setText("artist")
        self.albumLineEdit.setText("album")
        self.yearLineEdit.setText("year")


def main():
    """
    Main function to run the application.
    """
    app = QtWidgets.QApplication(sys.argv)

    # Load translations
    translator = QtCore.QTranslator()
    translator.load(os.path.join("lang", "language_" + QtCore.QLocale.system().name()))
    app.installTranslator(translator)

    # Create and show the main window
    ui = myUi_Form()
    ui.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
