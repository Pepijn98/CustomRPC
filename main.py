from PyQt5 import QtWidgets
import design
import sys
import pyrpc
import re
import time
import asyncio
import json

dark_theme: str = "background-color: rgb(46, 52, 54);\ncolor: rgb(238, 238, 236);"
# TODO : Light theme option for future update
# light_theme: str = "background-color: rgb(238, 238, 236);\ncolor: rgb(46, 52, 54);"


class RPCApp(QtWidgets.QMainWindow, design.Ui_CustomRPC):
    def __init__(self, parent=None):
        super(RPCApp, self).__init__(parent)
        self.setupUi(self)
        self.alert = QtWidgets.QMessageBox()
        self.rpc = None
        self.app_settings = None
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
            QtWidgets.QMessageBox.Information,
            'Do you want to save the filled in data for next time?',
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QmessageBox.Reset,
            def_btn=QtWidgets.QMessageBox.Yes,
            def_btn=QtWidgets.QmessageBox.Reset,
            return_val=True
        )

        if result == QtWidgets.QMessageBox.Yes:
            self.save_data()
        else if result == Qtwidgets.QMessageBox.Reset:
            self.save_data(reset=True)
        else:
            self.rpc.close()

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
                QtWidgets.QMessageBox.Warning,
                'State needs to be more than 2 characters long',
                QtWidgets.QMessageBox.Close,
                title='Warning'
            )
        elif len(details) < 2:
            return self.show_alert(
                QtWidgets.QMessageBox.Warning,
                'Details needs to be more than 2 characters long',
                QtWidgets.QMessageBox.Close,
                title='Warning'
            )

        if appid == '':
            if c_limage != '' or c_simage != '':
                return self.show_alert(
                    QtWidgets.QMessageBox.Warning,
                    'Custom data can only be set when a custom app id is given',
                    QtWidgets.QMessageBox.Close,
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
                QtWidgets.QMessageBox.Critical,
                'Details is a required field, please fill it in with some text',
                QtWidgets.QMessageBox.Ok,
                title='Critical'
            )
        elif state == '':
            return self.show_alert(
                QtWidgets.QMessageBox.Critical,
                'State is a required field, please fill it in with some text',
                QtWidgets.QMessageBox.Ok,
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
            self.rpc = pyrpc.DiscordRPC(appid, True)
            try:
                self.rpc.start()
                self.rpc.send_rich_presence(payload)
            except Exception as e:
                self.show_alert(
                    QtWidgets.QMessageBox.Critical,
                    type(e).__name__,
                    QtWidgets.QMessageBox.Close,
                    info=str(e),
                    title='Critical'
                )
        else:
            self.show_alert(
                QtWidgets.QMessageBox.Critical,
                '"{}" is not a valid app id'.format(appid),
                QtWidgets.QMessageBox.Close,
                title='Critical'
            )

    def close_rpc(self):
        if self.rpc is not None:
            self.rpc.close()

    def show_alert(self,
                   icon: QtWidgets.QMessageBox.Icon,
                   text: str,
                   btns: QtWidgets.QMessageBox.StandardButton,
                   info: str = '',
                   title: str = '',
                   def_btn: QtWidgets.QMessageBox.StandardButton = None,
                   return_val: bool = False):
        self.alert.setIcon(icon)
        self.alert.setText(text)
        self.alert.setInformativeText(info)
        self.alert.setWindowTitle(title)
        self.alert.setStandardButtons(btns)
        self.alert.setDefaultButton(def_btn)
        self.alert.setStyleSheet(dark_theme)

        # TODO : For future update to support light and dark theme
        # if self.app_settings is not None:
        #     if self.app_settings['darktheme']:
        #         self.alert.setStyleSheet(dark_theme)
        #     else:
        #         self.alert.setStyleSheet(light_theme)

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
                'settings': {'darktheme': False},
                'data': {
                    'details': '',
                    'state': '',
                    'largeImageText': '',
                    'smallImageText': '',
                    'timer': False,
                    'appid': '',
                    'largeImageName': '',
                    'smallImageName': ''
                }
            }
        else:
            if self.app_settings is not None:
                settings = self.app_settings
            else:
                settings = {'darktheme': False}
            data = {
                'settings': settings,
                'data': {
                    'details': self.details_tb.text(),
                    'state': self.state_tb.text(),
                    'largeImageText': self.largeimgtext_tb.text(),
                    'smallImageText': self.smallimgtext_tb.text(),
                    'timer': self.timer_cb.isChecked(),
                    'appid': self.appid_tb.text(),
                    'largeImageName': self.largeimgname_tb.text(),
                    'smallImageName': self.smallimgname_tb.text()
                }
            }
        with open('customrpc-data.json', 'w') as outfile:
            json.dump(data, outfile)

    def open_data(self):
        try:
            with open('customrpc-data.json', 'r') as file:
                json_data = json.load(file)
                data = json_data['data']
                self.app_settings = json_data['settings']
                self.details_tb.setText(data['details'])
                self.state_tb.setText(data['state'])
                self.largeimgtext_tb.setText(data['largeImageText'])
                self.smallimgtext_tb.setText(data['smallImageText'])
                self.timer_cb.setChecked(data['timer'])
                self.appid_tb.setText(data['appid'])
                self.largeimgname_tb.setText(data['largeImageName'])
                self.smallimgname_tb.setText(data['smallImageName'])

                # TODO : For future update to support light and dark theme
                # if self.app_settings is not None:
                #     if self.app_settings['darktheme']:
                #         self.setStyleSheet(dark_theme)
                #         self.centralwidget.setStyleSheet(dark_theme)
                #     else:
                #         self.setStyleSheet(light_theme)
                #         self.centralwidget.setStyleSheet(light_theme)
        except FileNotFoundError:
            pass
        except Exception as e:
            self.show_alert(
                QtWidgets.QMessageBox.Critical,
                type(e).__name__,
                QtWidgets.QMessageBox.Close,
                info=str(e),
                title='Critical'
            )


def main():
    app = QtWidgets.QApplication(sys.argv)
    form_main = RPCApp()
    form_main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
