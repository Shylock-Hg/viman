#! /usr/bin/env python3

'''
@brief vimanYamlWrapper wrapper fo yaml operations
@note not the only entry of yaml API
'''

import os
import sys
import errno

import yaml

from viman import vimanUtils

class vimanYamlWrapper():
    '''
    @brief vimanYamlWrapper wrapper of yaml operations
    '''

    ymlDefault = os.path.join(os.getenv('HOME'), '.viman.yml')

    @staticmethod
    def installWrapper(install):
        def wrapper(url, recipe):
            ret = install(url, recipe)  # install plugin
            yml = vimanYamlWrapper.loadYml()
            if yml is None:
                yml = {}
            yml[vimanUtils.vimanUtils.getPlugin4Url(url)] = {
                'url':url, 'recipe':recipe}
            vimanYamlWrapper.dumpYml(yml)
            return ret

        return wrapper

    @staticmethod
    def removeWrapper(remove):
        def wrapper(url):
            ret = remove(url)  # remove plugin
            yml = vimanYamlWrapper.loadYml()
            if yml is None:
                return errno.EINVAL
            try:
                yml.pop(vimanUtils.vimanUtils.getPlugin4Url(url))
            except KeyError:
                print(
                    'error:yml no key `{}`!'.format(
                        vimanUtils.vimanUtils.getPlugin4Url(url)),
                    file=sys.stderr)
            vimanYamlWrapper.dumpYml(yml)
            return ret
        
        return wrapper

    @staticmethod
    def removeByNameWrapper(removeByName):
        def wrapper(name):
            ret = removeByName(name)  # remove plugin by name
            yml = vimanYamlWrapper.loadYml()
            try:
                yml.pop(name)
            except KeyError:
                print('error:yml no key `{}`!'.format(name), file=sys.stderr)

            vimanYamlWrapper.dumpYml(yml)
            return ret

        return wrapper

    @staticmethod
    def loadYml(file=ymlDefault):
        '''
        @brief load yaml object from yaml file
        @param file yaml file name string
        @retval yaml object
        '''
        if not os.path.isfile(file):
            os.mknod(file)
        with open(file, 'r') as f:
            yml = yaml.safe_load(f)
            f.close()
            return yml

    @staticmethod
    def dumpYml(yml, file=ymlDefault):
        with open(file, 'w') as f:
            yaml.dump(yml, stream=f, default_flow_style=False)
            f.close()


def _test():
    with open(vimanYamlWrapper.ymlDefault, 'r') as f:
        # yaml.dump(yaml.load(f),stream = f, default_flow_style=False)
        yml = yaml.safe_load(f)
        print(yml)

if '__main__' == __name__:
    _test()
