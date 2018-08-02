
import subprocess
import os
import sys
import errno

import yaml

from vimanYamlWrapper import vimanYamlWrapper
from vimanUtils import vimanUtils

class vimanGitWrapper():
    '''
    @brief low operation wrapper of git , install , upgrade , remove , query 
    @note all other operation base on this
    '''

    DIR_PLUGIN = os.path.join(os.getenv('HOME'),'.vim/bundle')

    @staticmethod
    @vimanYamlWrapper.installWrapper
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
    def installByYml(ymlName):
        '''
        @brief install plugins by yml
        @param ymlName yml file name
        '''
        if not os.path.isfile(ymlName):
            print('error:don\'t exist file `{}`!'.format(ymlName),file=sys.stderr)
            sys.exit(errno.EINVAL)
        with open(ymlName) as f:
            yml = yaml.load(f)
            for v in yml.values():
                vimanGitWrapper.install(v['url'])

    @staticmethod
    def upgrade(url):
        '''
        @brief upgrade a vim plugin by git from url
        @param url url of git repository
        '''
        return vimanGitWrapper.upgradeByName(vimanUtils.getPlugin4Url(url))
        
    @staticmethod
    def upgradeByName(name):
        path = os.path.join(vimanGitWrapper.DIR_PLUGIN,name)
        if not os.path.isdir(path):
            sys.exit(errno.ENOENT)
        os.chdir(path)
        #sys.exit(subprocess.run(['git','pull']))
        return subprocess.run(['git','pull'])

    @staticmethod
    @vimanYamlWrapper.removeWrapper
    def remove(url):
        '''
        @brief remove a vim plugin from url
        @param url url of git repository
        '''
        return vimanGitWrapper.removeByName(vimanUtils.getPlugin4Url(url))

    @staticmethod
    @vimanYamlWrapper.removeByNameWrapper
    def removeByName(name):
        sys.stdout.flush()
        path = os.path.join(vimanGitWrapper.DIR_PLUGIN,name)
        if not os.path.isdir(path):
            print(path)
            sys.exit(errno.ENOENT)
        #sys.exit(subprocess.run(['rm','-rf',path]))
        return subprocess.run(['rm','-rf',path])


