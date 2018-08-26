#! /usr/bin/env python3

import argparse
import sys
import subprocess
import os
import errno

from viman import vimanArgParser
from viman import vimanGitWrapper
from viman import vimanYamlWrapper
from viman.__init__ import __version__
from viman.__init__ import __program__

PROGRAM = __program__
VERSION = __version__

#errno = ['OK',                          #0
        #'~/.vim/bundle don\'t exists!'] #1
'''
class vimanArgParser(argparse.ArgumentParser):
    def __init__(self,*args,**kwargs):
        super().__init__(...)
        # base option
        # Synchronize and option
        self.add_argument('-S','--synchronize',help='Synchronize plugin!')
        self.add_argument('-u','--sysupgrade',action='store_true',help='Upgrade all plugin!')

        #Remove and option
        self.add_argument('-R','--remove',help='Remove plugin!')

        #Upgrade and option
        self.add_argument('-U','--upgrade',help='Upgrade local plugin!')

        #Query and option
        self.add_argument('-Q','--query',help='Query local plugin!')

        #Version
        self.add_argument('-V','--version',action='version',version='%(prog)s 0.0.1')
'''


def main():
    #parse argumenits
    #argparser = vimanArgParser(prog='viman')
    #args = argparser.parse_args()
    '''
    if args.synchronize :
        vimanGitWrapper.vimanGitWrapper.install(args.synchronize)

    elif args.remove :
        vimanGitWrapper.vimanGitWrapper.remove(args.remove)
    elif args.upgrade:
        vimanGitWrapper.vimanGitWrapper.upgrade(args.upgrade)
    '''
    parser = vimanArgParser.vimanArgParser(sys.argv[1:])
    #print(parser.operations)
    #print(parser.options)
    #print(parser.targets)

    if parser.operations[0] == vimanArgParser.vimanOperations.operations['sync'][0]:
        # sync
        if vimanArgParser.vimanOptions.options['file'][0] in parser.options:
            # yml file
            for f in parser.targets:
                vimanGitWrapper.vimanGitWrapper.installByYml(f)
        elif vimanArgParser.vimanOptions.options['current'][0] in parser.options:
            # current yml string
            for yml in parser.targets:
                vimanGitWrapper.vimanGitWrapper.installByCurrent(yml)
        elif vimanArgParser.vimanOptions.options['sysupgrade'][0] in parser.options:
            # sysupgrade
            vimanGitWrapper.vimanGitWrapper.upgradeByYml(vimanYamlWrapper.vimanYamlWrapper.ymlDefault)

        else:
            for target in parser.targets:
                vimanGitWrapper.vimanGitWrapper.install(target, '')

    elif parser.operations[0] == vimanArgParser.vimanOperations.operations['remove'][0]:
        if vimanArgParser.vimanOptions.options['file'][0] in parser.options:
            for f in parser.targets:
                vimanGitWrapper.vimanGitWrapper.removeByYml(f)
        elif vimanArgParser.vimanOptions.options['name'][0] in parser.options:
            for name in parser.targets:
                vimanGitWrapper.vimanGitWrapper.removeByName(name)

        else:
            for target in parser.targets:
                vimanGitWrapper.vimanGitWrapper.remove(target)

    elif parser.operations[0] == vimanArgParser.vimanOperations.operations['upgrade'][0]:
        if vimanArgParser.vimanOptions.options['file'][0] in parser.options:
            # upgrade by yml file
            for f in parser.targets:
                vimanGitWrapper.vimanGitWrapper.upgradeByYml(f)
        elif vimanArgParser.vimanOptions.options['recursive'][0] in parser.options:
            # upgrade recursive
            vimanGitWrapper.vimanGitWrapper.upgradeByYml(vimanYamlWrapper.vimanYamlWrapper.ymlDefault)
        for target in parser.targets:
            vimanGitWrapper.vimanGitWrapper.upgrade(target)
    elif parser.operations[0] == vimanArgParser.vimanOperations.operations['query'][0]:
        yml = vimanYamlWrapper.vimanYamlWrapper.loadYml()
        if None == yml:
            print(yml)
        else:
            for name in yml:
                print(name)
    elif parser.operations[0] == vimanArgParser.vimanOperations.operations['version'][0]:
        print('{}-{}'.format(PROGRAM,VERSION))
    elif parser.operations[0] == vimanArgParser.vimanOperations.operations['help'][0]:
        vimanArgParser.vimanArgParser.printUsage()
        #parser.printUsage()
    else:
        print('error:invalid operation `{}`!'.format(parser.operations[0]),
                file=sys.stderr)
        return errno.EINVAL

    return 0

if '__main__' == __name__:
    sys.exit(main())

