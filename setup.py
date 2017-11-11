#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='scott-secret-sauce',
      version='4.3.0',
      description='scotts python secret sauce',
      author='scotthaleen',
      author_email='scotthaleen@users.noreply.github.com',
      url='https://github.com/scotthaleen/python-secret-sauce',
      include_package_data=True,
      packages=find_packages(exclude=("tests",)),
      data_files=[('', ['LICENSE'])],
      extras_require={},
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Libraries',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7'
      ])
