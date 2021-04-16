import launch
import launch_ros.actions

def generate_launch_description():
    pub_int32 = launch_ros.actions.Node(
        package='pub_sub_int32', executable='pub_int_node'
    )
    sub_int32 = launch_ros.actions.Node(
        package='pub_sub_int32', executable='sub_int_node'
    )
    rqt_graph = launch_ros.actions.Node(
        package='rqt_graph', executable='rqt_graph'
    )

    return launch.LaunchDescription([
        pub_int32,
        sub_int32,
        rqt_graph
    ])