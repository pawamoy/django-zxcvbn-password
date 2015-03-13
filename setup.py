#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from distutils.core import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-zxcvbn-password',
    version='1.0.3.0',
    packages=['zxcvbn_password'],
    package_data={'': '*.js'},
    include_package_data=True,
    license='BSD License',

    author='Timothée Mazzucotelli',
    author_email='timothee.mazzucotelli@gmail.com',
    url='https://github.com/Pawamoy/django-zxcvbn-password',
    # download_url = 'https://github.com/Pawamoy/django-zxcvbn-password/tarball/1.0.2',

    keywords="password validation front back zxcvbn confirmation field",
    description="A front-end and back-end password validation field using ZXCVBN.",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: BSD License",
    ]
)
