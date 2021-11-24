import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--foo')
parser.add_argument('bar')
parser.parse_args('X --foo Y'.split())

params = parser.parse_args('X --foo Y'.split())
print(str(params))
parser.print_help()
