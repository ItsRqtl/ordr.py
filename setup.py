from setuptools import setup, find_packages

VERSION = '0.0.5' 
DESCRIPTION = 'A simple o!rdr API and Websocket wrapper.'
LONG_DESCRIPTION = 'ordr.py is a simple and easy to use o!rdr API and Websocket wrapper.'

setup(
    name="ordr.py", 
    version=VERSION,
    author="Ryan",
    author_email="itsrql@gmail.com",
    description=DESCRIPTION,
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ItsRqtl/ordr.py",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3"
    ],
    packages=find_packages(),
    install_requires=[
        "requests", 
        "python-socketio",
        "aiohttp"
    ],
)