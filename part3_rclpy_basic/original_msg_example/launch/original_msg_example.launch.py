import launch
import launch_ros.actions

def generate_launch_description():
    pub_int32_a = launch_ros.actions.Node(
        package='pub_sub_int32', executable='pub_int_node',
        parameters=[
            {'pub_rate' : 10}
        ],
        remappings=[
            ('pub_int', '/a')
        ],
    )
    pub_int32_b = launch_ros.actions.Node(
        package='pub_sub_int32', executable='pub_int_node',
        namespace='b',
        parameters=[
            {'pub_rate' : 2}
        ],
        remappings=[
            ('pub_int', '/b')
        ],
    )
    original_msg_example = launch_ros.actions.Node(
        package='original_msg_example', executable='example_msg_output'
    )

    rqt_graph = launch_ros.actions.Node(
        package='rqt_graph', executable='rqt_graph'
    )

    return launch.LaunchDescription([
        pub_int32_a,
        pub_int32_b,
        original_msg_example,
        rqt_graph
    ])