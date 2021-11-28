import os
from glob import glob
from setuptools import setup, find_packages

package_name = 'part3_2_py_rosparam_example'


setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('./launch/*.launch.py')),
    ],

    entry_points={
        'console_scripts': [
            'param_int2string = '+ package_name +'.param_int2string:ros_main'
        ],
    }
)