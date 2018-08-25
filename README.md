# viman

[![Build Status](https://travis-ci.org/Shylock-Hg/viman.svg?branch=master)](https://travis-ci.org/Shylock-Hg/viman)

Plugin manager of vim written by *python3* with *pacman* flavor usage.And viman based on [pathogen](https://github.com/tpope/vim-pathogen) and [git](https://github.com/git/git).

## installation

0. install vim.
1. install and configure [pathogen](https://github.com/tpope/vim-pathogen).
2. install [git](https://github.com/git/git).
3. install *viman* by `pip install viman`.

## usage

- install plugin by `viman -S https://github.com/altercation/vim-colors-solarized.git`.
- uninstall plugin by `viman -R vim-colors-solarized` or `viman -R https://github.com/altercation/vim-colors-solarized.git`.
- query all plugin installed by `viman -Qa`.

## feature

1. dependency management
2. plugin backup

