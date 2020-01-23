#!/usr/bin/env python

import setuptools

import plink_remove_dups.release

install_requires = [
]

setuptools.setup(
    name='plink_remove_dups',
    url='https://github.com/j2moreno/plink_remove_dups',
    version=plink_remove_dups.release.__version__,
    description='Tool that helps remove duplicates inside of plink binary files',
    author='Leonardo Moreno',
    author_email='leo.moreno@epi.usf.edu',
    packages=[
        'plink_remove_dups',
    ],
    entry_points={
        'console_scripts': [
            'plink_remove_dups = plink_remove_dups.cli:main',
        ]
    },
    install_requires=install_requires
)
