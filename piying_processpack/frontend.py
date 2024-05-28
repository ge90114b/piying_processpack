import rclpy  
from rclpy.node import Node  
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy 
from sensor_msgs.msg import Image  
from std_msgs.msg import String  
from cv_bridge import CvBridge  
import cv2  
  
class ImageAndPointsSubscriber(Node):  
  
    def __init__(self):  
        super().__init__('backend')  
        self.bridge = CvBridge()  
        qos_profile = QoSProfile(  
            depth=10,           # 队列深度  
            reliability=QoSReliabilityPolicy.BEST_EFFORT,  # 可靠性策略  
            history=QoSHistoryPolicy.KEEP_LAST             # 历史记录策略  
        ) 
        self.image_subscription = self.create_subscription(  
            Image,  
            'image/frame',  
            self.image_callback,  
            qos_profile)  
  
        self.points_subscription = self.create_subscription(  
            String,  
            'points',  
            self.points_callback,  
            qos_profile) 
         
  
    def image_callback(self, msg):  
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')  
        cv2.imshow('Interface', cv_image)  
        cv2.waitKey(1)  
  
    def points_callback(self, msg):  
        self.get_logger().info(f'Received points message: {msg.data}')  
  
def main(args=None):  
    rclpy.init(args=args)  
    node = ImageAndPointsSubscriber()  
    try:  
        rclpy.spin(node)  
    except KeyboardInterrupt:  
        node.get_logger().info('KeyboardInterrupt detected, shutting down node...')  
    finally:  
        node.destroy_node()  
        rclpy.shutdown()  
        cv2.destroyAllWindows()  
  
if __name__ == '__main__':  
    main()