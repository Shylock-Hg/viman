viman
==========

.. image:: https://travis-ci.org/Shylock-Hg/viman.svg?branch=master
    :target: https://travis-ci.org/Shylock-Hg/viman

.. image:: https://img.shields.io/badge/pypi-v0.0.1-brightgreen.svg
    :target: https://pypi.org/project/viman/

Plugin manager of vim written by *python3* with *pacman* flavor usage.And viman based on .. _pathogen: https://github.com/tpope/vim-pathogen and .. _git: https://github.com/git/git.

installation
------------------

0. install vim.
1. install and configure .. _pathogen: https://github.com/tpope/vim-pathogen.
2. install .. _git: https://github.com/git/git.
3. install *viman* by :bash:`pip install viman`.


usage
-----------------

* install plugin by :bash:`viman -S https://github.com/altercation/vim-colors-solarized.git`.
* uninstall plugin by :bash:`viman -R vim-colors-solarized` or :bash:`viman -R https://github.com/altercation/vim-colors-solarized.git`.
* query all plugin installed by :bash:`viman -Qa`.

feature
--------------------

* dependency management
* plugin backup

