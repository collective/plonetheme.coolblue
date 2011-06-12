from setuptools import setup, find_packages
import os

setup(
    name='plonetheme.coolblue',
    description='An installable Diazo theme for Plone 4.1',
    long_description=open("README.rst").read() + "\n" +
        open(os.path.join("docs", "HISTORY.txt")).read(),
    version='0.1.1',
    author='Alex Clark',
    author_email='aclark@aclark.net',
    url='https://github.com/collective/plonetheme.coolblue',
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
