import sys,os
import cv2
from PySide6.QtWidgets import QMainWindow,QApplication,QFileDialog
from PySide6.QtGui import QPixmap,QImage
from PySide6.QtCore import QTimer
from mywindow import Ui_MainWindow
from detect_re import run
import torch


def convert2QImage(img):
    height, width, channel = img.shape
    return QImage(img,width,height,width * channel,QImage.Format_RGB888)

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = torch.hub.load("./","custom",path="runs/train/exp/weights/best.pt",source="local")
        self.timer = QTimer()
        self.timer.setInterval(1)
        self.bind_slots()
        self.video = None

    def image_pred(self,f_path):
        results = self.model(f_path)
        img = results.render()[0]
        return convert2QImage(img)

    def video_pred(self):
        ret, frame = self.video.read()
        if not ret:
            self.timer.stop()
        else:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.input.setPixmap(QPixmap.fromImage(convert2QImage(frame)))
            results = self.model(frame)
            img = results.render()[0]
            self.ouput.setPixmap(QPixmap.fromImage(convert2QImage(img)))

    def open_img2(self):
        self.timer.stop()
        file_path = QFileDialog.getOpenFileName(self, dir='mydata/split/train', filter='*.jpg;*.png,*.jpeg')
        if file_path[0]:
            file_path=file_path[0]
            self.input.setPixmap(QPixmap(file_path))
            qimage = self.image_pred(file_path)
            self.ouput.setPixmap(QPixmap.fromImage(qimage))

    def open_img(self):  # will generate './txt'
        self.timer.stop()
        file_path = QFileDialog.getOpenFileName(self, dir='mydata/split/train', filter='*.jpg;*.png,*.jpeg')
        if file_path[0]:
            file_path = file_path[0]
            self.input.setPixmap(QPixmap(file_path))
        run(source=file_path)
        path = 'runs/detect/exp1'
        f_path = os.path.join(path,os.listdir(path)[0])
        self.ouput.setPixmap(QPixmap(f_path))

    def open_video(self):
        file_path = QFileDialog.getOpenFileName(self, dir='mydata', filter='*.mp4')
        if file_path[0]:
            file_path = file_path[0]
            self.input.setPixmap(QPixmap(file_path))
            self.video = cv2.VideoCapture(file_path)
            self.timer.start()


    def bind_slots(self):
        self.det_img_2.clicked.connect(self.open_img2)
        self.det_img.clicked.connect(self.open_img)
        self.det_video.clicked.connect(self.open_video)
        self.timer.timeout.connect(self.video_pred)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()