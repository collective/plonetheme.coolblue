from setuptools import setup, find_packages

setup(
    name='plonetheme.coolblue',
    packages=find_packages(),
    namespace_packages=['plonetheme'],
    install_requires=[
        'plone.app.theming',
        'z3c.jbot',
    ],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)