from setuptools import setup, find_packages

setup(
    name="landsatxplore",
    version="0.15.0",
    packages=find_packages(),
    install_requires=[
        "python-dateutil>=2.8.0",
        "requests>=2.20.0",
        "shapely>=1.7.0",
        "tqdm>=4.58.0",
        "click>=7.1.0",
    ],
    entry_points={
        "console_scripts": [
            "landsatxplore=landsatxplore.cli:cli",
        ],
    },
    author="Yann Forget",
    author_email="yannforget@mailbox.org",
    description="Search and download Landsat scenes from EarthExplorer",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yannforget/landsatxplore",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
) 