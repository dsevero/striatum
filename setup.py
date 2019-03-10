from setuptools import find_packages, setup

install_requires = [
    'gym==0.12.0',
    'pandas==v0.24.1',
    'numpy==v1.16.2',
    'matplotlib==v3.0.3',
    'dask==1.1.3',
    'seaborn==v0.9.0',
    'cloudpickle'
]

tests_require = [
    'pytest==4.3.0',
    'pylava==0.2.2',
]

dev_require = [
    'ipython==7.3.0'
]

setup(
    name='striatum',
    packages=find_packages(),
    version='v0.1.0-alpha',
    author='dsevero',
    install_requires=install_requires,
    extras_require={
        'tests': tests_require,
        'dev': tests_require + dev_require,
        'complete': install_requires + tests_require + dev_require
    }
)
