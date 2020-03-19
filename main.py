from design import Ui_Form
from PyQt5.QtWidgets import QApplication, QWidget
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia

SOUNDS = {'a': "Sounds\\contrabassoon_A1_025_forte_normal.mp3",
          'b': "Sounds\\contrabassoon_B0_025_forte_normal.mp3",
          'c': "Sounds\\contrabassoon_C1_025_forte_normal.mp3",
          'd': "Sounds\\contrabassoon_D1_025_forte_normal.mp3",
          'e': "Sounds\\contrabassoon_D3_025_forte_normal.mp3",
          'f': "Sounds\\contrabassoon_Fs1_025_forte_normal.mp3",
          'g': "Sounds\\contrabassoon_G1_025_forte_normal.mp3",
          'h': "Sounds\\contrabassoon_C3_025_forte_normal.mp3",
          'i': "Sounds\\contrabassoon_E3_025_forte_normal.mp3",
          'j': "Sounds\\contrabassoon_Cs1_025_forte_normal.mp3",
          'k': "Sounds\\contrabassoon_G3_025_forte_normal.mp3",
          'l': "Sounds\\contrabassoon_F1_025_forte_normal.mp3",
          'm': "Sounds\\contrabassoon_E1_025_forte_normal.mp3",
          'n': "Sounds\\contrabassoon_B3_025_forte_normal.mp3",
          'p': "Sounds\\contrabassoon_C4_025_forte_normal.mp3",
          'q': "Sounds\\contrabassoon_A3_025_forte_normal.mp3",
          'r': "Sounds\\contrabassoon_D4_long_forte_major-trill.mp3",
          's': "Sounds\\contrabassoon_A2_025_forte_normal.mp3",
          't': "Sounds\\contrabassoon_Ds1_025_forte_normal.mp3",
          'u': "Sounds\\contrabassoon_F2_025_forte_normal.mp3",
          'w': "Sounds\\contrabassoon_As1_025_forte_normal.mp3",
          'x': "Sounds\\contrabassoon_As2_025_forte_normal.mp3",
          'y': "Sounds\\contrabassoon_F3_025_forte_normal.mp3",
          'z': "Sounds\\contrabassoon_As0_025_forte_normal.mp3",
          'v': "Sounds\\contrabassoon_B1_025_forte_normal.mp3",
          }


class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.player = QtMultimedia.QMediaPlayer()
        self.pushButton.clicked.connect(
            lambda checked, button=self.pushButton: self.button_press(button)
        )
        self.pushButton_2.clicked.connect(
            lambda checked, button=self.pushButton_2: self.button_press(button)
        )
        self.pushButton_3.clicked.connect(
            lambda checked, button=self.pushButton_3: self.button_press(button)
        )
        self.pushButton_4.clicked.connect(
            lambda checked, button=self.pushButton_4: self.button_press(button)
        )
        self.pushButton_5.clicked.connect(
            lambda checked, button=self.pushButton_5: self.button_press(button)
        )
        self.pushButton_6.clicked.connect(
            lambda checked, button=self.pushButton_6: self.button_press(button)
        )
        self.pushButton_7.clicked.connect(
            lambda checked, button=self.pushButton_7: self.button_press(button)
        )
        self.pushButton_8.clicked.connect(
            lambda checked, button=self.pushButton_8: self.button_press(button)
        )
        self.pushButton_9.clicked.connect(
            lambda checked, button=self.pushButton_9: self.button_press(button)
        )
        self.pushButton_10.clicked.connect(
            lambda checked, button=self.pushButton_10: self.button_press(button)
        )
        self.pushButton_11.clicked.connect(
            lambda checked, button=self.pushButton_11: self.button_press(button)
        )
        self.pushButton_12.clicked.connect(
            lambda checked, button=self.pushButton_12: self.button_press(button)
        )
        self.pushButton_13.clicked.connect(
            lambda checked, button=self.pushButton_13: self.button_press(button)
        )
        self.pushButton_14.clicked.connect(
            lambda checked, button=self.pushButton_14: self.button_press(button)
        )
        self.pushButton_15.clicked.connect(
            lambda checked, button=self.pushButton_15: self.button_press(button)
        )
        self.pushButton_16.clicked.connect(
            lambda checked, button=self.pushButton_16: self.button_press(button)
        )
        self.pushButton_17.clicked.connect(
            lambda checked, button=self.pushButton_17: self.button_press(button)
        )
        self.pushButton_18.clicked.connect(
            lambda checked, button=self.pushButton_18: self.button_press(button)
        )
        self.pushButton_19.clicked.connect(
            lambda checked, button=self.pushButton_19: self.button_press(button)
        )
        self.pushButton_20.clicked.connect(
            lambda checked, button=self.pushButton_20: self.button_press(button)
        )
        self.pushButton_21.clicked.connect(
            lambda checked, button=self.pushButton_21: self.button_press(button)
        )
        self.pushButton_22.clicked.connect(
            lambda checked, button=self.pushButton_22: self.button_press(button)
        )
        self.pushButton_23.clicked.connect(
            lambda checked, button=self.pushButton_23: self.button_press(button)
        )
        self.pushButton_24.clicked.connect(
            lambda checked, button=self.pushButton_24: self.button_press(button)
        )
        self.pushButton_25.clicked.connect(
            lambda checked, button=self.pushButton_25: self.button_press(button)
        )

    def load_mp3(self, filename):
        media = QtCore.QUrl.fromLocalFile(filename)
        content = QtMultimedia.QMediaContent(media)
        self.player.setMedia(content)

    def keyPressEvent(self, e):
        if e.text().lower() in SOUNDS:
            self.load_mp3(SOUNDS[e.text().lower()])
            self.player.play()

    def button_press(self, button):
        self.load_mp3(SOUNDS[button.text()[button.text().index('[') + 1:button.text().index(']')].lower()])
        self.player.play()


app = QApplication(sys.argv)
ex = Window()
ex.show()
sys.exit(app.exec_())