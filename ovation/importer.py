# Copyright 2011, Physion Consulting LLC
# -*- coding: utf-8 -*-

import sys
import argparse
import getpass
import logging

from ovation.connection import connect

def import_main(argv=sys.argv,
                name=__name__,
                description=None,
                file_ext=None,
                parser_callback=None,
                import_fn=None,
                dsc=None):

    """Basic importer main function for data importers

    Caller may provide a `parser_callback` for adding additional `argparse` arguments.

    The import function must be of the form::

        import_fn(data_context,
                  container=None, #EpochContainer UUID
                  protocol=None, #Protocol UUID
                  sources=[], #Source UUIDs
                  files=[],
                  timezone=None,
                  **args)

    A minimal import __main__.py using `import_main`::

        if __name__ == '__main__':
            sys.exit(import_main(args=sys.argv,
                                name=<importer name>,
                                description=<importer description>,
                                file_ext=<imported extension, e.g. csv>,
                                import_fn=<importer function or callable))



    Parameters
    ----------
    :parameter args : list
        Commandline arguments
    :parameter name : str
        Importer name
    :parameter description : str
        Importer description
    :parameter file_ext : str
        File extension for files imported by this importer
    :parameter parser_callback : callable
        Parser callback for adding additional argparse arguemnts. Must be of the form callback(parser) -> parser
    :parameter import_fn : callable
        Import function
    :parameter dsc : us.physion.ovation.api.DataStoreCoordinator
        Optional DataStoreCoordinator, e.g. for testing.

    Returns
    -------
    :return exit value
    """


    parser = argparse.ArgumentParser(prog=name,
                                     description=description)

    auth_group = parser.add_argument_group('authentication')
    auth_group.add_argument('--user', help='ovation.io user email')
    auth_group.add_argument('--password', help='ovation.io password')

    parser.add_argument('files', metavar='f.{}'.format(file_ext), nargs='+', type=str)

    parser.add_argument('--timezone',
                        default=None,
                        help='timezone name in which data was collected. Default = local time zone')

    experiment_group = parser.add_argument_group('epoch container')
    experiment_group.add_argument('--container', help='epoch container ID', required=True)
    experiment_group.add_argument('--protocol', help='protocol ID', required=True)
    experiment_group.add_argument('--sources', help='Source IDs', required=False, nargs='+', type=str)

    if parser_callback:
        parser = parser_callback(parser)

    args = parser.parse_args(args=argv)

    logging.basicConfig(filename='import.log',level=logging.INFO)

    if dsc is None:
        if args.user is None:
            args.user = raw_input('ovation.io user: ')

        if args.password is None:
            password = getpass.getpass(prompt='ovation.io password: ')
        else:
            password = args.password

        dsc = connect(args.user, password)

    ctx = dsc.getContext()

    try:
        # Remove authentication info from args
        args = vars(args)
        args.pop('user')
        args.pop('password')

        return import_fn(ctx, **args)
    except Exception:
        logging.error('Unable to import {}'.format(args.files), exc_info=True)
        return 1

