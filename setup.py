"""Setup config.
"""
from os import path
from setuptools import setup, find_packages


CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.5',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Framework :: Django',
]


README_FILE = path.join(path.dirname(path.abspath(__file__)), 'README.md')

try:
    import m2r
    LONG_DESCRIPTION = m2r.parse_from_file(README_FILE)
except Exception:
    LONG_DESCRIPTION = ''


setup(
    name='pebble-view-helpers',
    version='0.1.0',
    description="Set of helpers to make working with, and testing, generic views easier",
    author="SF Software limited t/a Pebble",
    author_email="sysadmin@mypebble.co.uk",
    url="https://github.com/mypebble/view-helpers",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'python-dateutil>=1.5',
        'django>=1.11',
    ],
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
)
