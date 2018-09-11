'''
@brief setup for packing
'''

import re

from setuptools import setup


def readme():
    '''
    @brief read content from README
    @retval content string of README
    '''
    with open('README.rst') as f:
        return f.read()


LONG_DESCRIPTION = open('README.rst').read()

def find_attr(attr, file_path):
    '''
    @brief find attribute from documents by regex
    @param attr attribute name string
    @param file path string
    @retval attribute value
    '''
    with open(file_path) as f:
        attr_file = f.read()
    attr_match = re.search(
        r"^{}\s*=\s*['\"]([^'\"]*)['\"]".format(attr),
        attr_file,
        re.M)

    if attr_match:
        return attr_match.group(1)

    raise RuntimeError("Unable to find {} string.".format(attr))


setup(
    name=find_attr('__program__', 'viman/__init__.py'),
    version=find_attr('__version__', 'viman/__init__.py'),
    description='The vim plugin manager based on git and pathogen!',
    long_description=LONG_DESCRIPTION,
    url='https://github.com/Shylock-Hg/viman.git',
    author='Shylock Hg',
    author_email='tcath2s@gmail.com',
    license='GPL-3.0',
    packages=['viman'],
    install_requires=['pyyaml'],
    python_requires='>=3.3',
    entry_points={
        'console_scripts': ['viman=viman.vimanApp:main'],
        },
    zip_safe=False)
