import os


def print_all_vars():
    for k, v in sorted(os.environ.items()):
        print(f'{k}={v}')


def create_var():
    # only for current run of the program
    os.environ['KEY_THAT_MIGHT_EXIST'] = 'myvalue'


def print_single_var():
    homevar = 'HOME' if os.name == 'posix' else 'USERPROFILE'
    print('home dir is', os.environ[homevar])


def get_keyerror():
    # raise a `KeyError` if a key is not present
    print(os.environ['KEY_THAT_MIGHT_EXIST'])


def get_keyerror_workaround():
    if 'KEY_THAT_MIGHT_EXIST' in os.environ:
        print(os.environ['KEY_THAT_MIGHT_EXIST'])


def get_none():
    # return `None` if a key is not present
    print(os.environ.get('KEY_THAT_MIGHT_EXIST'))


def get_default():
    # give a default value instead of `None`
    print(os.getenv('KEY_THAT_MIGHT_EXIST', 'my_default_value'))


create_var()
print_all_vars()
print_single_var()

get_keyerror()
get_keyerror_workaround()
get_none()
get_default()
