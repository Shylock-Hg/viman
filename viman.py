#! /usr/bin/env python3

import argparse
import sys
import subprocess
import os
import errno

import vimanArgParser
from vimanGitWrapper import vimanGitWrapper

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
        vimanGitWrapper.install(args.synchronize)

    elif args.remove :
        vimanGitWrapper.remove(args.remove)
    elif args.upgrade:
        vimanGitWrapper.upgrade(args.upgrade)
    '''
    parser = vimanArgParser.vimanArgParser(sys.argv[1:])
    print(parser.operations)
    print(parser.options)
    print(parser.targets)
    #gitWrapper = vimanGitWrapper()
    if parser.operations[0] in vimanArgParser.vimanOperations.operations['sync'][0]:
        if vimanArgParser.vimanOptions.options['file'][0] in parser.options:
            for f in parser.targets:
                vimanGitWrapper.installByYml(f)
        else:
            for target in parser.targets:
                vimanGitWrapper.install(target)

    elif parser.operations[0] in vimanArgParser.vimanOperations.operations['remove'][0]:
        for target in parser.targets:
            vimanGitWrapper.remove(target)
            #gitWrapper.remove(target)
    elif parser.operations[0] in vimanArgParser.vimanOperations.operations['upgrade'][0]:
        for target in parser.targets:
            vimanGitWrapper.upgrade(target)
    elif parser.operations[0] in vimanArgParser.vimanOperations.operations['query'][0]:
        pass
    elif parser.operations[0] in vimanArgParser.vimanOperations.operations['version'][0]:
        pass
    elif parser.operations[0] in vimanArgParser.vimanOperations.operations['help'][0]:
        pass
    else:
        print('error:invalid operation `{}`!'.format(parser.operations[0]), file=sys.stderr)
        return errno.EINVAL

    return 0




if '__main__' == __name__:
    sys.exit(main())

