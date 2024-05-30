import rclpy  
from rclpy.node import Node  
from std_msgs.msg import String
from std_msgs.msg import Header
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy 

rec,play='stop'
filedir=''

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
            lambda msg: (global play ; play=msg.data), qos_profile)#创建启动控制subscriber
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
        
    def play_callback(self,msg):
        global play
        play=msg.data
    def rec_callback(self,msg):
        global play
        play=msg.data
    def dir_callback(self,msg):
        global play
        play=msg.data
    def points_callback(self,msg):
        global play
        play=msg.data
    def process_thread(self):
        while play=='start':
            print("start")
        



def main(args=None):
    rclpy.init(args=args)
    node = CoreNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()