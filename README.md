# viman

|Pypi|CI|Coverage|Lint|Project|PR|
|:--|:--|:--|:--|:--|:--|
|[![Pypi Status](https://img.shields.io/badge/pypi-v0.0.12-brightgreen.svg)](https://pypi.org/project/viman/)|[![Build Status](https://travis-ci.org/Shylock-Hg/viman.svg?branch=master)](https://travis-ci.org/Shylock-Hg/viman)|[![codecov](https://codecov.io/gh/Shylock-Hg/viman/branch/master/graph/badge.svg)](https://codecov.io/gh/Shylock-Hg/viman)|[![CodeFactor](https://www.codefactor.io/repository/github/shylock-hg/viman/badge)](https://www.codefactor.io/repository/github/shylock-hg/viman)|[![BCH compliance](https://bettercodehub.com/edge/badge/Shylock-Hg/viman?branch=master)](https://bettercodehub.com/)|[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)|
||||[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/Shylock-Hg/viman.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/Shylock-Hg/viman/context:python)|||
||||[![Codacy Badge](https://api.codacy.com/project/badge/Grade/4bc646603b0847d2aee5c7527a35c8e6)](https://www.codacy.com/app/Shylock-Hg/viman?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Shylock-Hg/viman&amp;utm_campaign=Badge_Grade)|||

Plugin manager of vim written by *python3* with *pacman* flavor usage.And viman based on [pathogen](https://github.com/tpope/vim-pathogen) and [git](https://github.com/git/git).

## installation

1.  install vim.
2.  install and configure [pathogen](https://github.com/tpope/vim-pathogen).
3.  install *viman* by `pip3 install --user viman`.

note:You can also perform these three steps by `export NATIVE_INSTALL='sudo pacman --noconfirm -Sy' && curl -sL https://raw.githubusercontent.com/Shylock-Hg/viman/master/install.sh | sh`. And please value you own `NATIVE_INSTALL` such as `yse | sudo apt-get install` if you don't use `pacman`.

## usage

-   query help by `viman -h`
-   install plugin by `viman -S https://github.com/altercation/vim-colors-solarized.git`.
-   uninstall plugin by `viman -Rn vim-colors-solarized` or `viman -R https://github.com/altercation/vim-colors-solarized.git`.
-   query all plugins installed by `viman -Q`.
-   reduct all plugins from yml file by `viman -Sf <yml...>`

## feature

1.  dependency management
2.  plugin backup
