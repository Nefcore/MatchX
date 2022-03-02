# Installs this tool in your system

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "MatchX",
    version = "1.0",
    author = "Devansh Raghav",
    license = "MIT",
    keywords = ["MatchX", "Bug Bounty", "pentesting", "security", "hacking"],
    url = "https://github.com/whoamisec75/MatchX",
    packages=find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ],
    install_requires=[
        'colorama',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'matchx = MatchX.__main__:main'
        ]
    },
)
