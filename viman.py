#! /usr/bin/env python3

import argparse
import sys
import subprocess
import os
import errno

import yaml

import vimanArgParser

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

class vimanGitWrapper():
    '''
    @brief low operation wrapper of git , install , upgrade , remove , query 
    @note all other operation base on this
    '''

    DIR_PLUGIN = os.path.join(os.getenv('HOME'),'.vim/bundle')

    @staticmethod
    def install(url):
        '''
        @brief install a vim plugin to .vim/bundle by git from url
        @param url url of git repository
        '''
        if not os.path.isdir(vimanGitWrapper.DIR_PLUGIN):
            sys.exit(errno.ENOENT)
        os.chdir(vimanGitWrapper.DIR_PLUGIN)
        #sys.exit(subprocess.run(['git','clone',url]))
        return subprocess.run(['git','clone',url])

    @staticmethod
    def upgrade(url):
        '''
        @brief upgrade a vim plugin by git from url
        @param url url of git repository
        '''
        return vimanGitWrapper.upgradeByName(vimanGitWrapper.getPlugin4Url(url))
        
    @staticmethod
    def upgradeByName(name):
        path = os.path.join(vimanGitWrapper.DIR_PLUGIN,name)
        if not os.path.isdir(path):
            sys.exit(errno.ENOENT)
        os.chdir(path)
        #sys.exit(subprocess.run(['git','pull']))
        return subprocess.run(['git','pull'])

    @staticmethod
    def remove(url):
        '''
        @brief remove a vim plugin from url
        @param url url of git repository
        '''
        return vimanGitWrapper.removeByName(vimanGitWrapper.getPlugin4Url(url))

    @staticmethod
    def removeByName(name):
        sys.stdout.flush()
        path = os.path.join(vimanGitWrapper.DIR_PLUGIN,name)
        if not os.path.isdir(path):
            print(path)
            sys.exit(errno.ENOENT)
        #sys.exit(subprocess.run(['rm','-rf',path]))
        return subprocess.run(['rm','-rf',path])

    @staticmethod
    def getPlugin4Url(url):
        '''
        @brief get name of plugin from url
        @param url git repository url
        '''
        basename = os.path.basename(url)
        name = os.path.splitext(basename)
        return name[0]

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
    if parser.operations[0] in vimanArgParser.vimanOperations.operations['sync'][0]:
        for target in parser.targets:
            vimanGitWrapper.install(target)
    elif parser.operations[0] in vimanArgParser.vimanOperations.operations['remove'][0]:
        for target in parser.targets:
            vimanGitWrapper.remove(target)
    elif parser.operations[0] in vimanArgParser.vimanOperations.operations['upgrade'][0]:
        for target in parser.targets:
            vimanGitWrapper.upgrade(target)

    return 0

if '__main__' == __name__:
    sys.exit(main())

