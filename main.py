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
    parser.add_argument('-d', help='Set working directory', required=False)
    namespace = parser.parse_args()
    logging.debug(FileService.get_current_dir())
    FileService.change_dir(".")
    if bool(namespace.d):
        os.chdir(namespace.d)
    # from server import FileService

    reload(FileService)
    # FileService.__init__()
    logging.debug(FileService.get_current_dir())
    FileService.change_dir(".")


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
