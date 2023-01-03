from setuptools import setup, find_packages

VERSION = "0.0.1"
DESCRIPTION = "3D Barcharts for Plotly"
LONG_DESCRIPTION = "An add-on to make 3D barcharts in plotly."

setup(
    name="BarChart3D",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="Justin Korelc",
    author_email="23109889+JKORELC@users.noreply.github.com",
    license="MIT",
    packages=find_packages(),
    install_requires=[],
    keywords="plotly barchart 3d",
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ]
)
