from launch import LaunchDescription
from launch.actions import ExecuteProcess, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    sensors_launch_path = PathJoinSubstitution([
        FindPackageShare('linorobot2_bringup'), 'launch', 'sensors.launch.py'
    ])

    description_launch_path = PathJoinSubstitution([
        FindPackageShare('linorobot2_description'), 'launch', 'description.launch.py'
    ])

    # joy_launch_path = PathJoinSubstitution([
    #     FindPackageShare('linorobot2_bringup'), 'launch', 'joy_teleop.launch.py'
    # ])

    micro_ros_agent = ExecuteProcess(
        cmd=['ros2', 'run', 'micro_ros_agent', 'micro_ros_agent', 'udp4', '--port', '8888'],
        output='screen'
    )

    ekf_config_path = PathJoinSubstitution(
        [FindPackageShare("linorobot2_base"), "config", "ekf.yaml"]
    )

    return LaunchDescription([
        micro_ros_agent,
        Node(
            package='robot_localization',
            executable='ekf_node',
            name='ekf_filter_node',
            output='screen',
            parameters=[
                ekf_config_path
            ],
            remappings=[("odometry/filtered", "odom")]
        ),
        IncludeLaunchDescription(PythonLaunchDescriptionSource(description_launch_path)),
        IncludeLaunchDescription(PythonLaunchDescriptionSource(sensors_launch_path)),
        #IncludeLaunchDescription(PythonLaunchDescriptionSource(joy_launch_path))
    ])

