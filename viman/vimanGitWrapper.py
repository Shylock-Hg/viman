
import subprocess
import os
import sys
import errno

import yaml

from viman import vimanYamlWrapper
from viman import vimanUtils

class vimanGitWrapper():
    '''
    @brief low operation wrapper of git , install , upgrade , remove , query 
    @note all other operation base on this
    '''

    DIR_PLUGIN = os.path.join(os.getenv('HOME'),'.vim/bundle')

    @staticmethod
    @vimanYamlWrapper.vimanYamlWrapper.installWrapper
    def install(url):
        '''
        @brief install a vim plugin to .vim/bundle by git from url
        @param url url of git repository
        '''
        if not os.path.isdir(vimanGitWrapper.DIR_PLUGIN):
            #print('error:don\'t exist directory `{}`!'.format(vimanGitWrapper.DIR_PLUGIN),
                    #file=sys.stderr)
            #sys.exit(errno.ENOENT)
            os.makedirs(vimanGitWrapper.DIR_PLUGIN)
        os.chdir(vimanGitWrapper.DIR_PLUGIN)
        #sys.exit(subprocess.run(['git','clone',url]))
        ret = subprocess.run(['git','clone',url])
        if not 0 == ret.returncode:
            print('error:subprocess run `{}` failed!'.format(' '.join(ret.args)),
                    file=sys.stderr)
            sys.exit(ret.returncode)
        return ret

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
        return vimanGitWrapper.upgradeByName(vimanUtils.vimanUtils.getPlugin4Url(url))
        
    @staticmethod
    def upgradeByName(name):
        path = os.path.join(vimanGitWrapper.DIR_PLUGIN,name)
        if not os.path.isdir(path):
            print('error:don\'t exist directory `{}`!'.format(path),file=sys.stderr)
            sys.exit(errno.ENOENT)
        os.chdir(path)
        #sys.exit(subprocess.run(['git','pull']))
        ret = subprocess.run(['git','pull'])
        if not 0 == ret.returncode:
            print('error:subprocess run `{}` failed!'.format(' '.join(ret.args)),
                    file=sys.stderr)
            sys.exit(ret.returncode)
        return ret

    @staticmethod
    #@vimanYamlWrapper.vimanYamlWrapper.removeWrapper anti-multi YAML decorator
    def remove(url):
        '''
        @brief remove a vim plugin from url
        @param url url of git repository
        '''
        return vimanGitWrapper.removeByName(vimanUtils.vimanUtils.getPlugin4Url(url))

    @staticmethod
    @vimanYamlWrapper.vimanYamlWrapper.removeByNameWrapper
    def removeByName(name):
        path = os.path.join(vimanGitWrapper.DIR_PLUGIN,name)
        if not os.path.isdir(path):
            print('error:don\'t exist directory `{}`!'.format(path),file=sys.stderr)
            sys.exit(errno.ENOENT)
        #sys.exit(subprocess.run(['rm','-rf',path]))
        ret = subprocess.run(['rm','-rf',path])
        if not 0 == ret.returncode:
            print('error:subprocess run `{}` failed!'.format(' '.join(ret.args)),
                    file=sys.stderr)
            sys.exit(ret.returncode)
        return ret

    @staticmethod
    def removeByYml(ymlName):
        '''
        @brief remove plugins by yml
        @param ymlName yml file name
        '''
        if not os.path.isfile(ymlName):
            print('error:don\'t exist file `{}`!'.format(ymlName),file=sys.stderr)
            sys.exit(errno.EINVAL)
        with open(ymlName) as f:
            yml = yaml.load(f)
            for v in yml.values():
                vimanGitWrapper.remove(v['url'])


