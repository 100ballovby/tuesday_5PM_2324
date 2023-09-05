from PyQt6.QtWidgets import QApplication, QWidget
import sys


app = QApplication(sys.argv)  # чтобы работали аргументы из командной строки
window = QWidget()
window.show()  # окно приложения по умолчанию закрыто

app.exec()  # запуск цикла событий

# чтобы ее запустить, нужно в терминале ввести python3 [название файла].py
