'''
@brief vimanUtils common utils for viman
'''

import os

class vimanUtils():
    @staticmethod
    def getPlugin4Url(url):
        '''
        @brief get name of plugin from url
        @param url git repository url
        '''
        basename = os.path.basename(url)
        name = os.path.splitext(basename)
        return name[0]

    @staticmethod
    def get_github_url_4_name(name):
        '''
        @brief get url from the name of repository
        @param name username/repository
        '''
        GITHUB_PREFIX = 'https://github.com/'
        url = GITHUB_PREFIX + name + '.git'
        return url
