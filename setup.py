import os
from glob import glob
from setuptools import setup

package_name = 'metu_gui_v2'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yoy',
    maintainer_email='yusufonatyilmaz@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'talker = metu_gui_v2.ros_test_message:main',
                'listener = metu_gui_v2.rover_gui:main',
        ],
    },
)
