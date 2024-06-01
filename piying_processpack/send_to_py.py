import zmq  
import json  
import time 

class send(): 
    def send(HEAD,LEFT_HAND,RIGHT_HAND,X,Y):
            context = zmq.Context()  
            socket = context.socket(zmq.PUSH)  
            socket.bind("tcp://*:6666") 
            # 准备一个 JSON 对象  
            data = {
                "HEAD":HEAD,
                "LEFT_HAND":LEFT_HAND,
                "RIGHt_HAND":RIGHT_HAND,
                "X":X,
                "Y":Y
            }  
            data = json.dumps(data)
            
            socket.send_string(data)  # 第一个部分通常是主题，这里为空  
            print("sent")
            
if __name__=="__main__":
    send.send(1,1,1,1,1)