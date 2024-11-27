from setuptools import setup, find_packages

setup(
    name="doclayout-detector",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "torch>=1.9",
        "torchvision>=0.10",
        "huggingface_hub",
    ],
    author="Prashant Verma",
    author_email="prashant27050@gmail.com",
    description="A library for document layout detection using YOLO.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your_username/doclayout-detector",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
