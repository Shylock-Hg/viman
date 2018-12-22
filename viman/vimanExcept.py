#! /usr/bin/env python3

'''
@brief exception of viman application
@author Shylock Hg
@date 2018-12-22
@email tcath2s@gmail.com
'''

class vimanExcept(Exception):
    '''
    @brief exception of viman application
    '''
    def __init__(self, errno, desc):
        '''
        @brief create exception with errno and description
        @param errno error number
        @param desc description of error
        '''
        self.errno = errno
        self.desc = desc

    def what(self):
        '''
        @brief return the description string of exception
        '''
        return self.desc
