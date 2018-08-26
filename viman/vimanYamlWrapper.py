#! /usr/bin/env python3

import yaml
import os
import sys

from viman import vimanUtils

class vimanYamlWrapper():

    #ymlDefault = '~/.viman.yml'
    ymlDefault = os.path.join(os.getenv('HOME'),'.viman.yml')
    #ymlMode = 'r+'

    @staticmethod
    def installWrapper(install):
        def wrapper(url,recipe):
            ret = install(url,recipe) ## install plugin
            '''
            with open(vimanYamlWrapper.ymlDefault,'a+') as f:
                yaml.dump({vimanUtils.vimanUtils.getPlugin4Url(url):{'url':url,'recipe':''}}
                        ,stream=f,default_flow_style=False)
            '''
            '''
            with open(vimanYamlWrapper.ymlDefault,vimanYamlWrapper.ymlMode) as f:
                yml = dict(yaml.load(f))
                yml[vimanUtils.vimanUtils.getPlugin4Url(url)] = {'url':url,'recipe':''}
                f.seek(0)
                f.truncate()
                yaml.dump(yml,stream=f,default_flow_style=False)
            '''
            yml = vimanYamlWrapper.loadYml()
            if None == yml:
                yml = {}
            yml[vimanUtils.vimanUtils.getPlugin4Url(url)] = {'url':url,'recipe':recipe}
            vimanYamlWrapper.dumpYml(yml)
            return ret

        return wrapper

    @staticmethod
    def removeWrapper(remove):
        def wrapper(url):
            ret = remove(url)  ## remove plugin
            '''
            with open(vimanYamlWrapper.ymlDefault,vimanYamlWrapper.ymlMode) as f:
                yml = yaml.load(f)
                yml.pop(vimanUtils.vimanUtils.getPlugin4Url(url))
                f.seek(0)
                f.truncate()
                yaml.dump(yml,stream=f,default_flow_style=False)
            '''
            yml = vimanYamlWrapper.loadYml()
            yml.pop(vimanUtils.vimanUtils.getPlugin4Url(url))
            vimanYamlWrapper.dumpYml(yml)
            return ret
        
        return wrapper
        
    @staticmethod
    def removeByNameWrapper(removeByName):
        def wrapper(name):
            ret = removeByName(name) ## remove plugin by name
            '''
            with open(vimanYamlWrapper.ymlDefault,vimanYamlWrapper.ymlMode) as f:
                yml = yaml.load(f)
                yml.pop(name)
                f.seek(0)
                f.truncate()
                yaml.dump(yml,stream=f,default_flow_style=False)
            '''
            yml = vimanYamlWrapper.loadYml()
            yml.pop(name)
            vimanYamlWrapper.dumpYml(yml)
            return ret

        return wrapper

    @staticmethod
    def loadYml(file=ymlDefault):
        if not os.path.isfile(file):
            os.mknod(file);
        with open(file,'r') as f:
            yml = yaml.load(f)
            f.close()
            return yml

    @staticmethod
    def dumpYml(yml,file=ymlDefault):
        with open(file,'w') as f:
            yaml.dump(yml,stream=f,default_flow_style=False)
            f.close()


def _test():
    with open(vimanYamlWrapper.ymlDefault,'r') as f:
        #yaml.dump(yaml.load(f),stream = f, default_flow_style=False)
        yml = yaml.load(f)
        print(yml)

if '__main__' == __name__:
    _test()

