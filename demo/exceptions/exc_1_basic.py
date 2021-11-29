import sys
import traceback


def div(n1, n2):
    if type(n1) != int:
        raise TypeError(f'incorrect type: {type(n1)}')
    return n1 / n2


try:
    # TODO: show stack trace
    div(1, 0)
    div('a', 'b')
except ZeroDivisionError as e:  # only one exception here
    print(f'error occurred: {e}')
    print('-' * 60)
    traceback.print_exc(file=sys.stdout)
    print('-' * 60)
except (TypeError, RuntimeError) as e:  # few exceptions here
    print(f'error occurred: {e}')
