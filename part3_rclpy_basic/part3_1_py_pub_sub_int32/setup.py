import os
from glob import glob
from setuptools import setup, find_packages

package_name = 'part3_1_py_pub_sub_int32'


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
            'pub_int = '+ package_name +'.pub_int:ros_main',
            'sub_int = '+ package_name +'.sub_int:ros_main',
        ],
    }
)