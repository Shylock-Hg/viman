#! /usr/bin/env python3

import getopt
import sys

class vimanArgParser():
    '''
    @brief viman command line arguments parser
    @note viman command line synopsis `viman <operations> [options] [targets]`
    '''

    ## (short,long)
    operations = [('S','sync'),
                  ('R','remove'),
                  ('U','upgrade'),
                  ('Q','query'),
                  ('V','version'),
                  ('h','help')]

    options = [('u','sysupgrade','S')] ## (short,long,operations)

    def __init__(self,args):
        '''
        @brief parse command line arguments
        @param args sys.argv[1:]
        @retval generated object
        '''
        options_short = [option[0] for option in vimanArgParser.options if not '' == option[0]] + [operation[0] for operation in vimanArgParser.operations if not '' == operation[0]]
        options_long = [option[1] for option in vimanArgParser.options if not '' == option[1]] + [operation[1] for operation in vimanArgParser.operations if not '' == operation[1]]
        options_short = ''.join(options_short)
        
        opts,rest = getopt.getopt(args, options_short, options_long)

        self.targets = rest ## targets git repository url


def _test():
    parser = vimanArgParser(sys.argv[1:])

if '__main__' == __name__:
    _test()

