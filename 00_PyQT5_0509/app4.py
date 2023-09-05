from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from random import choice

window_titles = [
    'My app',
    'Still my app',
    'This is surprising',
    'Something went wrong',
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.times_clicked = 0
        self.setWindowTitle("MyApp")
        self.button_is_checked = True

        self.windowTitleChanged.connect(self.title_changer)

        self.button = QPushButton("Push me")
        self.button.clicked.connect(self.button_pressed)  # связываю кнопку с методом
        self.setCentralWidget(self.button)

    def button_pressed(self):  # приемщик сигнала
        print('Clicked')
        new_window_title = choice(window_titles)
        print(f'Setting title: {new_window_title}.')
        self.setWindowTitle(new_window_title)

    def title_changer(self, title):
        if title == 'Something went wrong':
            self.button.setDisabled(True)




app = QApplication(sys.argv)  # чтобы работали аргументы из командной строки
window = MainWindow()
window.show()  # окно приложения по умолчанию закрыто

app.exec()  # запуск цикла событий

# чтобы ее запустить, нужно в терминале ввести python3 [название файла].py
