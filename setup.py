from importlib.metadata import entry_points
from setuptools import find_packages, setup

import pathlib

with open("README.md", "r") as f:
    ld = f.read()

with open(
    str(pathlib.Path(__file__).parent.absolute()) + "/fib_py/version.py", "r"
) as f:
    version = f.read().split("=")[1].replace("'", "")

setup(
    name="fib_py",
    version=version,
    author="Jiajun Xie",
    author_email="kifferob9@outlook.com",
    description="Calculates a Fibonacci number",
    long_description=ld,
    long_description_content_type="text/markdown",
    url="https://github.com/JiajunX31/fib_py.git",
    install_requires=["PyYAML>=6.0", "dill>=0.3.4"],
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "fib-number = fib_py.cmd.fib_num:fib_num",
        ]
    },
    extras_require={"server": ["Flask>=2.0.0"]},
    python_requires=">=3",
    tests_require=["pytest"],
)
