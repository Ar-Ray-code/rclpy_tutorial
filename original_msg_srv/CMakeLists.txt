cmake_minimum_required(VERSION 3.5)
project(original_msg_srv)

set(CMAKE_CXX_STANDARD 17)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/ExampleMsg.msg"
  "srv/CalcMsgSrv.srv"
)

ament_export_dependencies(rosidl_default_runtime)

ament_package()