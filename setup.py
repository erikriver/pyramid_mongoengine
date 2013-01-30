from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, "README")).read()
README = README.split("\n\n", 1)[0] + "\n"

version = '0.2'

requires = [
            'pyramid',
            'mongoengine',
        ]

entry_points = """
    [paste.paster_create_template]
    pyramid_mongoengine = pyramid_mongoengine.paster_template:MongoengineProjectTemplate
    [pyramid.scaffold]
    mongoengine = pyramid_mongoengine.paster_template:MongoengineProjectTemplate
"""

setup(name='pyramid_mongoengine',
      version=version,
      description="pyramid project with MongoDB and mongoengine",
      long_description=README,
      classifiers=[
          "Intended Audience :: Developers",
          "Framework :: Pylons",
          "Programming Language :: Python",
          "License :: OSI Approved :: MIT License"
        ],
      keywords='pyramid mongodb mongoengine web wsgi',
      author='Ely Arzhannikov',
      author_email='iarzhannikov@gmail.com',
      url='https://github.com/xandox/pyramid_mongoengine',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      test_suite="pyramid_mongoengine",
      entry_points=entry_points,
      )
