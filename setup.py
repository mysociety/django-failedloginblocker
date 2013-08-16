from setuptools import setup

setup(
    name='django-failedloginblocker',
    version='1.0.0',
    packages=['failedloginblocker'],
    package_data={
        '': ['*.html'],
    },
    license=open('LICENSE').read(),
    long_description=open('README').read(),
    maintainer='mySociety',
    maintainer_email='programmers@mysociety.org',
    url='https://github.com/mysociety/django-failedloginblocker',
)
