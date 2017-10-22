"""."""

from setuptools import setup

setup(

    name='trigrams',
    description='Tom Swift Under Milk Wood',
    package_dir={'': 'src'},
    author='Robert Bronson and Darren Haynes',
    author_email='robert.j.bronson@gmail.com, darrenHaynes@zoho.com',
    py_modules=['trigrams'],
    install_requires=[],
    extras_require={
        'testing': ['pytest', 'pytest-cov', 'tox'],
        'development': ['ipython']
    },
    entry_points={}

)
