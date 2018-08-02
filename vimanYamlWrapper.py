#! /usr/bin/env python3

import yaml
import os
import sys

from vimanUtils import vimanUtils

class vimanYamlWrapper():

    #ymlDefault = '~/.viman.yml'
    ymlDefault = os.path.join(os.getenv('HOME'),'.viman.yml')
    ymlMode = 'r+'

    @staticmethod
    def installWrapper(install):
        def wrapper(url):
            ret = install(url) ## install plugin
            if not 0 == ret.returncode:
                print('error:subprocess run git failed!',file=sys.stderr)
                sys.exit(ret.returncode)
            with open(vimanYamlWrapper.ymlDefault,'a+') as f:
                yaml.dump({vimanUtils.getPlugin4Url(url):{'url':url,'recipe':''}}
                        ,stream=f,default_flow_style=False)
            '''
            with open(vimanYamlWrapper.ymlDefault,vimanYamlWrapper.ymlMode) as f:
                yml = dict(yaml.load(f))
                yml[vimanUtils.getPlugin4Url(url)] = {'url':url,'recipe':''}
                f.seek(0)
                f.truncate()
                yaml.dump(yml,stream=f,default_flow_style=False)
            '''
            return ret

        return wrapper

    @staticmethod
    def removeWrapper(remove):
        def wrapper(url):
            ret = remove(url)  ## remove plugin
            with open(vimanYamlWrapper.ymlDefault,vimanYamlWrapper.ymlMode) as f:
                yml = yaml.load(f)
                yml.pop(vimanUtils.getPlugin4Url(url))
                f.seek(0)
                f.truncate()
                yaml.dump(yml,stream=f,default_flow_style=False)
            return ret
        
        return wrapper
        
    @staticmethod
    def removeByNameWrapper(removeByName):
        def wrapper(name):
            ret = removeByName(name) ## remove plugin by name
            with open(vimanYamlWrapper.ymlDefault,vimanYamlWrapper.ymlMode) as f:
                yml = yaml.load(f)
                yml.pop(name)
                f.seek(0)
                f.truncate()
                yaml.dump(yml,stream=f,default_flow_style=False)
            return ret

        return wrapper


def _test():
    with open('test.yml','r+') as f:
        #yaml.dump(yaml.load(f),stream = f, default_flow_style=False)
        yml = yaml.load(f)
        f.seek(0)
        yaml.dump(yml,stream=f,default_flow_style=False)

if '__main__' == __name__:
    _test()

