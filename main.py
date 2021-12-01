#!/usr/bin/env python3
import logging
import logging.config
import logging
import os
import sys
from importlib import reload

from logger_setup import logger_setup
from server import FileService
from utils.Configs import config
from aiohttp import web

from server.WebHandler import WebHandler
# from utils.Config import config


def setup_logger(level: str = 'NOTSET', filename: str = None):
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

    # parser.parse_args()
    # setup_logger(level=logging.getLevelName(params.log_level.upper()), filename=params.log_file)
    setup_logger(level=config.log.level, filename=config.log.file)
    logging.debug('started')
    # logging.debug('config %s', config.to_dict())

    logging.debug(f'FileService current dir: {FileService.get_current_dir()}')
    print(f'FileService current dir: {FileService.get_current_dir()}')
    logging.debug("params: {}".format(config))
    # if bool(config.dir):
    #     os.chdir(config.dir)

    reload(FileService)
    logging.debug(f'FileService current dir: {FileService.get_current_dir()}')
    FileService.change_dir(".")

    handler = WebHandler()
    app = web.Application()
    app.add_routes([
        web.get('/', handler.handle),
        web.get('/change_dir', handler.change_dir),
        web.post('/change_dir', handler.change_dir),
        web.post(r'/change_dir/{urlpath:[A-Za-z0-9-_/.\\%&]+}', handler.change_dir),
        web.get('/files', handler.get_files),
        web.get(r'/files/{urlpath:[A-Za-z0-9-_/.\\%&]+}/', handler.get_files),
        web.get(r'/files/{filename:[A-Za-z0-9-_/.\\%&]+}', handler.get_file_data),
        web.post('/files', handler.create_file),
        web.delete(r'/files/{filename:[A-Za-z0-9-_/.\\%&]+}', handler.delete_file),
    ])
    # web.run_app(app, port=config.port)
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
