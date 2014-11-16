# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/id3_editor.ui'
#
# Created: Sun Nov 16 22:09:13 2014
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(377, 213)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.titleLabel = QtWidgets.QLabel(Form)
        self.titleLabel.setObjectName("titleLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.titleLabel)
        self.titleLineEdit = QtWidgets.QLineEdit(Form)
        self.titleLineEdit.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.titleLineEdit.setObjectName("titleLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.titleLineEdit)
        self.artistLabel = QtWidgets.QLabel(Form)
        self.artistLabel.setObjectName("artistLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.artistLabel)
        self.artistLineEdit = QtWidgets.QLineEdit(Form)
        self.artistLineEdit.setObjectName("artistLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.artistLineEdit)
        self.albumLabel = QtWidgets.QLabel(Form)
        self.albumLabel.setObjectName("albumLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.albumLabel)
        self.albumLineEdit = QtWidgets.QLineEdit(Form)
        self.albumLineEdit.setObjectName("albumLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.albumLineEdit)
        self.yearLabel = QtWidgets.QLabel(Form)
        self.yearLabel.setObjectName("yearLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.yearLabel)
        self.yearLineEdit = QtWidgets.QLineEdit(Form)
        self.yearLineEdit.setObjectName("yearLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.yearLineEdit)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(4, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.openButton = QtWidgets.QPushButton(Form)
        self.openButton.setObjectName("openButton")
        self.horizontalLayout.addWidget(self.openButton)
        self.saveButton = QtWidgets.QPushButton(Form)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)
        self.closeButton = QtWidgets.QPushButton(Form)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Super Ham"))
        self.titleLabel.setText(_translate("Form", "Title:"))
        self.artistLabel.setText(_translate("Form", "Artist:"))
        self.albumLabel.setText(_translate("Form", "Album:"))
        self.yearLabel.setText(_translate("Form", "Year:"))
        self.openButton.setText(_translate("Form", "Open"))
        self.saveButton.setText(_translate("Form", "Save"))
        self.closeButton.setText(_translate("Form", "Close"))

