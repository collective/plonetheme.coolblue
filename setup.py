from setuptools import setup, find_packages
import os

setup(
    name='plonetheme.coolblue',
    description='An installable Diazo theme for Plone 4.1',
    long_description=open('README.rst', 'rb').read(),
    version='0.1.0',
    author='Alex Clark',
    author_email='aclark@aclark.net',
    url='https://github.com/aclark4life/plonetheme.coolblue',
    packages=find_packages(),
    include_package_data=True,
    namespace_packages=[
        'plonetheme'
    ],
    install_requires=[
        'setuptools',
        'plone.app.theming',
    ],
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    entry_points={
        'z3c.autoinclude.plugin': 'target = plone',
    }
)
