# setup.py placed at root directory
import tarfile
from setuptools import setup, find_packages

setup(
    name='mle-training',
    version='1.0.0',
    author='Parul Vijay',
    description='MLE training Project. Fun Project!',
    long_description='This Project will help to find the regression values with help of differnt parameters',
    packages= ['src\data_ingest', 'src\model_scoring', 'src\model_training'],
    install_requires=['pandas', 'tarfile', 'six', 'sklearn', 'numpy', 'pickle']

    # python_requires='>=3.7, <4',
    # install_requires=['pandas'],
    # extras_require={
    #     'test': ['pytest', 'coverage'],
    # },
    # package_data={
    #     'sample': ['example_data.csv'],
    # },
    # entry_points={
    #     'runners': [
    #         'sample=sample:main',
    #     ]
    # }
)