#!/usr/bin/env python
import os
import re

from setuptools import setup, find_packages


version = re.compile(r'VERSION\s*=\s*\((.*?)\)')


def get_package_version():
    "returns package version without importing it"
    base = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(base, "flower/__init__.py")) as initf:
        for line in initf:
            m = version.match(line.strip())
            if not m:
                continue
            return ".".join(m.groups()[0].split(", "))


def get_requirements(filename):
    return open('requirements/' + filename).read().splitlines()


classes = """
    Development Status :: 4 - Beta
    Intended Audience :: Developers
    License :: OSI Approved :: BSD License
    Topic :: System :: Distributed Computing
    Programming Language :: Python
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3 :: Only
    Programming Language :: Python :: 3.6
    Programming Language :: Python :: 3.7
    Programming Language :: Python :: 3.8
    Programming Language :: Python :: 3.9
    Programming Language :: Python :: Implementation :: CPython
    Programming Language :: Python :: Implementation :: PyPy
    Operating System :: OS Independent
"""
classifiers = [s.strip() for s in classes.split('\n') if s]


setup(
    name='flower',
    version=get_package_version(),
    description='Functional Box Celery Flower',
    long_description=open('README.rst').read(),
    author='Functional Box LLC',
    author_email='nucleus@functionalbox.eu',
    url='https://functionalbox.com',
    license='BSD',
    classifiers=classifiers,
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=get_requirements('default.txt'),
    test_suite="tests",
    tests_require=get_requirements('test.txt'),
    package_data={'flower': ['templates/*', 'static/*.*',
                             'static/**/*.*', 'static/**/**/*.*']},
    entry_points={
        'celery.commands': [
            'flower = flower.command:flower',
        ],
    },
)
