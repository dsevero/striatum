from setuptools import find_packages, setup

# TODO: Freeze versions
install_requires = [
    'gym',
    'pandas',
    'numpy',
    'matplotlib',
    'dask'
]

# TODO: Freeze versions
tests_require = [
    'pytest',
    'pytest-cov',
    'pylava',
    'pytest-xdist',
    'ipdb',
]

dev_require = [
    'ipython'
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
