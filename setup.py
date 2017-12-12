from setuptools import setup, find_packages

setup(
    name='pebble-view-helpers',
    version='0.0.10',
    description="Set of helpers to make working with, and testing, generic views easier",
    author="SF Software limited t/a Pebble",
    author_email="sysadmin@mypebble.co.uk",
    url="https://github.com/mypebble/view-helpers",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'python-dateutil>=1.5',
    ],
)
