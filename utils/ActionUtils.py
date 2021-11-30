import argparse
from typing import Callable


def store_converted_with(func: Callable):
    class Action1(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            print('%r %r %r' % (namespace, values, option_string))
            new_value = func(values)
            setattr(namespace, self.dest, new_value)

    return Action1


def store_and_pipe_to(func: Callable, conv: Callable = lambda x: x):

    class Action1(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            if values:
                new_value = conv(values)
                func(new_value)
                setattr(namespace, self.dest, new_value)

    return Action1
