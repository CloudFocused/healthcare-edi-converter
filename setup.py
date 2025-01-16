from setuptools import setup, find_packages

setup(
    name="healthcare-edi-converter",
    version="0.1.0",
    author="CloudFocus.tech",
    description="A library to convert 837p EDI files objects",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/CloudFocused/healthcare-edi-converter",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)