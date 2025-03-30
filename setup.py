from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="openmindx",
    version="0.1.0",
    author="wawei",
    author_email="wawei@wawei.com",
    description="一个确定性时延的图像生成大模型git clone https://github.com/qwqqq6/openmindx.git",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/openmindx",
    packages=["mindx"],  # 指定包名为mindx
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)