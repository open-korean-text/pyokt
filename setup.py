from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))


setup(
    name='pyokt',
    version='0.1.2',
    description='open-korean-text wrapper for python',

    url='https://github.com/cookieshake/pyokt',

    author='cookieshake',
    author_email='cookieshake@github.com',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
    ],

    # What does your project relate to?
    keywords='open-korean-text korean text tokenize',
    packages=['pyokt'],
    install_requires=['jpype1'],
)