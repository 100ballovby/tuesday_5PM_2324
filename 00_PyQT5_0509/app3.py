from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import QSize, Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MyApp")
        self.button_is_checked = True

        self.button = QPushButton("Push me")
        """Сохраняем ссылку на кнопку в self, чтобы 
        в дальнейшем была возможность получить к ней доступ в слоте"""
        self.button.setCheckable(True)  # кнопка будет посылать сигналы
        self.button.released.connect(self.button_released)
        """сигнал released срабатывает  в тот момент, когда кнопку
        "отпустили", но состояние кнопки при этом в сигнале не отправляется 
        и не сохраняется в слоте. Вместо этого состояние кнопки вызывается
        в методе isChecked()"""
        self.button.setChecked(self.button_is_checked)

        # можно выставить границы расширения окна приложения
        self.setMaximumSize(QSize(1280, 720))
        self.setMinimumSize(QSize(640, 320))
        # setFixedSize() - фиксирует размер окна приложения, изменять размер больше нельзя
        # setMinimumSize()  - можно установить минимальный размер для окна (меньше не сможет быть)
        # setMaximumSize()  - установить максимальный размер для окна (больше не может быть)

        self.button.setMaximumSize(QSize(200, 100))
        # установим кнопку по центру
        self.setCentralWidget(self.button)
    def button_released(self):
        self.button_is_checked = self.button.isChecked()
        print(self.button_is_checked)




app = QApplication(sys.argv)  # чтобы работали аргументы из командной строки
window = MainWindow()
window.show()  # окно приложения по умолчанию закрыто

app.exec()  # запуск цикла событий

# чтобы ее запустить, нужно в терминале ввести python3 [название файла].py
