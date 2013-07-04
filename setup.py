from setuptools import setup, find_packages

setup(
    name='pebble-view-helpers',
    version='0.0.1',
    description="",
    author="SF Software limited t/a Pebble",
    author_email="sdev@talktopebble.co.uk",
    url="https://bitbucket.org/pebble/pebble-view-helpers",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'python-dateutil>=1.5',
    ],
)
