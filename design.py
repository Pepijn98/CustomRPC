# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_CustomRPC(object):
    def setupUi(self, CustomRPC):
        CustomRPC.setObjectName(_fromUtf8("CustomRPC"))
        CustomRPC.resize(521, 474)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../home/kurozero/Downloads/Wind.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CustomRPC.setWindowIcon(icon)
        CustomRPC.setWindowOpacity(1.0)
        self.centralwidget = QtGui.QWidget(CustomRPC)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.update_rpc_btn = QtGui.QPushButton(self.centralwidget)
        self.update_rpc_btn.setEnabled(False)
        self.update_rpc_btn.setGeometry(QtCore.QRect(150, 400, 171, 29))
        self.update_rpc_btn.setObjectName(_fromUtf8("update_rpc_btn"))
        self.details_tb = QtGui.QLineEdit(self.centralwidget)
        self.details_tb.setGeometry(QtCore.QRect(20, 50, 481, 29))
        self.details_tb.setToolTip(_fromUtf8(""))
        self.details_tb.setMaxLength(127)
        self.details_tb.setObjectName(_fromUtf8("details_tb"))
        self.state_tb = QtGui.QLineEdit(self.centralwidget)
        self.state_tb.setGeometry(QtCore.QRect(20, 90, 481, 29))
        self.state_tb.setToolTip(_fromUtf8(""))
        self.state_tb.setMaxLength(127)
        self.state_tb.setObjectName(_fromUtf8("state_tb"))
        self.appid_tb = QtGui.QLineEdit(self.centralwidget)
        self.appid_tb.setGeometry(QtCore.QRect(20, 280, 481, 29))
        self.appid_tb.setToolTip(_fromUtf8(""))
        self.appid_tb.setMaxLength(18)
        self.appid_tb.setObjectName(_fromUtf8("appid_tb"))
        self.id_secret_lbl = QtGui.QLabel(self.centralwidget)
        self.id_secret_lbl.setGeometry(QtCore.QRect(20, 250, 131, 17))
        self.id_secret_lbl.setObjectName(_fromUtf8("id_secret_lbl"))
        self.rpc_data_lbl = QtGui.QLabel(self.centralwidget)
        self.rpc_data_lbl.setGeometry(QtCore.QRect(20, 20, 141, 17))
        self.rpc_data_lbl.setObjectName(_fromUtf8("rpc_data_lbl"))
        self.largeimgname_tb = QtGui.QLineEdit(self.centralwidget)
        self.largeimgname_tb.setGeometry(QtCore.QRect(20, 320, 481, 29))
        self.largeimgname_tb.setMaxLength(31)
        self.largeimgname_tb.setObjectName(_fromUtf8("largeimgname_tb"))
        self.smallimgname_tb = QtGui.QLineEdit(self.centralwidget)
        self.smallimgname_tb.setGeometry(QtCore.QRect(20, 360, 481, 29))
        self.smallimgname_tb.setMaxLength(31)
        self.smallimgname_tb.setObjectName(_fromUtf8("smallimgname_tb"))
        self.largeimgtext_tb = QtGui.QLineEdit(self.centralwidget)
        self.largeimgtext_tb.setGeometry(QtCore.QRect(20, 130, 481, 29))
        self.largeimgtext_tb.setMaxLength(127)
        self.largeimgtext_tb.setObjectName(_fromUtf8("largeimgtext_tb"))
        self.smallimgtext_tb = QtGui.QLineEdit(self.centralwidget)
        self.smallimgtext_tb.setGeometry(QtCore.QRect(20, 170, 481, 29))
        self.smallimgtext_tb.setMaxLength(127)
        self.smallimgtext_tb.setObjectName(_fromUtf8("smallimgtext_tb"))
        self.timer_cb = QtGui.QCheckBox(self.centralwidget)
        self.timer_cb.setGeometry(QtCore.QRect(20, 210, 98, 22))
        self.timer_cb.setObjectName(_fromUtf8("timer_cb"))
        self.stop_rpc_btn = QtGui.QPushButton(self.centralwidget)
        self.stop_rpc_btn.setEnabled(False)
        self.stop_rpc_btn.setGeometry(QtCore.QRect(330, 400, 171, 29))
        self.stop_rpc_btn.setAutoDefault(False)
        self.stop_rpc_btn.setDefault(False)
        self.stop_rpc_btn.setFlat(False)
        self.stop_rpc_btn.setObjectName(_fromUtf8("stop_rpc_btn"))
        CustomRPC.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(CustomRPC)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 521, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        CustomRPC.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(CustomRPC)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        CustomRPC.setStatusBar(self.statusbar)

        self.retranslateUi(CustomRPC)
        QtCore.QMetaObject.connectSlotsByName(CustomRPC)

    def retranslateUi(self, CustomRPC):
        CustomRPC.setWindowTitle(_translate("CustomRPC", "Custom RPC", None))
        self.update_rpc_btn.setText(_translate("CustomRPC", "Update Rich Presence", None))
        self.details_tb.setPlaceholderText(_translate("CustomRPC", "details", None))
        self.state_tb.setPlaceholderText(_translate("CustomRPC", "state", None))
        self.appid_tb.setPlaceholderText(_translate("CustomRPC", "app id", None))
        self.id_secret_lbl.setText(_translate("CustomRPC", "Custom:", None))
        self.rpc_data_lbl.setText(_translate("CustomRPC", "Rich Presence data:", None))
        self.largeimgname_tb.setPlaceholderText(_translate("CustomRPC", "large image name", None))
        self.smallimgname_tb.setPlaceholderText(_translate("CustomRPC", "small image name", None))
        self.largeimgtext_tb.setPlaceholderText(_translate("CustomRPC", "large image text", None))
        self.smallimgtext_tb.setPlaceholderText(_translate("CustomRPC", "small image text", None))
        self.timer_cb.setText(_translate("CustomRPC", "Timer", None))
        self.stop_rpc_btn.setText(_translate("CustomRPC", "Stop Rich Presence", None))

