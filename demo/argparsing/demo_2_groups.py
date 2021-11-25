import argparse

__version__ = "0.1.0"


# python demo/argparsing/demo_2_groups.py -v
# python demo/argparsing/demo_2_groups.py -h
# python demo/argparsing/demo_2_groups.py create -h
# python demo/argparsing/demo_2_groups.py create abc.txt
# python demo/argparsing/demo_2_groups.py read abc.txt

def parse_args():
    """Command line parser."""

    debug_parser = argparse.ArgumentParser(add_help=False)

    debug_options = debug_parser.add_argument_group("Debug Options")
    debug_options.add_argument('-l', '--logfile', metavar='filename', type=argparse.FileType('wb', 0), default='-',
                               help='Specify the logfile (default: <stdout>)')
    group = debug_options.add_mutually_exclusive_group()
    group.add_argument('-q', '--quiet', action='store_true', help='disable logging')
    group.add_argument('-v', '--verbose', action='store_true', help='enhanced logging')
    group.add_argument('-d', '--debug', action='store_true', help='extensive logging')

    parser = argparse.ArgumentParser(description='Actions ')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)
    parser.add_argument('-f', '--folder', help='work dir', default="test_folder")

    subparsers = parser.add_subparsers(help='sub-commands')

    create_parser = subparsers.add_parser('create', help='Create file', parents=[debug_parser])
    create_parser.add_argument('file_name', nargs='?', help='New file', default="test.txt")
    create_parser.add_argument('mode', nargs='?', help='Mode to open file', default="rw")

    read_parser = subparsers.add_parser('read', help='Read file', parents=[debug_parser])
    read_parser.add_argument('file_name', help='Read file', default="test.txt")

    list_parser = subparsers.add_parser('list', help='Show files', parents=[debug_parser])

    create_parser.set_defaults(func=create_file)
    read_parser.set_defaults(func=read_file)
    list_parser.set_defaults(func=get_files)

    options = parser.parse_args()
    return options


def create_file(options):
    print(f"create_file '{options.file_name}' with mode '{options.mode}'")


def read_file(options):
    print(f"read_file '{options.file_name}'")


def get_files():
    print('get_files')


def main():
    options = parse_args()
    options.func(options)


if __name__ == '__main__':
    main()
