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
