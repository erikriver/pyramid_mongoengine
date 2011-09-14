from setuptools import setup, find_packages
import sys, os

version = '0.1'

requires = [
            'pyramid',
            'mongoengine',
        ]
entry_points = """
    [paster.paster_create_template]
    pyramid_mongoengine = pyramid_mongoengine.paster_template:MongoengineProjectTemplate
"""

setup(name='pyramid_mongoengine',
      version=version,
      description="pyramid project with MongoDB and mongoengine",
      long_description=README,
      classifiers=[
          "Intended Audience :: Developers",
          "Framework :: Pyramid",
          "Programming Language :: Python",
          "License :: OSI Approved :: MIT License"
        ],
      keywords='pyramid mongodb mongoengine web wsgi',
      author='Ely Arzhannikov',
      author_email='iarzhannikov@gmail.com',
      url='https://github.com/xandox/pyramid_mongoengine',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      entry_points=entry_points,
      )
