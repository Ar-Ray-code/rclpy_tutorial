import os
from glob import glob
from setuptools import setup

package_name = 'pub_sub_int32'

setup(
    name=package_name,
    version='0.0.0',
    packages=[],
    py_modules= [
        'scripts.pub_int',
        'scripts.sub_int'
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Ar-Ray-code',
    author_email="ray255ar@gmail.com",
    maintainer='user',
    maintainer_email="ray255ar@gmail.com",
    keywords=['ROS', 'ROS2'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='TODO: Package description.',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pub_int_node = scripts.pub_int:ros_main',
            'sub_int_node = scripts.sub_int:ros_main'
        ],
    },
    data_files=[
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
    ],
)
