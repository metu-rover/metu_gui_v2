from launch import LaunchDescription
from launch_ros.actions import Node

##! I have no idea why this works.
##! This one needs further investigation.
##! This approach combine both nodes into the listener node.
##! Try ros2 run rqt_graph rqt_graph with and without launchfile.

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='metu_gui_v2',
            executable='talker',
            name='talkers'),

        Node(
            package='metu_gui_v2',
            executable='listener',
            name='listeners'),
    ])