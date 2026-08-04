import sys

from PySide6.QtWidgets import QApplication

from ui import My_App




def main():

    app = QApplication(sys.argv)

    window = My_App()

    window.show()

    sys.exit(
        app.exec()
    )



if __name__ == "__main__":

    main()