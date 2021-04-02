cmake_minimum_required(VERSION 3.0.2)
project(original_msg_example)

set(CMAKE_CXX_FLAGS "-std=c++11 ${CMAKE_CXX_FLAGS}")

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  message_generation
)

add_message_files(
  FILES
  example_msg.msg
)
## using service
add_service_files(
  FILES
  calc_msg_srv.srv
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_package(
 CATKIN_DEPENDS
  rospy
  std_msgs
)
