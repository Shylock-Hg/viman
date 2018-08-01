#! /usr/bin/env python3

import getopt
import sys
import errno
import copy

class vimanOperations():
    ## (short,long)
    operations = {'sync':('S','sync'),
                  'remove':('R','remove'),
                  'upgrade':('U','upgrade'),
                  'query':('Q','query'),
                  'version':('V','version'),
                  'help':('h','help')}
    @staticmethod
    def getKey4Operation(operation:str):
        '''
        @brief get key by operation name(such as 'Q','sync')
        @param operation name
        @retval key of operations
        '''
        for kv in vimanOperations.operations.items():
            if operation in kv[1]:
                return kv[0]

    @staticmethod
    def getOperationsShort():
        return [operation[0] for operation in vimanOperations.operations.values() 
                if not '' == operation[0]]

    @staticmethod
    def getOperationsLong():
        return [operation[1] for operation in vimanOperations.operations.values() 
                if not '' == operation[1]]
    @staticmethod
    def getOperations():
        return [ops[0] for ops in list(vimanOperations.operations.values())] + [ops[1] for ops in list(vimanOperations.operations.values())]


class vimanOptions():
    options = {'sysupgrade':('u','sysupgrade','S'),
            'recursive':('r','recursive','U')} ## (short,long,operations)

    @staticmethod
    def getKey4Option(option:str):
        '''
        @brief get key by option name(such as 'u','sysupgrade')
        @param option name
        @retval key of options
        '''
        for kv in vimanOptions.options.items():
            if option in kv[1]:
                return kv[0]
    @staticmethod
    def getOptionShort():
        return [option[0] for option in vimanOptions.options.values() if not '' == option[0]]

    @staticmethod
    def getOptionLong():
        return [option[1] for option in vimanOptions.options.values() 
                if not '' == option[1]]
    
    @staticmethod
    def getOptions():
        return [opt[0] for opt in list(vimanOptions.options.values())] + [opt[1] for opt in list(vimanOptions.options.values())]


class vimanArgParser():
    '''
    @brief viman command line arguments parser
    @note viman command line synopsis `viman <operation> [options] [targets]`
    '''
    def __init__(self,args):
        '''
        @brief parse command line arguments
        @param args sys.argv[1:]
        @retval generated object
        '''
        '''
        options_short = [option[0] for option in vimanOptions.options.values() if not '' == option[0]] + [operation[0] for operation in vimanOperations.operations.values() if not '' == operation[0]]
        options_long = [option[1] for option in vimanOptions.options.values() if not '' == option[1]] + [operation[1] for operation in vimanOperations.operations.values() if not '' == operation[1]]
        options_short = ''.join(options_short)
        '''
        options_short = vimanOperations.getOperationsShort() + vimanOptions.getOptionShort()
        #print(options_short)
        options_short = ''.join(options_short)
        options_long  = vimanOperations.getOperationsLong()  + vimanOptions.getOptionLong()
        #print(options_long)
        
        opts,rest = getopt.getopt(args, options_short, options_long)

        self.targets = rest ## targets git repository url

        opts = map(lambda opt : opt[0].replace('-',''), opts)

        '''
        operations = [ops[0] for ops in list(vimanOperations.operations.values())] + [ops[1] for ops in list(vimanOperations.operations.values())]
        options = [opt[0] for opt in list(vimanOptions.options.values())] + [opt[1] for opt in list(vimanOptions.options.values())]
        '''
        operations = vimanOperations.getOperations()
        options = vimanOptions.getOptions()

        opts_operations = list(filter(lambda opt : opt in operations, copy.deepcopy(opts)))
        opts_options = list(filter(lambda opt : opt in options, copy.deepcopy(opts)))

        # check operations
        if not 1 == len(opts_operations):
            print('error: only one operation may be used at a time!',file=sys.stderr)
            sys.exit(errno.EINVAL)

        # check options
        def check_option(option,operation):
            key_option = vimanOptions.getKey4Option(option)
            key_operation = vimanOperations.getKey4Operation(operation)
            if not vimanOperations.operations[key_operation][0] in vimanOptions.options[key_option][2]:
                print('error:invalid option `{}` for operation `{}`'.format(option,vimanOperations.operations[key_operation][0]),file=sys.stderr)
                sys.exit(errno.EINVAL)

        for opt in opts_options:
            check_option(opt,operations[0])

        self.operations = opts_operations ## operations
        self.options = opts_options ## options



def _test():
    #print(vimanOperations.getOperations())
    #print(vimanOptions.getOptions())
    parser = vimanArgParser(sys.argv[1:])
    print(parser.operations)
    print(parser.options)
    print(parser.targets)

if '__main__' == __name__:
    _test()

