from setuptools import setup
from glob import glob
package_name = 'piying_processpack'
 
setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    package_data={
        'qtfrontend': ['piying_processpack/qtfrontend.py']
    },
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, glob("launch/*.launch.py"))
    ],
    install_requires=['setuptools','opencv-python','torch','ultralytics','numpy','pyzmq','tornado','PyQt5'],
    zip_safe=False,
    maintainer='ge90114b',
    maintainer_email='ge90114b@outlook.com',
    description='Piyingbot process package',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'yolo=piying_processpack.yolo_node:main',
            'frontend=piying_processpack.frontend:main',
            'qtfrontend=piying_processpack.qtnode:main'
        ],
    },
)