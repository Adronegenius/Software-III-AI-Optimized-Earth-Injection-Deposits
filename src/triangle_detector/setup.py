from setuptools import setup

package_name = 'triangle_detector'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your@email.com',
    description='ROS 2 node for triangle detection and centroid publishing using YOLOv8.',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'triangle_detector_node = triangle_detector.triangle_detector_node:main',
        ],
    },
)