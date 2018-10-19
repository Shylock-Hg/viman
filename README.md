# viman

[![Build Status](https://travis-ci.org/Shylock-Hg/viman.svg?branch=master)](https://travis-ci.org/Shylock-Hg/viman)
[![Pypi Status](https://img.shields.io/badge/pypi-v0.0.9-brightgreen.svg)](https://pypi.org/project/viman/)
[![codecov](https://codecov.io/gh/Shylock-Hg/viman/branch/master/graph/badge.svg)](https://codecov.io/gh/Shylock-Hg/viman)
[![CodeFactor](https://www.codefactor.io/repository/github/shylock-hg/viman/badge)](https://www.codefactor.io/repository/github/shylock-hg/viman)

Plugin manager of vim written by *python3* with *pacman* flavor usage.And viman based on [pathogen](https://github.com/tpope/vim-pathogen) and [git](https://github.com/git/git).

## installation

0. install vim.
1. install and configure [pathogen](https://github.com/tpope/vim-pathogen).
2. install [git](https://github.com/git/git).
3. install *viman* by `pip3 install --user viman`.

note:You can also perform these four steps by `export NATIVE_INSTALL='sudo pacman --noconfirm -Sy' && curl -sL https://raw.githubusercontent.com/Shylock-Hg/viman/master/install.sh | sh`. And please value you own `NATIVE_INSTALL` such as `yse | sudo apt-get install` if you don't use `pacman`.

## usage

- query help by `viman -h`
- install plugin by `viman -S https://github.com/altercation/vim-colors-solarized.git`.
- uninstall plugin by `viman -Rn vim-colors-solarized` or `viman -R https://github.com/altercation/vim-colors-solarized.git`.
- query all plugins installed by `viman -Q`.
- reduct all plugins from yml file by `viman -Sf <yml...>`

## feature

1. dependency management
2. plugin backup

