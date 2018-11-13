viman
==========

.. image:: https://travis-ci.org/Shylock-Hg/viman.svg?branch=master
    :target: https://travis-ci.org/Shylock-Hg/viman

.. image:: https://img.shields.io/badge/pypi-v0.0.9-brightgreen.svg
    :target: https://pypi.org/project/viman/

.. image:: https://codecov.io/gh/Shylock-Hg/viman/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/Shylock-Hg/viman

.. image:: https://www.codefactor.io/repository/github/shylock-hg/viman/badge
   :target: https://www.codefactor.io/repository/github/shylock-hg/viman
   :alt: CodeFactor

.. image:: https://img.shields.io/lgtm/grade/python/g/Shylock-Hg/viman.svg?logo=lgtm&logoWidth=18
   :target: https://lgtm.com/projects/g/Shylock-Hg/viman/context:python
   :alt: Language grade: Python

.. image:: https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square
   :target: http://makeapullrequest.com


Plugin manager of vim written by *python3* with *pacman* flavor usage.And viman based on `Pathogen <https://github.com/tpope/vim-pathogen>`_ and `Git <https://github.com/git/git>`_ .

installation
------------------

0. install vim.
1. install and configure `Pathogen <https://github.com/tpope/vim-pathogen>`_ .
2. install `Git <https://github.com/git/git>`_ .
3. install *viman* by ``pip3 install --user viman``.

note:You can also perform these four steps by ``export NATIVE_INSTALL='sudo pacman --noconfirm -Sy' && curl -sL https://raw.githubusercontent.com/Shylock-Hg/viman/master/install.sh | sh``. And please value you own *NATIVE_INSTALL* such as ``yes | sudo apt-get install`` if you don't use *pacman*.

usage
-----------------

* query usage of viman by ``viman -h``.
* install plugin by ``viman -S https://github.com/altercation/vim-colors-solarized.git ...``.
* uninstall plugin by ``viman -Rn vim-colors-solarized ...`` or ``viman -R https://github.com/altercation/vim-colors-solarized.git ...``.
* query all plugins installed by ``viman -Q``.
* reduct all plugins from yml file by ``viman -Sf <yml ...>``.

feature
--------------------

* dependency management
* plugin backup

