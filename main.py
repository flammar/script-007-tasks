#!/usr/bin/env python3
import argparse
import os
import sys
import logging
from importlib import reload
from server import FileService


def main():
    argv = sys.argv
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--dir', default='data', type=str, help="working directory (default: 'data')",
                        required=False)
    params = parser.parse_args()
    logging.debug(FileService.get_current_dir())
    # FileService.change_dir(".")
    if bool(params.dir):
        os.chdir(params.dir)
    # if bool(params.d):
    #     os.chdir(params.d)
    # from server import FileService

    reload(FileService)
    # FileService.__init__()
    logging.debug(FileService.get_current_dir())
    FileService.change_dir(".")

    """
    Command line options:
    -d --dir  - working directory (absolute or relative path, default: current_app_folder/data).
    -h --help - help.
    """
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-d', '--dir', default='data', type=str,
    #                     help="working directory (default: 'data')")
    # params = parser.parse_args()
    #
    # work_dir = params.dir if os.path.isabs(params.dir) else os.path.join(os.getcwd(), params.dir)
    # FileService.change_dir(work_dir)


if __name__ == '__main__':
    main()
