from setuptools import setup, find_packages
import os

version = '0.2'

setup(name='nuwcommunity.theme',
      version=version,
      description="NUW Community Diazo theme based on Twitter's Bootstrap CSS",
      long_description='',
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='plone diazo theme',
      author='',
      author_email='',
      url='',
      license='Apache License 2.0',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['nuwcommunity'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
