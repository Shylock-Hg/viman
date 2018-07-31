#! /usr/bin/env python3

import argparse
import sys
import subprocess
import os
import errno

#import yaml

#errno = ['OK',                          #0
        #'~/.vim/bundle don\'t exists!'] #1

class vimanArgParser(argparse.ArgumentParser):
    def __init__(self,*args,**kwargs):
        super().__init__(...)
        # base option
        # Synchronize and option
        self.add_argument('-S','--synchronize',help='Synchronize plugin!')
        self.add_argument('-u','--sysupgrade',action='store_true',help='Upgrade all plugin!')

        #Remove and option
        self.add_argument('-R','--remove',help='Remove plugin!')

        #Query and option
        self.add_argument('-Q','--query',help='Query local plugin!')

        #Upgrade and option
        self.add_argument('-U','--upgrade',help='Upgrade local plugin!')

        #Version
        self.add_argument('-V','--version',action='version',version='%(prog)s 0.0.1')

class vimanGitWrapper():
    '''
    @brief low operation wrapper of git , install , upgrade , remove , query 
    @note all other operation base on this
    '''

    #DIR_PLUGIN = '~/.vim/bundle' os.path.isdir fail
    DIR_PLUGIN='/home/shylock/.vim/bundle'

    @staticmethod
    def install(url):
        '''
        @brief install a vim plugin to .vim/bundle by git from url
        @param url url of git repository
        '''
        if not os.path.isdir(vimanGitWrapper.DIR_PLUGIN):
            sys.exit(errno.ENOENT)
        os.chdir(vimanGitWrapper.DIR_PLUGIN)
        sys.exit(subprocess.run(['git','clone',url]))

    @staticmethod
    def upgrade(url):
        '''
        @brief upgrade a vim plugin by git from url
        @param url url of git repository
        '''
        upgradeByName(_getPlugin4Url(url))
        
    @staticmethod
    def upgradeByName(name):
        path = sys.path.join(vimanGitWrapper.DIR_PLUGIN,name)
        if not os.path.isdir(path):
            sys.exit(errno.ENOENT)
        os.chdir(path)
        sys.exit(subprocess.run(['git','pull']))

    @staticmethod
    def remove(url):
        '''
        @brief remove a vim plugin from url
        @param url url of git repository
        '''
        removeByName(_getPlugin4Url(url))

    @staticmethod
    def removeByName(name):
        path = sys.path.join(vimanGitWrapper.DIR_PLUGIN,name)
        if not os.path.isdir(path):
            sys.exit(errno.ENOENT)
        sys.exit(subprocess.run(['rm','-rf',path]))

    @staticmethod
    def _getPlugin4Url(url):
        '''
        @brief get name of plugin from url
        @param url git repository url
        '''
        token_url = url.split('/')  # https://github.com/user/repository.git
        token_name = token_url[-1].split('.') # repository.git
        return token_name[0]

def main():
    #parse argumenits
    argparser = vimanArgParser(prog='viman')
    args = argparser.parse_args()

    if args.synchronize :
        vimanGitWrapper.install(args.synchronize)
    elif args.remove :
        pass

if '__main__' == __name__:
    main()

