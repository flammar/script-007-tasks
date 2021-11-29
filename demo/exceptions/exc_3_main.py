import sys

if __name__ == '__main__':
    try:

        # main()
        pass

    except KeyboardInterrupt:
        sys.exit('\nERROR: Interrupted by user')
    except BaseException as err:
        print("всё плохо {}".format(err))
        sys.exit(1)
