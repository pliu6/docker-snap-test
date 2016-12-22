from setuptools import setup, find_packages

setup(
    name="docker-test",
    version="0.0.1",
    author="Peng Liu",
    license="GPL",
    packages=find_packages(),
    install_requires=[
        'docker-py==1.10.6'
    ],

    entry_points={
        'console_scripts': [
            'dockertest = dockertest:main'
        ]
    },

    include_package_data = True
)
