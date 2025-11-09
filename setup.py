from pathlib import Path
from setuptools import find_packages
from setuptools import setup


version = "5.0.0.dev0"

long_description = f"{Path('README.rst').read_text()}\n{Path('CHANGES.rst')}\n"


setup(
    name="plone.portlet.static",
    version=version,
    description="An editable static HTML portlet for Plone.",
    long_description=long_description,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: Core",
        "Framework :: Zope :: 5",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="plone portlet static",
    author="Plone Foundation",
    author_email="plone-developers@lists.sourceforge.net",
    url="https://pypi.org/project/plone.portlet.static",
    license="GPL version 2",
    packages=find_packages("src"),
    package_dir={"": "src"},
    namespace_packages=["plone", "plone.portlet"],
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.8",
    extras_require=dict(
        test=[
            "plone.app.testing",
        ]
    ),
    install_requires=[
        "setuptools",
        "plone.base",
        "plone.portlets",
        "plone.app.portlets",
        "plone.app.textfield",
        "plone.app.z3cform",
        "plone.autoform",
        "plone.i18n",
        "Products.GenericSetup",
        "Zope",
    ],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
