from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='pyramid_mongoengine',
      version=version,
      description="pyramid project with MongoDB and mongoengine",
      long_description=README,
      classifiers=[
          "Intended Audience :: Developers",
          "Framework :: Pyramid",
          "Programming Language :: Python",
          "License :: OSI Approved :: MIT License"
        ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='pyramid mongodb mongoengine',
      author='Ely Arzhannikov',
      author_email='iarzhannikov@gmail.com',
      url='',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
