from setuptools import setup, find_packages

setup(
    name='jformat',
    version='0.1',
    description='Reformat any file or input into JSON',
    author='Alfredo Deza',
    author_email='alfredo@deza.pe',
    test_suite='jformat',
    scripts=['bin/jformat'],
    zip_safe=False,
    include_package_data=True,
    packages=find_packages()
)
