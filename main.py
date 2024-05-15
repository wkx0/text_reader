import sys

from PyQt5 import QtCore

from PyQt5.QtWidgets import QApplication

from windows.text_window import TextWin


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = TextWin()
    # w = SettingWin()
    w.show()
    qt_translator = QtCore.QTranslator()
    qt_translator.load("qt_" + QtCore.QLocale.system().name(),
                       QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.TranslationsPath))
    app.installTranslator(qt_translator)

    sys.exit(app.exec())
