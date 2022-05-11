import os
from setuptools import setup, find_packages

setup(
    name = "graph_test",
    version = "0.0.1",
    author = "Jon Ander Asua",
    author_email = "jasuamiranda1998@gmail.com",
    description = (""),
    license = "",
    keywords = "",
    packages=['procesSource','graphSource'],
    package_dir={"": "./"},
    long_description="Imagine a long description",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=[
        "pytest>=6.1.0"
    ]
)