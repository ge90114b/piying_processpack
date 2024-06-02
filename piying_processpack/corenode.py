import rclpy  
from rclpy.node import Node  
from std_msgs.msg import String
from std_msgs.msg import Header
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy 
import threading
import time
import json
import numpy as np
from piying_processpack.send_to_py import send

play='stop'
rec="stop"
filedir=''
point=''
mode='cap'
newPoints = []
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
    def minus(self,cent,org):
        pr=[0,0]
        for i in range(2):
            pr[i]=org[i]-cent[i]
        return pr
    def process_thread(self):
        while True:
            msg=''
            if play =='stop':
                self.pubstat(msg="停止中") 
                continue
            if mode == 'cap':
                msg+='实时模式'
                p=np.array([0,0])
                msg+=self.processcore(point,p)
            elif mode == "file":
                msg+='文件模式'                    
                if not filedir or not filedir.endswith(".act"):
                    msg+='\n未选择有效文件'
                    self.pubstat(msg=msg) 
                    continue
            self.pubstat(msg=msg)                
    def processcore(self,points:list,orgPoint):
        global newPoints
        arrayList,newPoints = [],[]    
        if len(points) == 11:           #正式用，调试不用
            for i1 in [0,5,6,9,10]:
                for i2 in [0,1]:
                    if points[i1][i2]==0:
                        return "\n未识别到有效人体关键点！"
                #坐标转换 将手臂中点移向坐标原点（orgPoint）
            points = [points[0],points[5],points[6],points[9],points[10]]
        for i1 in points:
            arrayList.append(np.array(i1)) #将列表转为数组
        
        midP = arrayList[1] + (arrayList[2] - arrayList[1])/2 #计算中点（向量法）
        print(type(midP),type(orgPoint))
        vector = orgPoint - midP #转换向量
        for i in arrayList:
            newPoints.append(i + vector)
        left_hand = newPoints[3] + np.array((-50,-50))
        right_hand = newPoints[4] + np.array((-50,50))
        nose = newPoints[0] + np.array((0,20))
        send.send(nose,left_hand,right_hand,midP.tolist()[0],midP.tolist()[1])
        return "\n正常"
    
        try:...
        except :
            return '\nerror'

        
        #nose = [round(x / 160,3) for x in points[0]] 
        #left_shoulder=[round(x / 160,3) for x in points[5]] 
        #right_shoulder=[round(x / 160,3) for x in points[6]] 
        #centpoint=[0,0]
        #for pos in [0,1]:
        #    centpoint[pos]=(left_shoulder[pos]+right_shoulder[pos])/2
        #centpoint=[round(x / 160,3) for x in centpoint] 
        #left_hand=[round(x / 160,3) for x in points[9]] 
        #right_hand=[round(x / 160,3) for x in points[10]] 
        #print(nose,centpoint,left_hand,right_hand)
        
        return "\n正在捕捉"
    


def main(args=None):
    rclpy.init(args=args)
    node = CoreNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()