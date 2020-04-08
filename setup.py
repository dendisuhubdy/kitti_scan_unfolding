# -*- coding: utf-8 -*-

from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name="unfolding",
    version="1.0",
    author="Larissa Triess",
    author_email="mail@triess.eu",
    description="Scan unfolding for raw KITTI point clouds",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ltriess/kitti_scan_unfolding",
    license="MIT",
    packages=["unfolding"],
    python_requires=">=3.5",
    install_requires=["numpy"],
)
