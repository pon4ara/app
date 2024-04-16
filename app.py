from PyQt6.QtWidgets import QMainWindow, QWidget, QApplication, QLabel, QLineEdit, QVBoxLayout, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        user_input = ""  # Переменная для хранения ввода пользователя

        self.setWindowTitle("My App")

        #button.setCheckable(True)

        layout = QVBoxLayout()
        layout.addWidget(QLineEdit())
        print(1)
        layout.addWidget(QPushButton("Save").clicked.connect(self.the_button_was_clicked))
        print(2)
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def the_button_was_clicked(self, text):
        user_input = text  # Сохраняем ввод пользователя в переменную
        self.label.setText(self.user_input)
        print("dffd")

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
