import argparse


# See https://docs.python.org/3.10/library/argparse.html#argparse.Action
class FooAction(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs is not None:
            raise ValueError("nargs not allowed")
        super().__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        print('%r %r %r' % (namespace, values, option_string))
        new_value = int(values) + 1
        setattr(namespace, self.dest, new_value)


parser = argparse.ArgumentParser()
parser.add_argument('-p', '--port',
                    type=int,
                    default=8080,
                    action=FooAction,
                    help='Server port',
                    )

params = parser.parse_args()
print(str(params))
print("server port is {}".format(params.port))
