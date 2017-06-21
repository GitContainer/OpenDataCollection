# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Open Data Collection',
    version='0.0.1',
    description='open data collection',
    long_description=readme,
    author='林聖泰',
    author_email='shengtai0201@gmail.com',
    url='https://github.com/shengtai0201/OpenDataCollection',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
