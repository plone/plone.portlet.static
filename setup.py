from setuptools import setup, find_packages
import os

version = '1.1.6'

setup(name='plone.portlet.static',
      version=version,
      description="A simple static HTML portlet for Plone 3",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone 3 portlet',
      author='Martin Aspeli',
      author_email='optilude@gmx.net',
      url='http://plone.org',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=["plone", 'plone.portlet'],
      include_package_data=True,
      zip_safe=False,
      extras_require=dict(
        test=[
            'Products.PloneTestCase',
        ]
      ),
      install_requires=[
          'setuptools',
          "plone.portlets",
          "plone.app.portlets",
          "plone.app.form>=1.1",
          "plone.i18n",
          'zope.component',
          'zope.formlib',
          'zope.i18nmessageid',
          'zope.interface',
          'zope.schema',
          # 'Zope2',
      ],
      )
