#!/usr/bin/env python3

from functools import cached_property
import sys
import threading
import time

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Worker:
    def start(self, amount, adressed, message):
        threading.Thread(target=self._execute, args=(amount, adressed, message), daemon=True).start()

    def _execute(self, amount, adressed, message):
        profile_path = "user-data-dir=/home/daniel/.config/google-chrome/storing1"

        options = webdriver.ChromeOptions()
        options.add_argument(profile_path)

        browser = webdriver.Chrome(executable_path="./chromedriver", options=options)
        browser.get("https://web.whatsapp.com")

        time.sleep(5)
        search = WebDriverWait(browser, 500).until(expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, "#side > div.SgIJV > div > label > div > div._2_1wd.copyable-text.selectable-text")))
        search.send_keys(adressed)
        time.sleep(1)
        search.send_keys(Keys.ENTER)
        send = WebDriverWait(browser, 500).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,
                                                                                                  "#main > footer > div.vR1LG._3wXwX.copyable-area > div._2A8P4._2A1WX > div > div._2_1wd.copyable-text.selectable-text")))

        try:
            for i in range(amount):
                send.send_keys(message)
                send.send_keys(Keys.ENTER)
        except:
            print('programm closes ...')

class interface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        self.boldFont = QFont()
        self.boldFont.setBold(True)
        self.setGeometry(200, 250, 650, 650)
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
        labelp1.setGeometry(400, 140, 250, 180)

        labelp2 = QLabel("picture1", self)
        labelp2.setPixmap(QPixmap("whatsapp_symbol.png"))
        labelp2.setScaledContents(True)
        labelp2.resize(80, 80)
        labelp2.setGeometry(50, 500, 80, 80)

        label1 = QLabel("description", self)
        label1.setGeometry(50, 60, 580, 60)
        label1.setText(
            "Welcome to my Whatsappbot. Are you ready to fuck other people with endless spam up. Have fun!!!")
        label1.setFont(QFont('Arial', 10))

        label1.setStyleSheet("border : 2px solid black;")
        label1.setWordWrap(True)

        label2 = QLabel("adress", self)
        label2.setGeometry(50, 140, 240, 60)
        label2.setText("adressed to: ")

        label2 = QLabel("message", self)
        label2.setGeometry(50, 360, 190, 60)
        label2.setText("message: ")

        label2 = QLabel("amount", self)
        label2.setGeometry(50, 240, 280, 60)
        label2.setText("amount of messages: ")

        self.label_input = QLabel("counter", self)
        self.label_input.setGeometry(170, 310, 130, 30)
        self.label_input.setFont(QFont("Arial", 13))
        self.label_input.setAlignment(Qt.AlignCenter)
        self.label_input.setStyleSheet("border:2px solid black")

    def input(self):
        self.input_adressed = QLineEdit(self)
        self.input_adressed.setGeometry(50, 190, 150, 30)

        self.input_message = QLineEdit(self)
        self.input_message.setGeometry(50, 410, 150, 30)

        self.input_amount = QSlider(self)
        self.input_amount.setGeometry(50, 290, 100, 70)
        self.input_amount.setMaximum(1000)

        self.input_amount.valueChanged.connect(self.label_input.setNum)

    def button(self):
        self.but_stop = QPushButton("Stop", self)
        self.but_stop.setGeometry(380, 400, 250, 50)
        self.but_stop.setFont(self.boldFont)
        self.but_stop.clicked.connect(self.stop)

        self.but_start = QPushButton("Start", self)
        self.but_start.setGeometry(380, 340, 250, 50)
        self.but_start.setFont(self.boldFont)
        self.but_start.clicked.connect(self.start)

        self.but_exit = QPushButton("Exit", self)
        self.but_exit.setGeometry(380, 460, 250, 50)
        self.but_exit.setFont(self.boldFont)
        self.but_exit.clicked.connect(self.exit)

    @cached_property
    def worker(self):
        return Worker()

    @property
    def amount(self):
        value = self.input_amount.value()
        return value

    @property
    def adressed(self):
        return self.input_adressed.text()

    @property
    def message(self):
        return self.input_message.text()

    def stop(self):
        print("programm stopps ...")
        QCoreApplication.quit()


    def exit(self):
        QCoreApplication.quit()

    def start(self):
        pop_up = QMessageBox(self)
        pop_up.setWindowTitle("Start Bot")
        pop_up.setText("Do you really wanna start the spam ?!")
        pop_up.setIcon(QMessageBox.Question)
        pop_up.setStandardButtons(QMessageBox.Cancel | QMessageBox.No | QMessageBox.Yes)
        pop_up.setDefaultButton(QMessageBox.Yes)
        if pop_up.exec_() == QMessageBox.Yes:
            print("programm starts ...")
            self.worker.start(self.amount, self.adressed, self.message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    x = interface()
    sys.exit(app.exec_())


