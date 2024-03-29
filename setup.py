from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='cms.policy',
      version=version,
      description="Chinese medical science AI system policy.",
      long_description=open("README.md").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['cms'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.CMFPlone',
          'collective.monkeypatcher',
          'collective.autopermission',
          'cms.db',
          'cms.theme',
          # -*- Extra requirements: -*-
      ],
      extras_require={
    'test': ['plone.app.testing',]
        },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
