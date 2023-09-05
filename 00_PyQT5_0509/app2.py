from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import QSize, Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MyApp")
        self.button_is_checked = True

        button = QPushButton("Push me")
        button.setCheckable(True)  # кнопка будет посылать сигналы
        #button.clicked.connect(self.button_pressed)  связываем нажатие на кнопку с методом класса
        button.toggled.connect(self.button_toggled)
        button.setChecked(self.button_is_checked)

        # можно выставить границы расширения окна приложения
        self.setMaximumSize(QSize(1280, 720))
        self.setMinimumSize(QSize(640, 320))
        # setFixedSize() - фиксирует размер окна приложения, изменять размер больше нельзя
        # setMinimumSize()  - можно установить минимальный размер для окна (меньше не сможет быть)
        # setMaximumSize()  - установить максимальный размер для окна (больше не может быть)

        button.setMaximumSize(QSize(200, 100))
        # установим кнопку по центру
        self.setCentralWidget(button)

    def button_pressed(self):
        print('clicked!')

    def button_toggled(self, check):
        self.button_is_checked = check
        print(self.button_is_checked)


app = QApplication(sys.argv)  # чтобы работали аргументы из командной строки
window = MainWindow()
window.show()  # окно приложения по умолчанию закрыто

app.exec()  # запуск цикла событий

# чтобы ее запустить, нужно в терминале ввести python3 [название файла].py
