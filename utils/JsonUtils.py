from typing import Callable


def add_conv(cond: Callable[[object], bool], conv: Callable[[object], object],
             base: Callable[[object], object] = lambda x: x) -> Callable[[object], object]:
    # def res(my_input: object) -> object:
    return lambda my_input: conv(my_input) if cond(my_input) else base(my_input)
