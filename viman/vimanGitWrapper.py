'''
@brief vimanGitWrapper wrapper of git subprocess
@note the only API to git operations
'''

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

    DIR_PLUGIN = os.path.join(os.getenv('HOME'), '.vim/bundle')

    @staticmethod
    @vimanYamlWrapper.vimanYamlWrapper.installWrapper
    def install(url, recipe):
        '''
        @brief install a vim plugin to .vim/bundle by git from url
        @param url url of git repository
        '''
        if not os.path.isdir(vimanGitWrapper.DIR_PLUGIN):
            os.makedirs(vimanGitWrapper.DIR_PLUGIN)
        pwd = os.getenv('PWD')
        os.chdir(vimanGitWrapper.DIR_PLUGIN)
        if hasattr(subprocess, 'run'):
            ret = subprocess.run(['/usr/bin/env', 'git', 'clone', url]).returncode
        else:
            ret = subprocess.call(['/usr/bin/env', 'git', 'clone', url])
        if 0 != ret:
            os.chdir(pwd)
            sys.exit(ret)
        os.chdir(pwd)
        ret = os.system(recipe)
        return ret

    @staticmethod
    def installByYml(ymlName):
        '''
        @brief install plugins by yml
        @param ymlName yml file name
        '''
        if not os.path.isfile(ymlName):
            print(
                'error:don\'t exist file `{}`!'.format(ymlName),
                file=sys.stderr)
            sys.exit(errno.EINVAL)
        with open(ymlName) as f:
            yml = yaml.safe_load(f)
            if yml:
                for v in yml.values():
                    vimanGitWrapper.install(v['url'], v['recipe'])

    @staticmethod
    def installByCurrent(ymlString):
        if ymlString:
            yml = yaml.safe_load(ymlString)
            if yml:
                for v in yml.values():
                    vimanGitWrapper.install(v['url'], v['recipe'])

    @staticmethod
    def upgrade(url):
        '''
        @brief upgrade a vim plugin by git from url
        @param url url of git repository
        '''
        return vimanGitWrapper.upgradeByName(
            vimanUtils.vimanUtils.getPlugin4Url(url))

    @staticmethod
    def upgradeByName(name):
        '''
        @brief upgrade plugin by plugin name
        '''
        path = os.path.join(vimanGitWrapper.DIR_PLUGIN, name)
        if not os.path.isdir(path):
            print(
                'error:don\'t exist directory `{}`!'.format(path),
                file=sys.stderr)
            sys.exit(errno.ENOENT)
        pwd = os.getenv('PWD')
        os.chdir(path)
        if hasattr(subprocess, 'run'):
            ret = subprocess.run(['/usr/bin/env', 'git', 'pull']).returncode
        else:
            ret = subprocess.call(['/usr/bin/env', 'git', 'pull'])
        if 0 != ret:
            os.chdir(pwd)
            sys.exit(ret)
        os.chdir(pwd)
        return ret

    @staticmethod
    def upgradeByYml(ymlName):
        if not os.path.isfile(ymlName):
            print(
                'error:don\'t exist file `{}`!'.format(ymlName),
                file=sys.stderr)
            sys.exit(errno.EINVAL)
        with open(ymlName) as f:
            yml = yaml.safe_load(f)
            if yml:
                for v in yml.values():
                    vimanGitWrapper.upgrade(v['url'])

    @staticmethod
    def remove(url):
        '''
        @brief remove a vim plugin from url
        @param url url of git repository
        '''
        return vimanGitWrapper.removeByName(
            vimanUtils.vimanUtils.getPlugin4Url(url))

    @staticmethod
    @vimanYamlWrapper.vimanYamlWrapper.removeByNameWrapper
    def removeByName(name):
        path = os.path.join(vimanGitWrapper.DIR_PLUGIN, name)
        if not os.path.isdir(path):
            print(
                'error:don\'t exist directory `{}`!'.format(path),
                file=sys.stderr)
            sys.exit(errno.ENOENT)
        if hasattr(subprocess, 'run'):
            ret = subprocess.run(['/usr/bin/env', 'rm', '-rf', path]).returncode
        else:
            ret = subprocess.call(['/usr/bin/env', 'rm', '-rf', path])
        if 0 != ret:
            sys.exit(ret)
        return ret

    @staticmethod
    def removeByYml(ymlName):
        '''
        @brief remove plugins by yml
        @param ymlName yml file name
        '''
        if not os.path.isfile(ymlName):
            print(
                'error:don\'t exist file `{}`!'.format(ymlName),
                file=sys.stderr)
            sys.exit(errno.EINVAL)
        with open(ymlName) as f:
            yml = yaml.safe_load(f)
            if yml:
                for v in yml.values():
                    vimanGitWrapper.remove(v['url'])
