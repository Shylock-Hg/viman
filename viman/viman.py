#! /usr/bin/env python3

'''
@biref viman cli entry
'''

import sys
import errno

from viman import vimanArgParser
from viman import vimanGitWrapper
from viman import vimanYamlWrapper
from viman.__init__ import __version__
from viman.__init__ import __program__

PROGRAM = __program__
VERSION = __version__

# errno = ['OK',                          #0
# '~/.vim/bundle don\'t exists!'] #1


def main():
    '''
    @brief viman for vim plugins manager
    @return error
    '''

    parser = vimanArgParser.vimanArgParser(sys.argv[1:])
    # print(parser.operations)
    # print(parser.options)
    # print(parser.targets)

    if parser.operations[0] == vimanArgParser.vimanOperations.\
            operations['sync'][0]:
        # sync
        if vimanArgParser.vimanOptions.options['file'][0] in parser.options:
            # yml file
            for yml_file in parser.targets:
                vimanGitWrapper.vimanGitWrapper.installByYml(yml_file)
        elif vimanArgParser.vimanOptions.options['current'][0] in \
                parser.options:
            # current yml string
            for yml in parser.targets:
                vimanGitWrapper.vimanGitWrapper.installByCurrent(yml)
        elif vimanArgParser.vimanOptions.options['sysupgrade'][0] in \
                parser.options:
            # sysupgrade
            vimanGitWrapper.vimanGitWrapper.upgradeByYml(
                vimanYamlWrapper.vimanYamlWrapper.ymlDefault)

        else:
            for target in parser.targets:
                vimanGitWrapper.vimanGitWrapper.install(target, '')

    elif parser.operations[0] == vimanArgParser.vimanOperations.\
            operations['remove'][0]:
        if vimanArgParser.vimanOptions.options['file'][0] in parser.options:
            # yml file
            for yml_file in parser.targets:
                vimanGitWrapper.vimanGitWrapper.removeByYml(yml_file)
        elif vimanArgParser.vimanOptions.options['name'][0] in parser.options:
            for name in parser.targets:
                vimanGitWrapper.vimanGitWrapper.removeByName(name)

        else:
            for target in parser.targets:
                vimanGitWrapper.vimanGitWrapper.remove(target)

    elif parser.operations[0] == vimanArgParser.vimanOperations.\
            operations['upgrade'][0]:
        if vimanArgParser.vimanOptions.options['file'][0] in parser.options:
            # upgrade by yml file
            for yml_file in parser.targets:
                vimanGitWrapper.vimanGitWrapper.upgradeByYml(yml_file)
        elif vimanArgParser.vimanOptions.options['recursive'][0] in \
                parser.options:
            # upgrade recursive
            vimanGitWrapper.vimanGitWrapper.upgradeByYml(
                vimanYamlWrapper.vimanYamlWrapper.ymlDefault)
        for target in parser.targets:
            vimanGitWrapper.vimanGitWrapper.upgrade(target)
    elif parser.operations[0] == vimanArgParser.vimanOperations.\
            operations['query'][0]:
        yml = vimanYamlWrapper.vimanYamlWrapper.loadYml()
        if yml is None:
            print(yml)
        else:
            for name in yml:
                print(name)
    elif parser.operations[0] == vimanArgParser.vimanOperations.\
            operations['version'][0]:
        print('{}-{}'.format(PROGRAM, VERSION))
    elif parser.operations[0] == vimanArgParser.vimanOperations.\
            operations['help'][0]:
        # help
        vimanArgParser.vimanArgParser.printUsage()
    else:
        # invalid operation
        print('error:invalid operation `{}`!'.format(parser.operations[0]),
              file=sys.stderr)
        return errno.EINVAL

    return 0

if '__main__' == __name__:
    sys.exit(main())
