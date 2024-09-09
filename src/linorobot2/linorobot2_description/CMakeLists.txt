cmake_minimum_required(VERSION 3.5)
project(linorobot2_description)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(tf2_ros REQUIRED)
find_package(urdf REQUIRED)

install(
  DIRECTORY launch urdf rviz
  DESTINATION share/${PROJECT_NAME}
)

install(
  PROGRAMS src/odom_to_tf.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
