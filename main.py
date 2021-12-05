import ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPainter, QPixmap, QPen, QImage, QIcon
from PyQt5.QtCore import Qt
import numpy as np
import cv2
import sys


class ExampleApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self._raw_image: np.array = None
        self._current_image: np.array = None
        self._ui = ui_MainWindow.Ui_MainWindow()
        self._ui.setupUi(self)
        self._ui.applyTransform.clicked.connect(self.apply_transform)
        self._ui.openAction.triggered.connect(self.open_file)
        self._ui.resetPointsButton.clicked.connect(self.clear_points)
        self._ui.resetTransformButton.clicked.connect(self.reset_transform)
        self._ui.viewer.signalFourPoints.connect(self.all_points)
        self._ui.viewer.signalOnePoint.connect(lambda: self._ui.resetPointsButton.setEnabled(True))
        self._ui.saveButton.clicked.connect(self.save_image)
        self._ui.saveButton.setEnabled(False)
        self._ui.applyTransform.setEnabled(False)
        self._ui.resetTransformButton.setEnabled(False)
        self._ui.resetPointsButton.setEnabled(False)
        self._ui.label.setVisible(False)

        # Иконка, сделанная на коленке
        pixmap = QPixmap(300, 300)
        pixmap.fill()
        painter = QPainter(pixmap)
        painter.setPen(QPen(Qt.black, 10))
        painter.drawEllipse(50, 50, 200, 200)
        painter.end()
        self.setWindowIcon(QIcon(pixmap))

    def clear_points(self):
        self._ui.viewer.clearPoints()
        self._ui.applyTransform.setEnabled(False)
        self._ui.resetPointsButton.setEnabled(False)

    def all_points(self):
        self._ui.applyTransform.setEnabled(True)
        self._ui.label.setVisible(False)

    def reset_transform(self):
        self._current_image = self._raw_image.copy()
        self.clear_points()
        self.show_image()
        self._ui.resetTransformButton.setEnabled(False)

    def show_image(self):
        height, width, pix_dim = self._current_image.shape
        bytesPerLine = pix_dim * width
        qImg = QImage(self._current_image.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
        self._ui.viewer.setPixmap(QPixmap.fromImage(qImg))
        self._ui.saveButton.setEnabled(True)

    def open_file(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Open File', './', "Image (*.png *.jpg *jpeg)")
        self._raw_image = cv2.imread(file)
        self._current_image = self._raw_image.copy()
        self.show_image()
        self._ui.resetTransformButton.setEnabled(False)
        self._ui.label.setVisible(True)
        self.clear_points()

    def save_image(self):
        if self._current_image is not None:
            path, _ = QFileDialog.getSaveFileName(self, 'Save File', './', "Images (*.png *.jpg *jpeg)")
            cv2.imwrite(path, self._current_image)

    def apply_transform(self):
        if self._current_image is None:
            return

        points = self._ui.viewer.getPoints()
        if len(points) < 4:
            return

        height, width, _ = self._current_image.shape

        ROIpoints = np.zeros((4,2), dtype='float32')

        counter = 0
        for point in points:
            ROIpoints[counter][0] = point[0] * width
            ROIpoints[counter][1] = point[1] * height
            counter += 1

        rect = np.zeros((4,2), dtype='float32')

        # наименьшая сумма будет у верхнего левого угла,
        # наибольшая - у нижнего правого угла
        s = np.sum(ROIpoints, axis=1)
        rect[0] = ROIpoints[np.argmin(s)]
        rect[2] = ROIpoints[np.argmax(s)]

        # верх-право будет с минимальной разницей
        # низ-лево будет иметь максимальную разницу
        diff = np.diff(ROIpoints, axis=1)
        rect[1] = ROIpoints[np.argmin(diff)]
        rect[3] = ROIpoints[np.argmax(diff)]

        # верх-лево, верх-право, низ-право, низ-лево
        (tl, tr, br, bl) = rect

        # вычислить ширину ROI
        widthA = np.sqrt((tl[0] - tr[0])**2 + (tl[1] - tr[1])**2 )
        widthB = np.sqrt((bl[0] - br[0])**2 + (bl[1] - br[1])**2 )
        maxWidth = max(int(widthA), int(widthB))

        # вычислить высоту ROI
        heightA = np.sqrt((tl[0] - bl[0])**2 + (tl[1] - bl[1])**2 )
        heightB = np.sqrt((tr[0] - br[0])**2 + (tr[1] - br[1])**2 )
        maxHeight = max(int(heightA), int(heightB))

        # набор итоговых точек для обзора всего документа
        # размер нового изображения
        dst = np.array([
            [0,0],
            [maxWidth-1, 0],
            [maxWidth-1, maxHeight-1],
            [0, maxHeight-1]], dtype="float32")

        # вычислить матрицу перспективного преобразования и применить её
        transformMatrix = cv2.getPerspectiveTransform(rect, dst)

        # преобразовать ROI
        self._current_image = cv2.warpPerspective(self._current_image, transformMatrix, (maxWidth, maxHeight))
        self.show_image()
        self.clear_points()
        self._ui.resetTransformButton.setEnabled(True)


def main():
    app = QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
