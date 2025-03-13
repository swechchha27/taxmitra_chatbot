"""
Setup configuration for the self-learning-chatbot project.

This module uses setuptools to package the self-learning-chatbot project.
It specifies the project metadata, dependencies, and entry points.
"""

from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='TaxMitra_Chatbot',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],  # Dependencies moved to pyproject.toml
    entry_points={
        'console_scripts': [
            'chatbot=main',
        ],
    },
    author='Swechchha Agarwal',
    author_email='swechchhagoyal27@gmail.com',
    description='A simple domain-specific chatbot for income tax guidance in India.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/swechchha27/taxmitra_chatbot',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='<=3.7',
)
