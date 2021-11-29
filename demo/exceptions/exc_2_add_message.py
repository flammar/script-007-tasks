def func1():
    raise RuntimeError("func1 error")


def func2():
    try:
        func1()
    except RuntimeError as err:
        # do something additional
        pass
        # append error context
        err.args += ('func2 error',)
        raise


def main():
    try:
        func2()
    except RuntimeError as err:
        print(f"main: {err.args}")
        for message in err.args:
            print(f"main: {message}")


if __name__ == '__main__':
    main()
