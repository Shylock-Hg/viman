#! /usr/bin/env python3

'''
@brief vimanArgParser the submodule of command line parser
@note 'viman <operation> [options...] [targets..]'
'''

import getopt
import sys
import errno
import copy

class vimanOperations():
    # (short,long,des)
    operations = {'sync': ('S', 'sync', 'Synchronize vim plugin package!'),
                  'remove': ('R', 'remove', 'Remove vim plugin package!'),
                  'upgrade': ('U', 'upgrade', 'Upgrade vim plugin package!'),
                  'query': ('Q', 'query', 'Query vim plugin package!'),
                  'version': ('V', 'version', 'Show version of application!'),
                  'help': ('h', 'help', 'Print help information!')}

    @staticmethod
    def getKey4Operation(operation:str):
        '''
        @brief get key by operation name(such as 'Q','sync')
        @param operation name
        @retval key of operations
        '''
        for key_value in vimanOperations.operations.items():
            if operation in key_value[1]:
                return key_value[0]

        return None

    @staticmethod
    def getOperationsShort():
        return [operation[0] for operation in
                vimanOperations.operations.values()
                if not '' == operation[0]]

    @staticmethod
    def getOperationsLong():
        return [operation[1] for operation in
                vimanOperations.operations.values()
                if not '' == operation[1]]

    @staticmethod
    def getOperations():
        return [ops[0] for ops in list(vimanOperations.operations.values())] +\
               [ops[1] for ops in list(vimanOperations.operations.values())]


class vimanOptions():

    # (short,long,operations,des)
    options = {
        'sysupgrade': (
            'u', 'sysupgrade', 'S', 'Upgrade all vim plugin packages!'),
        'file': (
            'f', 'file', 'SRU', 'Specify plugins by yml file!'),
        'recursive': (
            'r', 'recursive', 'U',
            'Recursive upgrade vim plugin packages!'),
        'current': (
            'c', 'current', 'S',
            'Specify a current yml context string'),
        'name': (
            'n', 'name', 'R',
            'Specify the name of plugins to remove!')}

    @staticmethod
    def getKey4Option(option:str):
        '''
        @brief get key by option name(such as 'u','sysupgrade')
        @param option name
        @retval key of options
        '''
        for key_value in vimanOptions.options.items():
            if option in key_value[1]:
                return key_value[0]

    @staticmethod
    def getOptionShort():
        return [option[0] for option in
                vimanOptions.options.values() if '' != option[0]]

    @staticmethod
    def getOptionLong():
        return [option[1] for option in vimanOptions.options.values()
                if '' != option[1]]

    @staticmethod
    def getOptions():
        return [opt[0] for opt in list(vimanOptions.options.values())] +\
                [opt[1] for opt in list(vimanOptions.options.values())]


class vimanArgParser():
    '''
    @brief viman command line arguments parser
    @note viman command line synopsis `viman <operation> [options] [targets]`
    '''
    def __init__(self, args):
        '''
        @brief parse command line arguments
        @param args sys.argv[1:]
        @retval generated object
        '''
        options_short = \
             vimanOperations.getOperationsShort() +\
             vimanOptions.getOptionShort()
        # print(options_short)
        options_short = ''.join(options_short)
        options_long = \
                vimanOperations.getOperationsLong() +\
                vimanOptions.getOptionLong()
        # print(options_long)

        opts, rest = getopt.getopt(args, options_short, options_long)

        self.targets = rest  # targets git repository url

        opts = map(lambda opt: opt[0].replace('-', ''), opts)
        # print(list(opts))

        operations = vimanOperations.getOperations()
        options = vimanOptions.getOptions()

        opts_operations = list(filter(
            lambda opt: opt in operations,
            copy.deepcopy(opts)))
        # print(opts_operations)
        opts_options = list(filter(
            lambda opt: opt in options,
            copy.deepcopy(opts)))

        # check operations
        if not 1 == len(opts_operations):
            print(
                    'error: only one operation may be used at a time!',
                    file=sys.stderr)
            sys.exit(errno.EINVAL)

        # check options
        def check_option(option, operation):
            key_option = vimanOptions.getKey4Option(option)
            key_operation = vimanOperations.getKey4Operation(operation)
            if not vimanOperations.operations[key_operation][0] in \
                    vimanOptions.options[key_option][2]:
                print('error:invalid option `{}` for operation `{}`'.format(
                    option,
                    vimanOperations.operations[key_operation][0]),
                    file=sys.stderr)
                sys.exit(errno.EINVAL)

        for opt in opts_options:
            check_option(opt, opts_operations[0])

        if len(opts_operations[0]) > 1:
            # operations
            self.operations = vimanOperations.operations[opts_operations[0]][0]
        else:
            self.operations = opts_operations[0]

        opts_options_short = filter(
                lambda o: 1 == len(o),
                copy.deepcopy(opts_options))
        opts_options_long = filter(
                lambda o: 1 < len(o),
                copy.deepcopy(opts_options))
        opts_options_long = map(
                lambda l: vimanOptions.operations[ops][0],
                opts_options_long)
        opts_options = list(opts_options_short) + list(opts_options_long)
        self.options = opts_options  # options

    @staticmethod
    def printUsage():
        '''
        @brief print usage of application
        '''
        print('\nSynopsis of viman: ')
        print('viman <operation> [options...] [targets...]')
        for ops in vimanOperations.operations.values():
            print('\n\tOperation `-{},--{}` for {}'.format(
                ops[0], ops[1], ops[2]))
            for opt in vimanOptions.options.values():
                if ops[0] in opt[2]:
                    print('\t\tOption `-{},--{}` for {}'.format(
                        opt[0], opt[1], opt[3]))


def _test():
    parser = vimanArgParser(sys.argv[1:])
    print(parser.operations)
    print(parser.options)
    print(parser.targets)

if '__main__' == __name__:
    _test()
