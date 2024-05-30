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
from sys import exit, argv
import sys
from PyQt5.QtCore import pyqtSignal  

app = QApplication(sys.argv)

#designer自动生成代码由 class Ui_MainWindow(object): 到 # retranslateUi，这一部分代码会因ui变化而反复被替代，建议全局变量不要写进setupUi内，可以再设一个class存储所有的全局变量
#按钮加事件用 self.对象.clicked.connect(函数)
class Ui_MainWindow(object):
    playbut = pyqtSignal()
    endplaybut = pyqtSignal()
    recbut = pyqtSignal()
    endrecbut = pyqtSignal()
    submit = pyqtSignal()
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(597, 393)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 0, 1, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        #录制 按钮
        self.record = QPushButton(self.centralwidget)
        self.record.setObjectName(u"record")


        self.verticalLayout_2.addWidget(self.record)
        self.record.clicked.connect(lambda: self.recbut.emit())
        #结束录制 按钮
        self.end_record = QPushButton(self.centralwidget)
        self.end_record.setObjectName(u"end_record")

        self.verticalLayout_2.addWidget(self.end_record)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)
        self.end_record.clicked.connect(lambda: self.endrecbut.emit())
        #播放 按钮
        self.play = QPushButton(self.centralwidget)
        self.play.setObjectName(u"play")

        self.verticalLayout_2.addWidget(self.play)
        self.play.clicked.connect(lambda: self.playbut.emit())

        #停止播放 按钮
        self.end_play = QPushButton(self.centralwidget)
        self.end_play.setObjectName(u"end_play")

        self.verticalLayout_2.addWidget(self.end_play)
        self.end_play.clicked.connect(lambda: self.endplaybut.emit())


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 2, 1, 1)
        #opencv视窗
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        #界面右下角提交 按钮
        self.summit = QPushButton(self.centralwidget)
        self.summit.setObjectName(u"submit")

        self.gridLayout.addWidget(self.summit, 1, 2, 1, 1)
        self.summit.clicked.connect(lambda: self.submit.emit())
        #界面下方 输入条
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
#if QT_CONFIG(statustip)
        self.lineEdit.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
        self.lineEdit.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.gridLayout.setColumnStretch(0, 6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 597, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(statustip)
        MainWindow.setStatusTip("")
#endif // QT_CONFIG(statustip)
        #要改按钮文字直接在这里改
        self.record.setText(QCoreApplication.translate("MainWindow", u"\u5f55\u5236", None))
        self.end_record.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u5f55\u5236", None))
        self.play.setText(QCoreApplication.translate("MainWindow", u"\u64ad\u653e", None))
        self.end_play.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u64ad\u653e", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"opencvLabel", None))
        self.summit.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u4ea4\u8868\u5355", None))
#if QT_CONFIG(tooltip)
        self.lineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"sss", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.lineEdit.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7c98\u8d34\u8def\u5f84\u4ee5\u53d1\u9001\u81f3topic", None))
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
        self.imgsubscription = self.create_subscription(
            Image,
            'image/frame', 
            self.image_callback, qos_profile)#创建图片subscriber
        
        self.playpub=self.create_publisher(String,'play',qos_profile)#为开始按钮、文件名、录制按钮创建发布者
        self.recpub=self.create_publisher(String,'rec',qos_profile)
        self.filepub=self.create_publisher(String,'filedir',qos_profile)

        self.ui.playbut.connect(lambda : self.playpub.publish(String(data="start")))
        self.ui.endplaybut.connect(lambda : self.playpub.publish(String(data="stop")))
        self.ui.recbut.connect(lambda : self.recpub.publish(String(data="start")))
        self.ui.endrecbut.connect(lambda : self.recpub.publish(String(data="stop")))
        self.ui.submit.connect(lambda : self.filepub.publish(String(data = self.ui.lineEdit.text())))

    def image_callback(self, msg):
        cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")#接受图片topic并转为opencv
        self.ui.ShowCV(cv_image)
    def play(self,msg):#控制是否开始
        ctlmsg=String()
        ctlmsg.data=str(msg)
        self.playpub.publish(ctlmsg)
    def rec(self,msg):#控制是否开始
        ctlmsg=String()
        ctlmsg.data=str(msg)
        self.recpub.publish(ctlmsg)
    def filedir(self):#传递动作文件目录
        dir = self.ui.lineEdit.text()
        msg=String()
        msg.data=dir
        self.filepub.publish(msg)
def main(args=None):
    rclpy.init(args=args)
    node = QtFrontendNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()