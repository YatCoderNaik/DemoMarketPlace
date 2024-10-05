
from setuptools import setup, find_packages

setup(
    name='MarketplaceProject',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'prettytable',
    ],
    entry_points={
        'console_scripts': [
            'marketplace = main:main',  # Assuming main.py has a main function
        ],
    },
)
