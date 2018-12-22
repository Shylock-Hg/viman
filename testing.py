#! /usr/bin/env python3

'''
@brief
@author Shylock Hg
@date 2018-12-04
@email tcath2s@gmail.com
'''

import unittest
import os

from viman import vimanApp

class cli_tests(unittest.TestCase):
    argv_set = [
        ['viman', '-h'],
        ['viman', '-V'],
        ['viman', '-Q'],
        ['viman', '-Sf', 'test.yml'],
        ['viman', '-S', 'https://github.com/vimscript/vim-snippets.git'],
        ['viman', '-Ur'],
        ['viman', '-R', 'https://github.com/vimscript/vim-snippets.git'],
        ['viman', '-Rn', 'nerdtree'],
        ['viman', '-Rf', os.path.join(os.path.expanduser('~'), '.viman.yml')],
    ]

    def test_cli(self):
        for argv in cli_tests.argv_set:
            self.assertEqual(vimanApp.main(argv), 0)


if __name__ == '__main__':
    unittest.main()
