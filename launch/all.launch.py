from launch import LaunchDescription  
from launch_ros.actions import Node  
  
def generate_launch_description():  
    # 定义yolo节点  
    yolo_node = Node(  
        package='piying_processpack',  
        executable='yolo',  
        name='yolo_node',  
        
    )  

    qt_frontend_node = Node(  
        package='piying_processpack',  
        executable='qtfrontend',  
        name='qtfrontend_node',  
        
    ) 
    core_node = Node(  
        package='piying_processpack',  
        executable='core',  
        name='core_node',  
        
    ) 
      
    
    return LaunchDescription([  
        yolo_node,  
        core_node, 
        qt_frontend_node 
    ])
