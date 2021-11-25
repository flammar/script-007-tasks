#!/usr/bin/env python3
import argparse
import os
import sys
# from server import FileService


def main():
    argv = sys.argv
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', help='set current directory', required=False)
    namespace = parser.parse_args()
    # print(FileService.get_current_dir())
    # FileService.change_dir(".")
    if bool(namespace.d):
        os.chdir(namespace.d)
    from server import FileService
    # FileService.__init__()
    # print(FileService.get_current_dir())
    # FileService.change_dir(".")


if __name__ == '__main__':
    main()
