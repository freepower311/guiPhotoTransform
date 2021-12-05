from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QPoint, pyqtSignal, QSize
from PyQt5.QtGui import QPainter, QPixmap, QMouseEvent, QPaintEvent, QPen


class ImageViewer(QWidget):
    signalFourPoints = pyqtSignal()
    signalOnePoint = pyqtSignal()

    def __init__(self, parent):
        super().__init__(parent)
        self._pixmap = None
        self._points = []
        self._centerPoint = None
        self._imageSize = QSize()


    def setPixmap(self, pixmap: QPixmap):
        self._pixmap = pixmap
        self.update()

    def paintEvent(self, event: QPaintEvent):
        qp = QPainter(self)
        if self._pixmap is not None:
            scaledPixmap = self._pixmap.scaled(self.size(), Qt.KeepAspectRatio)
            self._centerPoint = QPoint(int((self.size().width()  - scaledPixmap.width())  / 2), \
                                 int((self.size().height() - scaledPixmap.height()) / 2))
            self._imageSize = scaledPixmap.size()
            qp.drawPixmap(self._centerPoint, scaledPixmap)
            for point in self._points:
                targetPoint = QPoint(int(self._imageSize.width()  * point[0] + self._centerPoint.x()), \
                                     int(self._imageSize.height() * point[1] + self._centerPoint.y()))
                qp.setPen(QPen(Qt.red, 2));
                qp.drawLine(targetPoint.x() - 5, \
                            targetPoint.y(), \
                            targetPoint.x() + 5, \
                            targetPoint.y())
                qp.drawLine(targetPoint.x(), \
                            targetPoint.y() - 5, \
                            targetPoint.x(), \
                            targetPoint.y() + 5)
        else:
            qp.drawText(event.rect(), Qt.AlignCenter, "Выберите изображение. (Файл->Открыть)")
        qp.end()


    def mousePressEvent(self, ev: QMouseEvent):
        if ev.button() == Qt.LeftButton and self._pixmap is not None and len(self._points) < 4:
            ev.accept()
            pos = ev.pos()
            if pos.x() < self._centerPoint.x() or \
                pos.x() > self._centerPoint.x() + self._imageSize.width() or \
                pos.y() < self._centerPoint.y() or \
                pos.y() > self._centerPoint.y() + self._imageSize.height():
                return

            x = (pos.x() - self._centerPoint.x()) / self._imageSize.width()
            y = (pos.y() - self._centerPoint.y()) / self._imageSize.height()
            if len(self._points) == 0:
                self.signalOnePoint.emit()
            self._points.append([x, y])
            if len(self._points) == 4:
                self.signalFourPoints.emit()

            self.update()
        else:
            return QWidget.mousePressEvent(self, ev)

    def clearPoints(self):
        self._points.clear()
        self.update()

    def getPoints(self):
        return self._points
