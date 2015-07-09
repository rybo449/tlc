import multiprocessing
import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    import distribute_setup
    distribute_setup.use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='tlc',
    version='1.0',
    author='Sriniketh Vijayaraghavan, Doug Steinberg, Lluvia Hernandez, Yixue Wang',
    description='tlc taxi analysis toolkit',
    author_email='sv1272@nyu.edu',
    packages=find_packages(),
    url='http://github.com/rybo449/tlc',
    install_requires=[
        'httplib2==0.9.1',
        'python-instagram==1.3.1',
        'simplejson==3.7.3',
        'six==1.9.0',
        'wsgiref==0.1.2',
    ],
    keywords='TLC',
    zip_safe = True
)