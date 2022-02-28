from importlib.metadata import entry_points
from setuptools import setup

setup(
    name="fbhq",
    version="0.0.1",
    author="zblurx",
    url="https://github.com/zblurx/acltoolkit",
    long_description="README.md",
    license="MIT",
    packages=["fbhq"],
    install_requires=[
        "py2neo"
    ],
    entry_points={
        "console_scripts":["fbhq=fbhq.entry:main"],
    },
)