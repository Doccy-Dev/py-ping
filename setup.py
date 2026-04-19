import os
from setuptools import setup, find_packages

setup(
    name="py-ping",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "py-ping=py_ping.main:main"
        ]
    }
)
