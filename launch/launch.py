from launch import LaunchDescription  
from launch_ros.actions import Node  
  
def generate_launch_description():  
    # 定义yolo节点  
    yolo_node = Node(  
        package='process',  # 替换为实际的yolo节点所在的包名  
        executable='yolo',  # 替换为实际的yolo节点可执行文件名  
        name='yolo_node',  
        # 可以添加其他参数，如命名空间、重映射等  
    )  
      
    # 定义frontend节点  
    frontend_node = Node(  
        package='process',  # 替换为实际的frontend节点所在的包名  
        executable='frontend',  # 替换为实际的frontend节点可执行文件名  
        name='frontend_node',  
        # 可以添加其他参数，如命名空间、重映射等  
    )  
      
    # 返回LaunchDescription对象，包含要启动的节点  
    return LaunchDescription([  
        yolo_node,  
        frontend_node,  
    ])