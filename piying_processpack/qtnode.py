import rclpy  
from rclpy.node import Node  
from sensor_msgs.msg import Image  
from std_msgs.msg import String
from std_msgs.msg import Header
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy 
from cv_bridge import CvBridge
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets, QtGui
from sys import exit, argv
import sys

app = QApplication(sys.argv)

class Ui_MainWindow(object):
    #UI显示 目前没做窗口位置固定
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(832, 599)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, -10, 781, 581))
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 500, 801, 71))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")   #按钮1

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")   #按钮2

        self.horizontalLayout.addWidget(self.pushButton_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 832, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"opencvLabel", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

    #openCV显示主函数
    def ShowCV(self, cv_image):  
    # 将OpenCV的BGR图像转换为Qt的QImage（需要RGB格式）  
        height, width, channel = cv_image.shape  
        bytes_per_line = 3 * width  # RGB图像，每像素3个字节  
        qt_image = QImage(cv_image.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()  
    
        # 创建QPixmap对象，并设置QLabel  
        pixmap = QPixmap.fromImage(qt_image)  
        scaled_pixmap = pixmap.scaled(self.label.width(), self.label.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)  
        self.label.setPixmap(scaled_pixmap) 
        QApplication.processEvents()


class QtFrontendNode(Node):
    def __init__(self):
        super().__init__('qtfrontend')
        self.ui = Ui_MainWindow()
        self.widget = QMainWindow()
        self.ui.setupUi(self.widget)
        self.widget.show()
        self.bridge = CvBridge()
        qos_profile = QoSProfile(  
            depth=10,           # 队列深度  
            reliability=QoSReliabilityPolicy.BEST_EFFORT,  # 可靠性策略  
            history=QoSHistoryPolicy.KEEP_LAST             # 历史记录策略  
        ) 
        self.subscription = self.create_subscription(
            Image,
            'image/frame', 
            self.image_callback, qos_profile)

    def image_callback(self, msg):
        cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        self.ui.ShowCV(cv_image)

def main(args=None):
    rclpy.init(args=args)
    node = QtFrontendNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()