from setuptools import setup

setup(
    name='sqlite_benchmark',
    version='0.0.1',
    install_requires=[
        'flask',
        'flask_sqlalchemy',
        'sqlalchemy'
    ],
    packages=['sqlite_benchmark'],
    package_dir={
        'sqlite_benchmark': 'app'
    }
)
