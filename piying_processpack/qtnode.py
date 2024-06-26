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
import cv2

app = QApplication(sys.argv)

#designer自动生成代码由 class Ui_MainWindow(object): 到 # retranslateUi，这一部分代码会因ui变化而反复被替代，建议全局变量不要写进setupUi内，可以再设一个class存储所有的全局变量
#按钮加事件用 self.对象.clicked.connect(函数)
#单选按钮事件用 self.对象.buttonClicked.connect(函数)
#
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 667)
        self.actionaaa = QAction(MainWindow)
        self.actionaaa.setObjectName(u"actionaaa")
        self.actionaaa.setCheckable(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setBaseSize(QSize(0, 0))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(9, 9, 9, -1)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.statue = QLabel(self.centralwidget)
        self.statue.setObjectName(u"statue")
        self.statue.setMinimumSize(QSize(140, 0))
        self.statue.setCursor(QCursor(Qt.ForbiddenCursor))
        self.statue.setFrameShape(QFrame.Panel)
        self.statue.setFrameShadow(QFrame.Sunken)
        self.statue.setLineWidth(2)
        self.statue.setTextFormat(Qt.AutoText)
        self.statue.setAlignment(Qt.AlignCenter)
        self.statue.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.statue)

        self.record = QPushButton(self.centralwidget)
        self.record.setObjectName(u"record")

        self.verticalLayout_2.addWidget(self.record)

        self.end_record = QPushButton(self.centralwidget)
        self.end_record.setObjectName(u"end_record")

        self.verticalLayout_2.addWidget(self.end_record)

        self.play = QPushButton(self.centralwidget)
        self.play.setObjectName(u"play")

        self.verticalLayout_2.addWidget(self.play)

        self.end_play = QPushButton(self.centralwidget)
        self.end_play.setObjectName(u"end_play")

        self.verticalLayout_2.addWidget(self.end_play)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 4, 1, 2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(720, 540))
        self.label.setMaximumSize(QSize(720, 540))
        self.label.setCursor(QCursor(Qt.ForbiddenCursor))
        self.label.setFrameShape(QFrame.Box)
        self.label.setFrameShadow(QFrame.Raised)
        self.label.setLineWidth(1)
        self.label.setMidLineWidth(0)
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 0, 1, 1, 1)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
#if QT_CONFIG(statustip)
        self.lineEdit.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
        self.lineEdit.setAutoFillBackground(False)

        self.gridLayout.addWidget(self.lineEdit, 2, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.capture = QRadioButton(self.centralwidget)
        self.capture.setObjectName(u"capture")

        self.horizontalLayout_3.addWidget(self.capture)

        self.readFiles = QRadioButton(self.centralwidget)
        self.readFiles.setObjectName(u"readFiles")

        self.horizontalLayout_3.addWidget(self.readFiles)


        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 1, 1, 1)

        self.summit = QPushButton(self.centralwidget)
        self.summit.setObjectName(u"summit")

        self.gridLayout.addWidget(self.summit, 2, 4, 1, 2)

        self.gridLayout.setRowStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 22))
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
        self.actionaaa.setText(QCoreApplication.translate("MainWindow", u"aaa", None))
#if QT_CONFIG(statustip)
        self.statue.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.statue.setText("")
        self.record.setText(QCoreApplication.translate("MainWindow", u"\u5f55\u5236", None))
        self.end_record.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u5f55\u5236", None))
        self.play.setText(QCoreApplication.translate("MainWindow", u"\u64ad\u653e", None))
        self.end_play.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u64ad\u653e", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"opencvLabel", None))
#if QT_CONFIG(tooltip)
        self.lineEdit.setToolTip(QCoreApplication.translate("MainWindow", u"sss", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.lineEdit.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7c98\u8d34\u8def\u5f84\u4ee5\u53d1\u9001\u81f3topic", None))
        self.capture.setText(QCoreApplication.translate("MainWindow", u"\u5b9e\u65f6\u6355\u6349", None))
        self.readFiles.setText(QCoreApplication.translate("MainWindow", u"\u8bfb\u53d6\u6587\u4ef6", None))
        self.summit.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u4ea4\u8868\u5355", None))
    # retranslateUi
        self.pixmap = QPixmap() 

    #openCV显示主函数
    def ShowCV(self, cv_image):  
        # 将OpenCV的BGR图像转换为Qt的QImage（需要RGB格式）  
        cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        height, width, channel = cv_image.shape  
        bytes_per_line = 3 * width  # RGB图像，每像素3个字节  
        qt_image = QImage(cv_image.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()  
    
        # 更新QPixmap对象，并设置QLabel  
        self.pixmap = QPixmap.fromImage(qt_image)  
        self.label.resize(self.pixmap.width(), self.pixmap.height())
        scaled_pixmap = self.pixmap.scaled(self.label.width(), self.label.height(), Qt.KeepAspectRatio, Qt.SmoothTransformation)  
        self.label.setPixmap(scaled_pixmap) 
        QApplication.processEvents()
    def setStatueText(self, text: str):  #更新状态栏
        self.statue.setText(text)


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
        self.statsubscription = self.create_subscription(
            String,
            'stat', 
            self.stat_callback, qos_profile)#创建图片subscriber
        
        self.playpub=self.create_publisher(String,'play',qos_profile)#为开始按钮、文件名、录制按钮创建发布者
        self.recpub=self.create_publisher(String,'rec',qos_profile)
        self.filepub=self.create_publisher(String,'filedir',qos_profile)
        self.modepub=self.create_publisher(String,'mode',qos_profile)

        self.ui.play.clicked.connect(lambda : self.play(msg="start"))
        self.ui.end_play.clicked.connect(lambda : self.play(msg="stop"))
        self.ui.record.clicked.connect(lambda : self.rec(msg="start"))
        self.ui.end_record.clicked.connect(lambda : self.rec(msg="stop"))
        self.ui.summit.clicked.connect(lambda : self.filedir())
        self.ui.capture.clicked.connect(lambda : self.modeswitch(msg="cap"))
        self.ui.readFiles.clicked.connect(lambda : self.modeswitch(msg="file"))

    def image_callback(self, msg):
        cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")#接受图片topic并转为opencv
        self.ui.ShowCV(cv_image)
    def stat_callback(self,msg):
        stat=msg.data
        self.ui.setStatueText(stat)
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
    def modeswitch(self,msg):#传递模式切换
        ctlmsg=String()
        ctlmsg.data=msg
        self.modepub.publish(ctlmsg)
def main(args=None):
    rclpy.init(args=args)
    node = QtFrontendNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
