from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'ros2_aeb_simulation'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')), 
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Danis Balazs',
    maintainer_email='bldanis04@gmail.com',
    description='ROS2-based automatic emergency braking system simulation',
    license='GNU General Public License v3.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # 'control_vehicle = ros2_aeb_simulation.control_vehicle:main',
        ],
    },
)
