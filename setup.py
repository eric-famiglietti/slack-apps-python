from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='slack-apps-python',
    version='0.0.0.dev1',
    description='Python module for scraping the Slack App Directory.',
    long_description=long_description,
    url='https://github.com/eric-famiglietti/slack-apps-python',
    author='Eric Famiglietti',
    author_email='eric.famiglietti@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='slack scraper',
    py_modules=['app_directory'],
    install_requires=['beautifulsoup4', 'requests'],
    extras_require={
        'test': ['responses'],
    },
)
