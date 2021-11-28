#!/usr/bin/env python3
import argparse
import os
import logging
from importlib import reload

from logger_setup import logger_setup
from server import FileService


def main():
    """
    Command line options:
    -d --dir  - working directory (absolute or relative path, default: current_app_folder/data).
    -h --help - help.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir', default='data', type=str, help="working directory (default: 'data')",
                        required=False)
    params = parser.parse_args()
    logging.debug(f'FileService current dir: {FileService.get_current_dir()}')
    logging.debug("params: {}".format(params))

    if bool(params.dir):
        os.chdir(params.dir)

    reload(FileService)
    logging.debug(f'FileService current dir: {FileService.get_current_dir()}')
    FileService.change_dir(".")


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()

logger_setup()

print('started')
logger = logging.getLogger('myprogram')
logger.error('example of error message')
logger.warning('example of warning message')
logger.info('example of information message')
logger.debug('example of debug message')
print('finished')
