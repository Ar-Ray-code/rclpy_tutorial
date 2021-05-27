import launch
import launch_ros.actions

def generate_launch_description():
    param_int2string_node = launch_ros.actions.Node(
        package='part3_2_py_rosparam_example', executable='param_int2string',
        parameters=[
            {'get_number'     : 1}
        ]
    )

    return launch.LaunchDescription([
        param_int2string_node
    ])
