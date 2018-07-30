#! /usr/bin/env python3

import argparse
import sys

class vimanArgParser(argparse.ArgumentParser):
    def __init__(self,*args,**kwargs):
        super().__init__(...)
        # base option
        self.add_argument('-S','--synchronize',help='Synchronize plugin!')
        self.add_argument('-R','--remove',help='Remove plugin!')
        self.add_argument('-Q','--query',help='Query local plugin!')
        self.add_argument('-U','--upgrade',help='Upgrade local plugin!')
        self.add_argument('-V','--version',action='version',version='%(prog)s 0.0.1')


def main():
    argparser = vimanArgParser(prog='viman')
    args = argparser.parse_args()



if '__main__' == __name__:
    main()

