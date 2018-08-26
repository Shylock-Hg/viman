import re

from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

LONG_DESCRIPTION = open('README.rst').read()

def find_version(file_path):
    with open(file_path) as f:
        version_file = f.read()
    version_match = re.search(
        r"^__version__\s*=\s*['\"]([^'\"]*)['\"]",
        version_file,
        re.M,
    )
    if version_match:
        return version_match.group(1)

    raise RuntimeError("Unable to find version string.")

setup(name='viman',
        version=find_version('viman/__init__.py'),
        description='The vim plugin manager based on git and pathogen!',
        long_description = LONG_DESCRIPTION,
        url='https://github.com/Shylock-Hg/viman.git',
        author='Shylock Hg',
        author_email='tcath2s@gmail.com',
        license='GPL-3.0',
        packages=['viman'],
        install_requires = ['pyyaml'],
        entry_points = {
            'console_scripts': ['viman=viman.viman:main'],
            },
        zip_safe=False)
