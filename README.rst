viman
==========

Plugin manager of vim written by *python3* with *pacman* flavor usage.And viman based on .. _a pathogen: https://github.com/tpope/vim-pathogen and .. _a git: https://github.com/git/git.

installation
------------------

0. install vim.
1. install and configure .. _a pathogen: https://github.com/tpope/vim-pathogen.
2. install .. _a git: https://github.com/git/git.
3. install *viman* by `pip install viman`.


usage
-----------------

* install plugin by `viman -S https://github.com/altercation/vim-colors-solarized.git`.
* uninstall plugin by `viman -R vim-colors-solarized` or `viman -R https://github.com/altercation/vim-colors-solarized.git`.
* query all plugin installed by `viman -Qa`.

feature
--------------------

* dependency management
* plugin backup

