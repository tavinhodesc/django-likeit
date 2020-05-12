#!/usr/bin/env python

from setuptools import setup, find_packages

try:
    import pypandoc
    README = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    README = open('README.md').read()

setup(
    name='django-likeit-ptbr',
    version='0.1.2',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description=README[2].rstrip('\n'),
    long_description=''.join(README),
    url='https://github.com/gustavodesc/django-likeit-ptbr',
    download_url='https://github.com/gustavodesc/django-likeit-ptbr/tarball/0.1',
    author='Gustavo Guella',
    author_email='gustavodesc@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
    )
