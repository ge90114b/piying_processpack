import rclpy  
from rclpy.node import Node  
from sensor_msgs.msg import Image  
from std_msgs.msg import String
from std_msgs.msg import Header
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy 
from cv_bridge import CvBridge
from piying_processpack.qtfrontend import *
from PyQt5.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)



class QtFrontendNode(Node):
    def __init__(self):
        super().__init__('my_node')
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
    timer = QTimer()
    timer.timeout.connect(lambda: None)
    timer.start(1000 / 30)  # 每秒30帧
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()