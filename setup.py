from setuptools import setup, find_packages

setup(
    name='django-failedloginblocker',
    version='1.0.0',
    packages=find_packages(),
    package_data={
        '': ['*.html'],
    },
    license=open('LICENSE').read(),
    long_description=open('README').read(),
    maintainer='mySociety',
    maintainer_email='programmers@mysociety.org',
    url='https://github.com/mysociety/django-failedloginblocker',
)
