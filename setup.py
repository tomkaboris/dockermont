from setuptools import setup, find_packages

setup(
    name='docker_monitor',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'docker'
    ],
    entry_points={
        'console_scripts': [
            'docker-monitor=dockermont.monitor:DockerMonitor',
        ],
    },
    author='Boris',
    description='A simple Docker container monitoring package',
    url='https://github.com/tomkaboris/dockermont',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
