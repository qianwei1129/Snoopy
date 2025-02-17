#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='WYLQ',
    version='1.0.0',
    description=(
        '用于计算指定开始日期条件下的五运六气'
    ),
    long_description=open('README.rst').read(),
    author='Shen Tianwei',
    author_email='2990834217@qq.com',
    maintainer='Carrie-HYY',
    maintainer_email='2833972093@qq.com',
    license='BSD License',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/Carrie-HuYY/WYLQ',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
)

install_requires=[
    'ephem == 4.1.6',
    'sxtwl == 2.0.7',
    ]