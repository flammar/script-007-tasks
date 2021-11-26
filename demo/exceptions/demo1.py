def summa(n1, n2):
    if type(n1) != 'int':
        # TODO: show stack trace
        raise TypeError('incorrect type: {}'.format(type(n1)))
    return n1 - n2


try:
    summa('a', 'b')
except (TypeError, RuntimeError) as e:
    print("error occurred {}".format(e.message))
