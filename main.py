#!/usr/bin/env python3
import logging
import logging.config
import logging
import sys
from importlib import reload

from logger_setup import logger_setup
from server import FileService
from utils.Configs import config_data
from aiohttp import web

from server.WebHandler import WebHandler
from utils.Config import config


def setup_logger(level='NOTSET', filename=None):
    logger_conf = {
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
        logger_conf['handlers']['file'] = {
            'class': 'logging.FileHandler',
            'encoding': 'UTF-8',
            'formatter': 'default',
            'filename': filename,
        }
        logger_conf['root']['handlers'].append('file')
    logging.config.dictConfig(logger_conf)


def main():
    """
    Command line options:
    -d --dir  - working directory (absolute or relative path, default: current_app_folder/data).
    -h --help - help.
    """

    # parser = argparse.ArgumentParser()
    # parser.add_argument('-d', '--dir', default='data', type=str, help="working directory (default: 'data')",
    #                     required=False)
    # parser.add_argument('--log-level', default='warning', choices=['debug', 'info', 'warning', 'error'],
    #                     help='Log level to console (default is warning)')
    # parser.add_argument('-l', '--log-file', type=str, help='Log file.')

    params = config_data.data
    # parser.parse_args()
    # setup_logger(level=logging.getLevelName(params.log_level.upper()), filename=params.log_file)
    setup_logger(level=logging.getLevelName(params.log.level), filename=params.log.file)
    logging.debug('started')
    # logging.debug('config %s', config.to_dict())

    logging.debug(f'FileService current dir: {FileService.get_current_dir()}')
    print(f'FileService current dir: {FileService.get_current_dir()}')
    logging.debug("params: {}".format(params))
    if bool(params.dir):
        os.chdir(params.dir)

    reload(FileService)
    logging.debug(f'FileService current dir: {FileService.get_current_dir()}')
    FileService.change_dir(".")

    handler = WebHandler()
    app = web.Application()
    app.add_routes([
        web.get('/', handler.handle),
        # TODO: add more routes
    ])
    web.run_app(app, port=config.port)



if __name__ == '__main__':
    # logging.basicConfig(level=logging.DEBUG)
    # main()

    # logger_setup()

    try:
        main()
    except KeyboardInterrupt:
        sys.exit('\nERROR: Interrupted by user')
    # except BaseException as err:
    #     print(f'ERROR: Something goes wrong:\n{err}')
    #     sys.exit(1)
