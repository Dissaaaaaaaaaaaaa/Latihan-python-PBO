from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QSlider, QStyle, QSizePolicy, QFileDialog
from PyQt5.QtGui import QIcon, QPalette
from PyQt5.QtCore import Qt, QUrl
import sys,os
import vlc

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("mp4 nya dissa")
        self.setGeometry(350, 100, 700, 500)
        self.setWindowIcon(QIcon('2.jpg'))

        p = self.palette()
        p.setColor(QPalette.Window, Qt.black)
        self.setPalette(p)

        self.instance = vlc.Instance(["--no-xlib"])  # Add options as needed
        self.mediaPlayer = self.instance.media_player_new()

        self.init_ui()
        self.show()

    def init_ui(self):
        # create open button
        openBtn = QPushButton('Open Video')
        openBtn.clicked.connect(self.open_file)

        # create button for playing
        self.playBtn = QPushButton()
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playBtn.clicked.connect(self.play_video)

        # create slider for position
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 0)
        self.slider.sliderMoved.connect(self.set_position)

        # create slider for volume
        self.volumeSlider = QSlider(Qt.Horizontal)
        self.volumeSlider.setRange(0, 100)
        self.volumeSlider.setValue(50)  # Set default volume to 50
        self.volumeSlider.sliderMoved.connect(self.set_volume)

        # create label
        self.label = QLabel()
        self.label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

        # create videowidget object
        videowidget = QWidget()

        # create hbox layout
        hboxLayout = QHBoxLayout()
        hboxLayout.setContentsMargins(0, 0, 0, 0)

        # set widgets to the hbox layout
        hboxLayout.addWidget(openBtn)
        hboxLayout.addWidget(self.playBtn)
        hboxLayout.addWidget(self.slider)

        # create vbox layout
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(videowidget)
        vboxLayout.addLayout(hboxLayout)
        vboxLayout.addWidget(self.label)
        vboxLayout.addWidget(self.volumeSlider)  # Add volume slider to the layout

        self.setLayout(vboxLayout)

        self.mediaPlayer.set_hwnd(videowidget.winId())

        # media player signals
        self.mediaPlayer.set_fullscreen(True)  # Uncomment this line if you want fullscreen by default
        self.mediaPlayer.set_mrl("")  # Add media resource locator as needed
        self.mediaPlayer.play()

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")

        if filename != '':
            media = self.instance.media_new(QUrl.fromLocalFile(filename).toString())
            self.mediaPlayer.set_media(media)
            self.playBtn.setEnabled(True)

    def play_video(self):
        if self.mediaPlayer.is_playing():
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def set_position(self, position):
        self.mediaPlayer.set_position(position / 1000.0)

    def set_volume(self, volume):
        self.mediaPlayer.audio_set_volume(volume)

    def handle_errors(self):
        self.playBtn.setEnabled(False)
        self.label.setText("Error: " + self.mediaPlayer.errorString())
        print("Error: " + self.mediaPlayer.errorString())

os.add_dll_directory(os.getcwd())
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
