from setuptools import setup, find_packages

setup(
    name="ddf_optimizer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scipy",
        "pandas"
    ],
    author="151Wang",
    author_email="shuyi.wang@slu.se",
    description="A Python package for Directional Distance Function (DDF) optimization",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com//pyddf",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
