import rclpy  
from rclpy.node import Node  
from sensor_msgs.msg import Image  
from std_msgs.msg import String
from sensor_msgs.msg import Image as SensorImage  
BGR8 = SensorImage().BGR8
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy 
from ultralytics import YOLO
import torch 
import socket  
import struct  
import numpy as np  
import cv2  
import threading
class YoloNode(Node):  
    def __init__(self):  
        super().__init__('yolo_node')  
        self.UDP_IP = "0.0.0.0"  
        self.UDP_PORT = 9999  
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
        self.sock.bind((self.UDP_IP, self.UDP_PORT))  
        self.model = YOLO('./model/yolov8n-pose.pt')
        qos_profile = QoSProfile(  
            depth=10,           # 队列深度  
            reliability=QoSReliabilityPolicy.BEST_EFFORT,  # 可靠性策略  
            history=QoSHistoryPolicy.KEEP_LAST             # 历史记录策略  
        ) 
        self.image_publisher = self.create_publisher(Image, 'image/frame', qos_profile)  
        self.points_publisher = self.create_publisher(String, 'points', qos_profile) 
  
        # UDP监听线程  
  
        self.udp_thread = threading.Thread(target=self.udp_listener)  
        self.udp_thread.daemon = True  
        self.udp_thread.start()  
    def trans_to_ros(self,frame):
        # 将OpenCV图像转换为ROS 2 Image消息  
                    header = self.create_timestamped_header()  
                    image_msg = Image()  
                    image_msg.header = header  
                    image_msg.height = frame.shape[0]  
                    image_msg.width = frame.shape[1]  
                    image_msg.encoding = BGR8  
                    image_msg.is_bigendian = 0  
                    image_msg.step = frame.shape[1] * frame.shape[2]  
                    image_msg.data = frame.tobytes() 
                    return image_msg
    def interface(self,frame):
         result=self.model(frame)
         annotated_frame = result[0].plot() 
         keypoints = result[0].keypoints.xy.squeeze().tolist()
         ret=[annotated_frame,keypoints]
         return ret
    def udp_listener(self):  
        while rclpy.ok():  
            try:  
                data, addr = self.sock.recvfrom(65507)  
                size = struct.unpack('i', data[:4])[0]  
                if len(data) == size + 4:  
                    frame_data = data[4:]  
                    frame = np.frombuffer(frame_data, dtype=np.uint8)  
                    frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)  
                    interface=self.interface(frame)
                    frame=interface[0]
  
                    # 发布ROS 2 Image消息  
                    self.image_publisher.publish(self.trans_to_ros(frame)) 
                    self.points_publisher.publish(interface[1]) 
  
            except Exception as e:  
                self.get_logger().error(f'Error in UDP listener: {e}')  

    def shutdown(self):  
        self.sock.close()  
        super().shutdown()  

def main(args=None):  
    rclpy.init(args=args)  
  
    node = YoloNode()  
  
    rclpy.spin(node)  
  
    node.shutdown()  
    rclpy.shutdown()  
  
if __name__ == '__main__':  
    main()