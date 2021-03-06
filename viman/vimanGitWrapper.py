'''
@brief vimanGitWrapper wrapper of git operation (plugin operation in fact)
@note the only API to git operations
'''

import os
import sys
import errno
import shutil

import yaml
from git import Repo
from git import remote

from viman import vimanYamlWrapper
from viman import vimanUtils
from viman import vimanExcept

class vimanGitWrapper():
    '''
    @brief low operation wrapper of plugin , install , upgrade , remove , query
    @note all other operation base on this
    '''

    DIR_PLUGIN = os.path.join(os.path.expanduser('~'), '.vim/pack/viman/start')

    @staticmethod
    @vimanYamlWrapper.vimanYamlWrapper.installWrapper
    def install(url, recipe):
        '''
        @brief install a vim plugin to .vim/bundle by git from url
        @param url url of git repository
        '''
        if not os.path.isdir(vimanGitWrapper.DIR_PLUGIN):
            os.makedirs(vimanGitWrapper.DIR_PLUGIN)
        Repo.clone_from(url, os.path.join(
            vimanGitWrapper.DIR_PLUGIN,
            vimanUtils.vimanUtils.getPlugin4Url(url)))
        ret = os.system(recipe)
        if ret != 0:
            raise vimanExcept.vimanExcept(ret, "System scripts failed!")

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
            # sys.exit(errno.EINVAL)
            raise vimanExcept.vimanExcept(
                errno.EINVAL, "Don't exist yml file `{}`!".format(ymlName))
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
    def install_by_name(repository):
        '''
        @brief install the plugin by repository name in GitHub
        @param repository username/repository
        '''
        url = vimanUtils.vimanUtils.get_github_url_4_name(repository)
        vimanGitWrapper.install(url, '')

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
            # sys.exit(errno.ENOENT)
            raise vimanExcept.vimanExcept(
                errno.ENOENT, "Don't exist path `{}`!".format(path))
        repo = Repo(path)
        r = remote.Remote(repo, 'origin')
        r.pull()
        return 0

    @staticmethod
    def upgradeByYml(ymlName):
        if not os.path.isfile(ymlName):
            print(
                'error:don\'t exist file `{}`!'.format(ymlName),
                file=sys.stderr)
            # sys.exit(errno.EINVAL)
            raise vimanExcept.vimanExcept(
                errno.EINVAL, "Don't exist yml file `{}`!".format(ymlName))
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
            # sys.exit(errno.ENOENT)
            raise vimanExcept.vimanExcept(
                errno.ENOENT, "Don't exist directory `{}`".format(path))
        shutil.rmtree(path, ignore_errors=True)
        return 0

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
            # sys.exit(errno.EINVAL)
            raise vimanExcept.vimanExcept(
                errno.EINVAL, "Don't exist file `{}`".format(ymlName))
        with open(ymlName) as f:
            yml = yaml.safe_load(f)
            if yml:
                for v in yml.values():
                    vimanGitWrapper.remove(v['url'])
