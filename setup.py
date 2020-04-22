#!/usr/bin/env python

from distutils.core import setup

setup(
    name='webkit2-launcher',
    version='0.1',
    description='A very simple launcher for webapps',
    author='Maciej Krüger',
    author_email='mkg20001@gmail.com',
    url='https://os.mercode.org',
    packages=['launcher', 'launcher.example'],
    package_dir={'launcher': 'launcher'},
    package_data={'launcher.example': ['example/*']},
    entry_points={
        'console_scripts': [
            'webkit2-launcher=launcher.launcher:main',
        ],
    },
)
