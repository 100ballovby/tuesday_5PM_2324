from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MyApp")
        self.button_is_checked = True

        self.button = QPushButton("Push me")
        self.setCentralWidget(self.button)

    def button_pressed(self):
        self.button.setText('You already clicked me')
        self.button.setEnabled(False)

        self.setWindowTitle('My oneshot app')




app = QApplication(sys.argv)  # чтобы работали аргументы из командной строки
window = MainWindow()
window.show()  # окно приложения по умолчанию закрыто

app.exec()  # запуск цикла событий

# чтобы ее запустить, нужно в терминале ввести python3 [название файла].py
