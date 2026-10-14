from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    turtlebot4_launch = PathJoinSubstitution(
        [
            FindPackageShare("turtlebot4_ignition_bringup"),
            "launch",
            "turtlebot4_ignition.launch.py",
        ]
    )

    return LaunchDescription(
        [
            DeclareLaunchArgument("sim_world", default_value="depot"),
            DeclareLaunchArgument("x", default_value="0.0"),
            DeclareLaunchArgument("y", default_value="0.0"),
            DeclareLaunchArgument("z", default_value="0.0"),
            DeclareLaunchArgument("yaw", default_value="0.0"),
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(turtlebot4_launch),
                launch_arguments={
                    "world": LaunchConfiguration("sim_world"),
                    "rviz": "true",
                    "gazebo": "ignition",
                    "use_sim_time": "true",
                    "x": LaunchConfiguration("x"),
                    "y": LaunchConfiguration("y"),
                    "z": LaunchConfiguration("z"),
                    "yaw": LaunchConfiguration("yaw"),
                }.items(),
            )
        ]
    )
