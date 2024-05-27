from launch import LaunchDescription  
from launch_ros.actions import Node  
  
def generate_launch_description():  
    # 定义yolo节点  
    yolo_node = Node(  
        package='piying_processpack',  
        executable='yolo',  
        name='yolo_node',  
        
    )  
      
    # 定义frontend节点  
    frontend_node = Node(  
        package='piying_processpack',  
        executable='frontend',  
        name='frontend_node',  
        
    )  
      
    
    return LaunchDescription([  
        yolo_node,  
        frontend_node,  
    ])
