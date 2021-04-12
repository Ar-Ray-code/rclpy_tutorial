import launch
import launch_ros.actions

def generate_launch_description():
    pub_int32 = launch_ros.actions.Node(
        package='pub_sub_int32', executable='pub_int_node',
        parameters=[
            {'pub_rate'     : 2}
        ]
    )
    sub_int32 = launch_ros.actions.Node(
        package='pub_sub_int32', executable='sub_int_node',
        parameters=[
            {'pub_rate'     : 1}
        ]
    )
    original_msg_example = launch_ros.actions.Node(
        package='original_msg_example', executable='example_msg_output'
    )

    rqt_graph = launch_ros.actions.Node(
        package='rqt_graph', executable='rqt_graph'
    )

    return launch.LaunchDescription([
        pub_int32,
        sub_int32,
        rqt_graph,
        original_msg_example
    ])