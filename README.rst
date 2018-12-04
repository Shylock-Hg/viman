viman
==========

+------------+------------+-----------+-----------------+---------------+---------------+
|    Pypi    |     CI     | Coverage  |      Lint       |   Project     |      PR       |
+============+============+===========+=================+===============+===============+
|   |Pypi|   |  |travis|  | |codecov| | |codefactor|    |     |BCH|     | |PR-welcomes| |
+------------+------------+-----------+-----------------+---------------+---------------+
|            |            |           | |lgtm-lint|     |               |               |
+------------+------------+-----------+-----------------+---------------+---------------+
|            |            |           | |Codacy Badge|  |               |               |
+------------+------------+-----------+-----------------+---------------+---------------+

.. |travis| image:: https://travis-ci.org/Shylock-Hg/viman.svg?branch=master
    :target: https://travis-ci.org/Shylock-Hg/viman

.. |Pypi| image:: https://img.shields.io/badge/pypi-v0.0.12-brightgreen.svg
    :target: https://pypi.org/project/viman/

.. |codecov| image:: https://codecov.io/gh/Shylock-Hg/viman/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/Shylock-Hg/viman

.. |codefactor| image:: https://www.codefactor.io/repository/github/shylock-hg/viman/badge
   :target: https://www.codefactor.io/repository/github/shylock-hg/viman
   :alt: CodeFactor

.. |lgtm-lint| image:: https://img.shields.io/lgtm/grade/python/g/Shylock-Hg/viman.svg?logo=lgtm&logoWidth=18
   :target: https://lgtm.com/projects/g/Shylock-Hg/viman/context:python
   :alt: Language grade: Python

.. |Codacy Badge| image:: https://api.codacy.com/project/badge/Grade/4bc646603b0847d2aee5c7527a35c8e6
   :target: https://www.codacy.com/app/Shylock-Hg/viman?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Shylock-Hg/viman&amp;utm_campaign=Badge_Grade)

.. |BCH| image:: https://bettercodehub.com/edge/badge/Shylock-Hg/viman?branch=master
   :target: https://bettercodehub.com/

.. |PR-welcomes| image:: https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square
   :target: http://makeapullrequest.com


Plugin manager of vim written by *python3* with *pacman* flavor usage.And viman based on `Pathogen <https://github.com/tpope/vim-pathogen>`_ and `Git <https://github.com/git/git>`_ .

installation
------------------

1. install vim.
2. install and configure `Pathogen <https://github.com/tpope/vim-pathogen>`_ .
3. install *viman* by ``pip3 install --user viman``.

note:You can also perform these three steps by ``export NATIVE_INSTALL='sudo pacman --noconfirm -Sy' && curl -sL https://raw.githubusercontent.com/Shylock-Hg/viman/master/install.sh | sh``. And please value you own *NATIVE_INSTALL* such as ``yes | sudo apt-get install`` if you don't use *pacman*.

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

