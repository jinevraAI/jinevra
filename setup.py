from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jinevra",
    version="0.0.1",
    author="Eleanor Stribling",
    author_email="hello@jinevra.ai",
    description="jinevra democratizes AI for natural language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://jinevra.herokuapp.com",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
