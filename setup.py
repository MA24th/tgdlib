#!/usr/bin/env python3
from setuptools import setup, find_packages
from io import open


def read(filename):
    with open(filename, encoding='utf-8') as file:
        return file.read()


setup(name='tgdlib',
      version='1.0.0',
      description='The Powerful Telegram tdlib Client Framework',
      long_description=read('README.rst'),
      long_description_content_type="text/x-rst",
      author='Mustafa Asaad',
      author_email='ma24th@yahoo.com',
      url='https://github.com/MA24th/tgdlib',
      packages=find_packages(),
      license='GNU GPLv2',
      keywords='telegram-tdlib, tdlib, framework, tgdlib',
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: 3.7',
                   'Programming Language :: Python :: 3.8',
                   'Environment :: Console',
                   'License :: OSI Approved :: GNU General Public License v2 (GPLv2)']
      )
