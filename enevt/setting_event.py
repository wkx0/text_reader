from PyQt5 import QtCore
from PyQt5.QtCore import QMetaObject, pyqtSignal
from PyQt5.QtWidgets import QFileDialog, QColorDialog, QMessageBox

from ui.setting_ui import SettingUI


class SettingEvent(SettingUI):
    _signal: pyqtSignal = pyqtSignal(str, str, str, str, str)
    _close_signal: pyqtSignal = pyqtSignal(str)
    _find_signal: pyqtSignal = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self.load_config()
        QMetaObject.connectSlotsByName(self)  # 自动自动连接信号和槽

    @QtCore.pyqtSlot()
    def on_select_file_button_clicked(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "Text Files (*.txt)",
                                                   options=options)
        if file_path:
            self.file_Edit.setText(file_path)

    @QtCore.pyqtSlot()
    def on_select_font_color_button_clicked(self):
        color_dialog = QColorDialog(self)
        color_dialog.setLocale(QtCore.QLocale(QtCore.QLocale.German, QtCore.QLocale.Germany))
        color = color_dialog.getColor()

        if color.isValid():
            color_name = color.name()
            self.font_color_Edit.setText(color_name)

    @QtCore.pyqtSlot()
    def on_select_background_color_button_clicked(self):
        color_dialog = QColorDialog(self)
        color_dialog.setLocale(QtCore.QLocale(QtCore.QLocale.German, QtCore.QLocale.Germany))
        color = color_dialog.getColor()

        if color.isValid():
            color_name = color.name()
            self.background_color_Edit.setText(color_name)

    @QtCore.pyqtSlot()
    def on_save_button_clicked(self):
        file = self.file_Edit.text()
        line_height = self.line_height_Edit.text()
        font_size = self.font_size_Edit.text()
        font_color = self.font_color_Edit.text()
        background_color = self.background_color_Edit.text()

        self.conf.set_text_path(file)
        self.conf.set_line_height(line_height)
        self.conf.set_font_size(font_size)
        self.conf.set_font_color(font_color)
        self.conf.set_background_color(background_color)
        # 通知主窗口更新UI
        self._signal.emit(file, line_height, font_size, font_color, background_color)
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText("保存成功！")
        msg.setWindowTitle("成功")
        msg.show()

    @QtCore.pyqtSlot()
    def on_close_button_clicked(self):
        self.close()
        self._close_signal.emit("close")

    @QtCore.pyqtSlot()
    def on_find_next_button_clicked(self):
        find_text = self.find_Edit.text()
        self._find_signal.emit(find_text, "next")

    @QtCore.pyqtSlot()
    def on_find_up_button_clicked(self):
        find_text = self.find_Edit.text()
        self._find_signal.emit(find_text, "reverse")

    def load_config(self):
        if self.conf.text_path != "":
            self.file_Edit.setText(self.conf.text_path)
        if self.conf.line_height != "":
            self.line_height_Edit.setValue(int(self.conf.line_height))
        if self.conf.font_size != "":
            self.font_size_Edit.setValue(int(self.conf.font_size))
        if self.conf.font_color != "":
            self.font_color_Edit.setText(self.conf.font_color)
        if self.conf.background_color != "":
            self.background_color_Edit.setText(self.conf.background_color)

    def closeEvent(self, event):
        event.ignore()  # 阻止默认关闭行为
        self.hide()  # 隐藏子窗口而不关闭

    @property
    def signal(self):
        return self._signal

    @property
    def close_signal(self):
        return self._close_signal

    @property
    def find_signal(self):
        return self._find_signal