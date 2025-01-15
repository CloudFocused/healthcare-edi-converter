from setuptools import setup, find_packages

setup(
    name="healthclaimconverter",
    version="0.1.0",
    author="Chad",
    description="A library to convert 837p EDI files to JSON format",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/healthclaimconverter",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)