#
# Launch file for playback of an audio stream or wav file.
#
import os

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir, LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    
    log_level = DeclareLaunchArgument('log_level', default_value='info')
    
    input_device = DeclareLaunchArgument('input_device', default_value='/jetson-voice/data/audio/dusty.wav')
    
    audio_input = Node(package='jetson_voice_ros', executable='audio_input.py',
                       parameters=[
                            {"device": LaunchConfiguration('input_device')},
                       ],
                       arguments=['--ros-args', '--log-level', LaunchConfiguration('log_level')],
                       output='screen', emulate_tty=True)              
                            
    return LaunchDescription([
        log_level,
        input_device,
        audio_input
    ])