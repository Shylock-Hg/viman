from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='viman',
        version='0.0.1',
        description='The vim plugin manager based on git and pathogen!',
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
