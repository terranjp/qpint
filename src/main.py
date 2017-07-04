import sys
from PyQt5.QtWidgets import QApplication
from widgets.unitConverterWidget import UnitConverterWidget


def handleException(exc_type, exc_value, exc_traceback):
    import traceback
    traceback.print_exception(exc_type, exc_value, exc_traceback)

sys.excepthook = handleException


def main():
    app = QApplication(sys.argv)
    window = UnitConverterWidget()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()