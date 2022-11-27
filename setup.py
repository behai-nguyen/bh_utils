"""
Installation script for bh-utils project.

* Upgrade:

C:\PF\Python310\python.exe -m pip install --upgrade virtualenv 
C:\PF\Python310\python.exe -m pip install --upgrade pip

* Create virtual environment venv:

C:\PF\Python310\Scripts\virtualenv.exe venv

* Install wheel:

.\venv\Scripts\pip.exe install wheel

* Editable install:

venv\Scripts\pip.exe install -e .

* Package:

venv\Scripts\python.exe setup.py bdist_wheel

==> F:\bh_utils\dist\bh_utils-1.0.0-py3-none-any.whl

* Install package on a new environment:

venv\Scripts\pip.exe install bh_utils-1.0.0-py3-none-any.whl

"""
from pathlib import Path
from setuptools import setup, find_packages

setup(
    name='bh-utils',
    description='BeHai Utility Library',
    version='1.0.0',
    author='Van Be Hai Nguyen',
    author_email='behai_nguyen@hotmail.com',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires='>=3.10',
    install_requires=[
        'PyYAML',
        'pytest',
        'coverage',
    ],
)