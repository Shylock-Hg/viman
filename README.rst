viman
==========

.. image:: https://travis-ci.org/Shylock-Hg/viman.svg?branch=master
    :target: https://travis-ci.org/Shylock-Hg/viman

.. image:: https://img.shields.io/badge/pypi-v0.0.1-brightgreen.svg
    :target: https://pypi.org/project/viman/

Plugin manager of vim written by *python3* with *pacman* flavor usage.And viman based on `Pathogen <https://github.com/tpope/vim-pathogen>`_ and `Git <https://github.com/git/git>_ .

installation
------------------

0. install vim.
1. install and configure `Pathogen <https://github.com/tpope/vim-pathogen>_ .
2. install `Git <https://github.com/git/git>_ .
3. install *viman* by :sh:`pip install --user viman`.


usage
-----------------

* query usage of viman by :sh:`viman -h`.
* install plugin by :sh:`viman -S https://github.com/altercation/vim-colors-solarized.git`.
* uninstall plugin by :sh:`viman -Rn vim-colors-solarized` or :sh:`viman -R https://github.com/altercation/vim-colors-solarized.git`.
* query all plugins installed by :sh:`viman -Q`.
* reduct all plugins from yml file by :sh:`viman -Sf <yml...>`.

feature
--------------------

* dependency management
* plugin backup

