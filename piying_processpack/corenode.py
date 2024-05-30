import rclpy  
from rclpy.node import Node  
from std_msgs.msg import String
from std_msgs.msg import Header
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy 
import threading
import time

play='stop'
rec="stop"
filedir=''
point=''
class CoreNode(Node):
    def __init__(self):
        super().__init__('CoreNode')
        qos_profile = QoSProfile(  
            depth=10,           # 队列深度  
            reliability=QoSReliabilityPolicy.BEST_EFFORT,  # 可靠性策略  
            history=QoSHistoryPolicy.KEEP_LAST             # 历史记录策略  
        ) 
        self.playsubscription = self.create_subscription(
            String,
            'play', 
            self.play_callback, qos_profile)#创建启动控制subscriber
        self.recsubscription = self.create_subscription(
            String,
            'rec', 
            self.rec_callback, qos_profile)#创建录像控制subscriber
        self.dirsubscription = self.create_subscription(
            String,
            'filedir', 
            self.dir_callback, qos_profile)#创建动作文件地址subscriber
        self.points_subscription = self.create_subscription(  
            String,  
            'points',  
            self.points_callback, qos_profile) #创建点位subscriber
        self.mode_subscription = self.create_subscription(  
            String,  
            'mode',  
            self.mode_callback, qos_profile) #创建模式subscriber
        self.action_publisher = self.create_publisher(String, 'action', qos_profile) 
        self.process_thr=threading.Thread(target=self.process_thread)
        self.process_thr.daemon=True
        self.process_thr.start()
        
    def play_callback(self,msg):
        global play
        print(msg.data)
        play=msg.data
    def rec_callback(self,msg):
        global rec
        rec=msg.data
    def dir_callback(self,msg):
        global dir
        dir=msg.data
    def points_callback(self,msg):
        global point
        point=msg.data
    def process_thread(self):
        while True:
            if play =='stop':
                continue
            
            self.processcore(points=point)
    def processcore(self,points):#点位信息转化
        for i1 in [0,5,6,9,10]:
            for i2 in [0,1]:
                if points[i1][i2]==0:
                    bad=True
                    break
            if bad:
                break
        if not bad:
            nose=points[0]
            left_shoulder=points[5]
            right_shoulder=points[6]
            centpoint=[]
            for pos in [0,1]:
                centpoint[pos]=(left_shoulder[pos]+right_shoulder[pos])/2
                
            left_hand=points[9]
            right_hand=points[10]




def main(args=None):
    rclpy.init(args=args)
    node = CoreNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()