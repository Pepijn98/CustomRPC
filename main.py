from PyQt4 import QtGui  # , QtCore
import design
import sys
import pyrpc
import re


class RPCApp(QtGui.QMainWindow, design.Ui_CustomRPC):
    def __init__(self, parent=None):
        super(RPCApp, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Custom RPC')
        self.alert = QtGui.QMessageBox()
        self.rpc = None
        self.btn_timer = 0
        self.btn_timer_loop = True
        self.update_rpc_btn.clicked.connect(self.update_rpc)
        self.update_rpc_btn.setDisabled(True)
        self.state_tb.setMaxLength(127)
        self.state_tb.textChanged.connect(self.on_textchange)
        self.details_tb.setMaxLength(127)
        self.details_tb.textChanged.connect(self.on_textchange)
        self.largeimgname_tb.setMaxLength(31)
        self.largeimgname_tb.textChanged.connect(self.on_textchange)
        self.largeimgtext_tb.setMaxLength(127)
        self.largeimgtext_tb.textChanged.connect(self.on_textchange)
        self.smallimgname_tb.setMaxLength(31)
        self.smallimgname_tb.textChanged.connect(self.on_textchange)
        self.smallimgtext_tb.setMaxLength(127)
        self.smallimgtext_tb.textChanged.connect(self.on_textchange)

    def closeEvent(self, event):
        if self.rpc is not None:
            self.rpc.close()
        event.accept()

    def update_rpc(self):
        self.btn_timer_loop = True

        state = self.state_tb.text()
        details = self.details_tb.text()

        if len(state) < 2 or len(details) < 2:
            return self.show_alert(
                QtGui.QMessageBox.Warning,
                'Text too short',
                'Either state or details is too short, both need to be more than 2 characters long',
                'Critical',
                QtGui.QMessageBox.Ok
            )

        appid = self.appid_tb.text()
        c_limage = self.largeimgname_tb.text()
        c_ltext = self.largeimgtext_tb.text()
        c_simage = self.smallimgname_tb.text()
        c_stext = self.smallimgtext_tb.text()

        print(appid)

        if appid == '':
            if c_limage != '' or c_simage != '':
                return self.show_alert(
                    QtGui.QMessageBox.Warning,
                    'Custom data but no custom id',
                    'Custom data e.g. large image can only be set when a custom app id is given',
                    'Warning',
                    QtGui.QMessageBox.Ok
                )
            else:
                appid = '416357849153929226'
                c_limage = 'nobu'
                c_simage = ''

        payload = {
            'state': state,
            'details': details,
            'assets': {
                'large_text': c_ltext,
                'large_image': c_limage,
                'small_text': c_stext,
                'small_image': c_simage
            },
        }

        if details == '':
            return self.show_alert(
                QtGui.QMessageBox.Critical,
                'Forgot Required Field',
                'details is a required field, please fill it in with some text',
                'Critical',
                QtGui.QMessageBox.Ok
            )
        elif state == '':
            return self.show_alert(
                QtGui.QMessageBox.Critical,
                'Forgot Required Field',
                'state is a required field, please fill it in with some text',
                'Critical',
                QtGui.QMessageBox.Ok
            )

        if c_limage == '' and c_simage == '':
            del payload['assets']['large_image']
            del payload['assets']['small_image']
        elif c_limage == '':
            del payload['assets']['large_image']
        elif c_simage == '':
            del payload['assets']['small_image']

        if c_ltext == '' and c_stext == '':
            del payload['assets']['large_text']
            del payload['assets']['small_text']
        elif c_ltext == '':
            del payload['assets']['large_text']
        elif c_stext == '':
            del payload['assets']['small_text']

        if len(payload['assets']) == 0:
            del payload['assets']

        snowflake = re.compile(r'\d{17,18}')
        match = snowflake.match(appid)

        if match:
            self.rpc = pyrpc.DiscordRPC(appid, verbose=False)
            try:
                self.rpc.start()
                self.rpc.send_rich_presence(payload)
            except Exception as e:
                self.show_alert(
                    QtGui.QMessageBox.Critical,
                    type(e).__name__,
                    str(e),
                    'Critical',
                    QtGui.QMessageBox.Ok
                )
        else:
            self.show_alert(
                QtGui.QMessageBox.Critical,
                'Invalid App ID',
                '"{}" is not a valid id. An id is between the 17 and 18 digits long.'.format(appid),
                'Critical',
                QtGui.QMessageBox.Ok
            )

    def show_alert(self, icon: QtGui.QMessageBox, text: str, info: str, title: str, btns: int):
        self.alert.setIcon(icon)
        self.alert.setText(text)
        self.alert.setInformativeText(info)
        self.alert.setWindowTitle(title)
        self.alert.setStandardButtons(btns)
        self.alert.exec_()

    def on_textchange(self):
        if self.state_tb.text() == '' or self.details_tb.text() == '':
            self.update_rpc_btn.setDisabled(True)
        else:
            self.update_rpc_btn.setDisabled(False)


def main():
    app = QtGui.QApplication(sys.argv)
    form_main = RPCApp()
    form_main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
