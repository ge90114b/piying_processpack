import rclpy  
from rclpy.node import Node  
from std_msgs.msg import String
from std_msgs.msg import Header
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy 
import threading
import time
import json

play='stop'
rec="stop"
filedir=''
point=''
mode='cap'
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
        self.action_publisher = self.create_publisher(String, 'action', qos_profile) #创建动作publisher
        self.statue_publisher = self.create_publisher(String, 'stat', qos_profile)#创建状态publisher
        
        self.process_thr=threading.Thread(target=self.process_thread)
        self.process_thr.daemon=True
        self.process_thr.start()
        
    def play_callback(self,msg):
        global play
        play=msg.data
    def rec_callback(self,msg):
        global rec
        rec=msg.data
    def dir_callback(self,msg):
        global filedir
        filedir=msg.data
        
    def points_callback(self,msg):
        global point
        point=json.loads(msg.data)
    def mode_callback(self,msg):
        global mode
        mode=msg.data
    def pubstat(self,msg):#发布运行状态
        ctlmsg=String()
        ctlmsg.data=str(msg)
        self.statue_publisher.publish(ctlmsg)
    def pubact(self,msg):#发布动作
        ctlmsg=String()
        ctlmsg.data=str(msg)
        self.action_publisher.publish(ctlmsg)
    def process_thread(self):
        while True:
            msg=''
            if play =='stop':
                self.pubstat(msg="停止中") 
                continue
            if mode == 'cap':
                msg+='实时模式'
                msg+=self.processcore(points=point)
            elif mode == "file":
                msg+='文件模式'                    
                if not filedir or not filedir.endswith(".act"):
                    msg+='\n未选择有效文件'
                    self.pubstat(msg=msg) 
                    continue
            self.pubstat(msg=msg)                
    def processcore(self,points):#点位信息转化
        print(points)
        try:
            for i1 in [0,5,6,9,10]:
                for i2 in [0,1]:
                    if points[i1][i2]==0:
                        return "\n未识别到有效人体关键点！"
        except :
            
            return '\nerror'

        
        nose = [round(x / 160,3) for x in points[0]] 
        left_shoulder=[round(x / 160,3) for x in points[5]] 
        right_shoulder=[round(x / 160,3) for x in points[6]] 
        centpoint=[0,0]
        for pos in [0,1]:
            centpoint[pos]=(left_shoulder[pos]+right_shoulder[pos])/2
        centpoint=[round(x / 160,3) for x in centpoint] 
        left_hand=[round(x / 160,3) for x in points[9]] 
        right_hand=[round(x / 160,3) for x in points[10]] 
        print(nose,centpoint,left_hand,right_hand)
        return "\n正在捕捉"


def main(args=None):
    rclpy.init(args=args)
    node = CoreNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()