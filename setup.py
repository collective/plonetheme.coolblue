from setuptools import setup, find_packages

setup(
    name='plonetheme.coolblue',
    version='0.1.0',
    author='Alex Clark',
    author_email='aclark@aclark.net',
    url='https://github.com/aclark4life/plonetheme.coolblue',
    packages=find_packages(),
    namespace_packages=[
        'plonetheme'
    ],
    install_requires=[
        'plone.app.theming',
        'z3c.jbot',
    ],
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    entry_points={
        'z3c.autoinclude.plugin': 'target = plone',
    },
)
