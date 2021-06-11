from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5 import QtGui
import sys

class interface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        self.boldFont = QtGui.QFont()
        self.boldFont.setBold(True)
        self.setGeometry(1200, 250, 600, 500)
        self.title = self.setWindowTitle("Whatsapp Bot interface")
        self.Layout_components()
        self.labels()
        self.input()
        self.button()
        self.setFont(QFont("Arial", 15))
        self.setWindowIcon(QIcon("Bot.png"))
        self.show()

    def Layout_components(self):
        self.exit_ = QAction(QIcon("Bot.png"), "Exit", self)
        self.stop_ = QAction(QIcon("Bot.png"), "Stop", self)
        self.start_ = QAction(QIcon("Bot.png"), "Start", self)
        self.exit_.triggered.connect(self.exit)
        self.stop_.triggered.connect(self.stop)
        self.start_.triggered.connect(self.start)

        menubar = self.menuBar()
        file = menubar.addMenu("Bot")
        file.addAction(self.exit_)
        file.addAction(self.stop_)
        file.addAction(self.start_)

    def labels(self):

        labelp1 = QLabel("picture", self)
        labelp1.setPixmap(QPixmap("Bot.png"))
        labelp1.setGeometry(340, 100, 210, 180)

        labelp2 = QLabel("picture1", self)
        labelp2.setPixmap(QPixmap("whatsapp_symbol.png"))
        labelp2.setScaledContents(True)
        labelp2.resize(80, 80)
        labelp2.setGeometry(50, 400, 80, 80)

        label1 = QLabel("description", self)
        label1.setGeometry(50, 40, 500, 50)
        label1.setText("Welcome to my Whatsappbot. Are you ready to fuck other people with endless spam up. Have fun!!!")
        label1.setFont(QFont("Arial", 14))
        label1.setStyleSheet("border : 2px solid black;")
        label1.setWordWrap(True)

        label2 = QLabel("adress", self)
        label2.setGeometry(50, 100, 150, 50)
        label2.setText("adressed to: ")

        label2 = QLabel("message", self)
        label2.setGeometry(50, 300, 150, 50)
        label2.setText("message: ")

        label2 = QLabel("amount", self)
        label2.setGeometry(50, 200, 200, 50)
        label2.setText("amount of messages: ")

        self.label_input = QLabel("counter", self)
        self.label_input.setGeometry(170, 260, 80, 20)
        self.label_input.setFont(QFont("Arial", 15))
        self.label_input.setAlignment(Qt.AlignCenter)
        self.label_input.setStyleSheet("border:2px solid black")


    def input(self):
        self.input_adressed = QLineEdit(self)
        self.input_adressed.setGeometry(50, 150, 150, 30)
        self.input_adressed.textChanged.connect(self.clicked_adressed)

        self.input_message = QLineEdit(self)
        self.input_message.setGeometry(50, 350, 150, 30)
        self.input_message.textChanged.connect(self.clicked_message)

        self.input_amount = QSlider(self)
        self.input_amount.setGeometry(50, 240, 100, 70)
        self.input_amount.setMaximum(1000)
        self.input_amount.valueChanged.connect(self.clicked_amount)

    def button(self):

        self.but_stop = QPushButton("Stop", self)
        self.but_stop.setGeometry(340, 360, 210, 50)
        self.but_stop.setFont(self.boldFont)
        self.but_stop.clicked.connect(self.stop)

        self.but_start = QPushButton("Start", self)
        self.but_start.setGeometry(340, 300, 210, 50)
        self.but_start.setFont(self.boldFont)
        self.but_start.clicked.connect(self.start)

        self.but_exit = QPushButton("Exit", self)
        self.but_exit.setGeometry(340, 420, 210, 50)
        self.but_exit.setFont(self.boldFont)
        self.but_exit.clicked.connect(self.exit)

    def clicked_amount(self):

        self.amount = self.input_amount.value()
        if self.amount >= 0:
            self.label_input.setText(f"{self.amount}")

    def clicked_adressed(self):

        print(self.input_adressed.text())

    def clicked_message(self):

        print(self.input_message.text())

    def stop(self):
        print("programm stopps ...")

    def exit(self):
        #print("programm exits ...")
        app.exit()
        sys.exit()

    def start(self):
        pop_up = QMessageBox(self)
        pop_up.setWindowTitle("Start Bot")
        pop_up.setText("Do you really wanna start the spam ?!")
        pop_up.setIcon(QMessageBox.Question)
        pop_up.setStandardButtons(QMessageBox.Cancel | QMessageBox.No | QMessageBox.Yes)
        pop_up.setDefaultButton(QMessageBox.Yes)
        x = pop_up.exec_()

        if x == QMessageBox.Yes:
            print("programm starts ...")


app = QApplication(sys.argv)
y = interface()
sys.exit(app.exec_())