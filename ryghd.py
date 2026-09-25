import os
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QUrl
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(826, 583)

        self.audio_output_1 = QAudioOutput()
        self.player_1 = QMediaPlayer()
        self.player_1.setAudioOutput(self.audio_output_1)
        self.audio_output_1.setVolume(0.5)
        self.player_1.setSource(QUrl.fromLocalFile(os.path.abspath("Enrique.mp3")))

        self.audio_output_2 = QAudioOutput()
        self.player_2 = QMediaPlayer()
        self.player_2.setAudioOutput(self.audio_output_2)
        self.audio_output_2.setVolume(0.5)
        self.player_2.setSource(QUrl.fromLocalFile(os.path.abspath("Fahhh_Meme.mp3")))

        self.audio_output_3 = QAudioOutput()
        self.player_3 = QMediaPlayer()
        self.player_3.setAudioOutput(self.audio_output_3)
        self.audio_output_3.setVolume(0.5)
        self.player_3.setSource(QUrl.fromLocalFile(os.path.abspath("ok.mp3")))

        self.audio_output_4 = QAudioOutput()
        self.player_4 = QMediaPlayer()
        self.player_4.setAudioOutput(self.audio_output_4)
        self.audio_output_4.setVolume(0.5)
        self.player_4.setSource(QUrl.fromLocalFile(os.path.abspath("idk.mp3")))

        self.audio_output_5 = QAudioOutput()
        self.player_5 = QMediaPlayer()
        self.player_5.setAudioOutput(self.audio_output_5)
        self.audio_output_5.setVolume(0.5)
        self.player_5.setSource(QUrl.fromLocalFile(os.path.abspath("Hell_nah.mp3")))

        self.audio_output_6 = QAudioOutput()
        self.player_6 = QMediaPlayer()
        self.player_6.setAudioOutput(self.audio_output_6)
        self.audio_output_6.setVolume(0.5)
        self.player_6.setSource(QUrl.fromLocalFile(os.path.abspath("ah_shit.mp3")))

        self.audio_output_7 = QAudioOutput()
        self.player_7 = QMediaPlayer()
        self.player_7.setAudioOutput(self.audio_output_7)
        self.audio_output_7.setVolume(0.5)
        self.player_7.setSource(QUrl.fromLocalFile(os.path.abspath("pls_speed.mp3")))

        self.audio_output_8 = QAudioOutput()
        self.player_8 = QMediaPlayer()
        self.player_8.setAudioOutput(self.audio_output_8)
        self.audio_output_8.setVolume(0.5)
        self.player_8.setSource(QUrl.fromLocalFile(os.path.abspath("why.mp3")))

        self.audio_output_9 = QAudioOutput()
        self.player_9 = QMediaPlayer()
        self.player_9.setAudioOutput(self.audio_output_9)
        self.audio_output_8.setVolume(0.5)
        self.player_9.setSource(QUrl.fromLocalFile(os.path.abspath("Man.mp3")))

        self.audio_output_10 = QAudioOutput()
        self.player_10 = QMediaPlayer()
        self.player_10.setAudioOutput(self.audio_output_10)
        self.audio_output_10.setVolume(0.5)
        self.player_10.setSource(QUrl.fromLocalFile(os.path.abspath("Alarm.mp3")))

        self.audio_output_11 = QAudioOutput()
        self.player_11 = QMediaPlayer()
        self.player_11.setAudioOutput(self.audio_output_11)
        self.audio_output_11.setVolume(0.5)
        self.player_11.setSource(QUrl.fromLocalFile(os.path.abspath("OMG_Wow_Meme.mp3")))

        self.audio_output_12 = QAudioOutput()
        self.player_12 = QMediaPlayer()
        self.player_12.setAudioOutput(self.audio_output_12)
        self.audio_output_12.setVolume(0.5)
        self.player_12.setSource(QUrl.fromLocalFile(os.path.abspath("amogus.mp3")))

        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(70, 40, 141, 141))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.CrossCursor))
        self.pushButton.setDefault(True)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.play_sound_1)

        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 40, 141, 141))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.CrossCursor))
        self.pushButton_2.setDefault(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.play_sound_2)

        self.pushButton_3 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_3.setGeometry(QtCore.QRect(560, 40, 141, 141))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.CrossCursor))
        self.pushButton_3.setDefault(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.play_sound_3)

        self.pushButton_4 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_4.setGeometry(QtCore.QRect(400, 40, 141, 141))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.CrossCursor))
        self.pushButton_4.setDefault(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.play_sound_4)

        self.pushButton_5 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_5.setGeometry(QtCore.QRect(240, 210, 141, 141))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.CrossCursor))
        self.pushButton_5.setDefault(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.play_sound_5)

        self.pushButton_6 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_6.setGeometry(QtCore.QRect(70, 210, 141, 141))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.CrossCursor))
        self.pushButton_6.setDefault(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.play_sound_6)

        self.pushButton_7 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_7.setGeometry(QtCore.QRect(400, 210, 141, 141))
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.CrossCursor))
        self.pushButton_7.setDefault(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.play_sound_7)

        self.pushButton_8 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_8.setGeometry(QtCore.QRect(560, 210, 141, 141))
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.CrossCursor))
        self.pushButton_8.setDefault(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.play_sound_8)

        self.pushButton_9 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_9.setGeometry(QtCore.QRect(240, 380, 141, 141))
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.CrossCursor))
        self.pushButton_9.setDefault(True)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.play_sound_9)

        self.pushButton_10 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_10.setGeometry(QtCore.QRect(70, 380, 141, 141))
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.CrossCursor))
        self.pushButton_10.setDefault(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.clicked.connect(self.play_sound_10)

        self.pushButton_11 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_11.setGeometry(QtCore.QRect(400, 380, 141, 141))
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.CrossCursor))
        self.pushButton_11.setDefault(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.clicked.connect(self.play_sound_11)

        self.pushButton_12 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_12.setGeometry(QtCore.QRect(560, 380, 141, 141))
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.CrossCursor))
        self.pushButton_12.setDefault(True)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.clicked.connect(self.play_sound_12)
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def play_sound_1(self):
        self.player_1.setPosition(0)
        self.player_1.play()

    def play_sound_2(self):
        self.player_2.setPosition(0)
        self.player_2.play()

    def play_sound_3(self):
        self.player_3.setPosition(0)
        self.player_3.play()

    def play_sound_4(self):
        self.player_4.setPosition(0)
        self.player_4.play()

    def play_sound_5(self):
        self.player_5.setPosition(0)
        self.player_5.play()

    def play_sound_6(self):
        self.player_6.setPosition(0)
        self.player_6.play()

    def play_sound_7(self):
        self.player_7.setPosition(0)
        self.player_7.play()

    def play_sound_8(self):
        self.player_8.setPosition(0)
        self.player_8.play()

    def play_sound_9(self):
        self.player_9.setPosition(0)
        self.player_9.play()

    def play_sound_10(self):
        self.player_10.setPosition(0)
        self.player_10.play()

    def play_sound_11(self):
        self.player_11.setPosition(0)
        self.player_11.play()

    def play_sound_12(self):
        self.player_12.setPosition(0)
        self.player_12.play()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Enrique"))
        self.pushButton_2.setText(_translate("Form", "FAHHHH"))
        self.pushButton_3.setText(_translate("Form", "Aproved"))
        self.pushButton_4.setText(_translate("Form", "I don't know"))
        self.pushButton_5.setText(_translate("Form", "Hell nah"))
        self.pushButton_6.setText(_translate("Form", "AH shit"))
        self.pushButton_7.setText(_translate("Form", "Please speed"))
        self.pushButton_8.setText(_translate("Form", "Why this game is so fun"))
        self.pushButton_9.setText(_translate("Form", "Man shut up"))
        self.pushButton_10.setText(_translate("Form", "ALARM"))
        self.pushButton_11.setText(_translate("Form", "Omg,Wow"))
        self.pushButton_12.setText(_translate("Form", "Amogus"))

class Window(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()