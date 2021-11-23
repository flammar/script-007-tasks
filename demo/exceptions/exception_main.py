if __name__ == '__main__':
    try:
        main()
    except BaseException as err:
        # logging
        print("всё плохо {}".format(err))
