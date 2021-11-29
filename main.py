#!/usr/bin/env python3
import argparse
import logging
import logging.config
import os
import logging
from importlib import reload

from logger_setup import logger_setup
from server import FileService


def setup_logger(level='NOTSET', filename=None):
    config = {
        'version': 1,
        'formatters': {
            'default': {
                'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'level': level,
            },
        },
        'root': {
            'level': 'DEBUG',
            'handlers': ['console'],
        }
    }
    if filename:
        config['handlers']['file'] = {
            'class': 'logging.FileHandler',
            'encoding': 'UTF-8',
            'formatter': 'default',
            'filename': filename,
        }
        config['root']['handlers'].append('file')
    logging.config.dictConfig(config)


def main():
    """
    Command line options:
    -d --dir  - working directory (absolute or relative path, default: current_app_folder/data).
    -h --help - help.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir', default='data', type=str, help="working directory (default: 'data')",
                        required=False)
    parser.add_argument('--log-level', default='warning', choices=['debug', 'info', 'warning', 'error'],
                        help='Log level to console (default is warning)')
    parser.add_argument('-l', '--log-file', type=str, help='Log file.')
    params = parser.parse_args()
    setup_logger(level=logging.getLevelName(params.log_level.upper()), filename=params.log_file)
    logging.debug('started')
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
    try:
        main()
    except KeyboardInterrupt:
        sys.exit('\nERROR: Interrupted by user')
    except BaseException as err:
        print(f'ERROR: Something goes wrong:\n{err}')
        sys.exit(1)
