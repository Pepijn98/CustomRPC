from PyQt4 import QtGui
import design
import sys
import pyrpc
import re
import time
import asyncio
import json


class RPCApp(QtGui.QMainWindow, design.Ui_CustomRPC):
    def __init__(self, parent=None):
        super(RPCApp, self).__init__(parent)
        self.setupUi(self)
        self.alert = QtGui.QMessageBox()
        self.rpc = None
        self.appid_tb.setToolTip('Required field when using a custom app')
        self.state_tb.setToolTip('Required field')
        self.details_tb.setToolTip('Required field')
        self.update_rpc_btn.clicked.connect(self.update_rpc)
        self.stop_rpc_btn.clicked.connect(self.close_rpc)
        self.state_tb.textChanged.connect(self.on_textchange)
        self.details_tb.textChanged.connect(self.on_textchange)
        self.open_data()
        self.rpc_conn = asyncio.Task(self.check_rpc_conn())

    def closeEvent(self, event):
        result = self.show_alert(
            QtGui.QMessageBox.Information,
            'Do you want to save the filled in data for next time?',
            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
            def_btn=QtGui.QMessageBox.Yes,
            return_val=True
        )

        if result == QtGui.QMessageBox.Yes:
            self.save_data()
        else:
            self.save_data(reset=True)

        if self.rpc is not None:
            self.rpc.close()

        event.accept()

    def update_rpc(self):
        state = self.state_tb.text()
        details = self.details_tb.text()
        appid = self.appid_tb.text()
        c_limage = self.largeimgname_tb.text()
        c_ltext = self.largeimgtext_tb.text()
        c_simage = self.smallimgname_tb.text()
        c_stext = self.smallimgtext_tb.text()
        current_time = time.time()

        if len(state) < 2:
            return self.show_alert(
                QtGui.QMessageBox.Warning,
                'State needs to be more than 2 characters long',
                QtGui.QMessageBox.Close,
                title='Warning'
            )
        elif len(details) < 2:
            return self.show_alert(
                QtGui.QMessageBox.Warning,
                'Details needs to be more than 2 characters long',
                QtGui.QMessageBox.Close,
                title='Warning'
            )

        if appid == '':
            if c_limage != '' or c_simage != '':
                return self.show_alert(
                    QtGui.QMessageBox.Warning,
                    'Custom data can only be set when a custom app id is given',
                    QtGui.QMessageBox.Close,
                    title='Warning'
                )
            else:
                appid = '416357849153929226'
                c_limage = 'large_image'
                c_simage = ''

        payload = {
            'state': state,
            'details': details,
            'timestamps': {
                'start': int(current_time)
            },
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
                'Details is a required field, please fill it in with some text',
                QtGui.QMessageBox.Ok,
                title='Critical'
            )
        elif state == '':
            return self.show_alert(
                QtGui.QMessageBox.Critical,
                'State is a required field, please fill it in with some text',
                QtGui.QMessageBox.Ok,
                title='Critical'
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

        if not self.timer_cb.isChecked():
            del payload['timestamps']

        snowflake = re.compile(r'\d{17,18}')
        match = snowflake.match(appid)

        if match:
            self.rpc = pyrpc.DiscordRPC(appid)
            try:
                self.rpc.start()
                self.rpc.send_rich_presence(payload)
            except Exception as e:
                self.show_alert(
                    QtGui.QMessageBox.Critical,
                    type(e).__name__,
                    QtGui.QMessageBox.Close,
                    info=str(e),
                    title='Critical'
                )
        else:
            self.show_alert(
                QtGui.QMessageBox.Critical,
                '"{}" is not a valid app id'.format(appid),
                QtGui.QMessageBox.Close,
                title='Critical'
            )

    def close_rpc(self):
        if self.rpc is not None:
            self.rpc.close()

    def show_alert(self, icon: QtGui.QMessageBox, text: str, btns: int, info: str = '', title: str = '', def_btn: int = None, return_val: bool = False):
        self.alert.setIcon(icon)
        self.alert.setText(text)
        self.alert.setInformativeText(info)
        self.alert.setWindowTitle(title)
        self.alert.setStandardButtons(btns)
        self.alert.setDefaultButton(def_btn)
        if return_val:
            return self.alert.exec()
        else:
            self.alert.exec_()

    def on_textchange(self):
        if self.state_tb.text() == '' or self.details_tb.text() == '':
            self.update_rpc_btn.setDisabled(True)
        else:
            self.update_rpc_btn.setDisabled(False)

    async def check_rpc_conn(self):
        while True:
            if self.rpc is not None:
                self.stop_rpc_btn.setDisabled(False)
            else:
                self.stop_rpc_btn.setDisabled(True)
            await asyncio.sleep(10)

    def save_data(self, reset: bool = False):
        if reset:
            data = {
                'details': '',
                'state': '',
                'largeImageText': '',
                'smallImageText': '',
                'timer': False,
                'appid': '',
                'largeImageName': '',
                'smallImageName': ''
            }
        else:
            data = {
                'details': self.details_tb.text(),
                'state': self.state_tb.text(),
                'largeImageText': self.largeimgtext_tb.text(),
                'smallImageText': self.smallimgtext_tb.text(),
                'timer': self.timer_cb.isChecked(),
                'appid': self.appid_tb.text(),
                'largeImageName': self.largeimgname_tb.text(),
                'smallImageName': self.smallimgname_tb.text()
            }
        with open('customrpc-data.json', 'w') as outfile:
            json.dump(data, outfile)

    def open_data(self):
        try:
            with open('customrpc-data.json', 'r') as file:
                stuff = json.load(file)
                self.details_tb.setText(stuff['details'])
                self.state_tb.setText(stuff['state'])
                self.largeimgtext_tb.setText(stuff['largeImageText'])
                self.smallimgtext_tb.setText(stuff['smallImageText'])
                self.timer_cb.setChecked(stuff['timer'])
                self.appid_tb.setText(stuff['appid'])
                self.largeimgname_tb.setText(stuff['largeImageName'])
                self.smallimgname_tb.setText(stuff['smallImageName'])
        except FileNotFoundError:
            pass
        except Exception as e:
            self.show_alert(
                QtGui.QMessageBox.Critical,
                type(e).__name__,
                QtGui.QMessageBox.Close,
                info=str(e),
                title='Critical'
            )


def main():
    app = QtGui.QApplication(sys.argv)
    form_main = RPCApp()
    form_main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
