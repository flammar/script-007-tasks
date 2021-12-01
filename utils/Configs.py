import argparse
import configparser
import os
import sys

import dotted_dict

from utils.ActionUtils import store_and_pipe_to
from utils.ObjectUtils import keys, setpath, getpath, get_
from utils.Singleton import singleton

DEFAULT_CONFIG = "config.ini"
_env_prefix = 'SERVER_'


def _init_settngs():
    """
    Returns:
            {"<section...>":{"<key...>":[[<default>,<test default>],[<extra keys...>],<type>,<help>,{extra options},converter]]}}
    """
    return {
        # 'config': ['config.ini'],
        'dir': [['data', '.'], ["-d"], str, "working directory (default: 'data')"],
        'log': {
            'level': ['WARNING', ["-l"], str, 'log level (default: warning)', {}, lambda s: s.upper()],
            'file': [ None, [], str, 'log file.'],  # 'server.log'
        },
        'port': [[8080, 0], ["-p"], int, "server port"],
        'autocreate': [None, [], bool, "autocreate directory if not existing"],
    }


def _init_config(my_settings):
    my_keys = keys(my_settings)
    res = {}
    in_test = _is_in_test()
    for i in my_keys:
        v = getpath(my_settings, i)[0]
        setpath(res, i, v if not isinstance(v, list) else v[1] if in_test else v[0])
    return res


def _param_name(i, prefix: str = ""):
    return prefix + i.replace(".", "_")


def get_type(slot):
    return get_(slot, 2, str)


def get_conv(slot):
    return get_(slot, 5, lambda x: x)


def _is_in_test():
    py_prog_file_name = os.path.basename(sys.argv[0])
    return py_prog_file_name.startswith('_') and 'test' in py_prog_file_name


def get_extra_keys(slot):
    return get_(slot, 1, [])


def get_help(slot, i):
    return get_(slot, 3, i.split(".").pop())


def get_extra(slot):
    return get_(slot, 4, {})


@singleton
class Config:
    settings = _init_settngs()
    params_keys = keys(settings)
    data = dotted_dict.DottedDict(_init_config(settings))

    def update_data(self, path, value):
        value and setpath(self.data, path, value)

    def __init__(self):
        self.set_data()

    def _args(self):
        parser = argparse.ArgumentParser()
        for i in self.params_keys:
            slot = getpath(self.settings, i)
            parser.add_argument(*(get_extra_keys(slot)), _param_name(i, '--'), default=getpath(self.data, i),
                                required=False, type=get_type(slot), help=(get_help(slot, i)), **(get_extra(slot)),
                                action=store_and_pipe_to((lambda j: lambda v: setpath(self.data, j, v))(i),
                                                         get_conv(slot)))
        parser.parse_args()

    def _env(self):
        for i in self.params_keys:
            self.update_data(i, os.environ.get(_param_name(i, _env_prefix).upper(), None))

    def _ini(self):
        with open(DEFAULT_CONFIG) as stream:
            ini_parser = configparser.ConfigParser()
            ini_parser.read_string('[default]\n' + stream.read())
            ini_params = dict(list((ini_parser['default'] or []).items()))
        for i in self.params_keys:
            slot = getpath(self.settings, i)
            self.update_data(i, get_conv(slot)(get_type(slot)(get_(ini_params, i))))

    def set_data(self):
        print("self.data: %s" % self.data)
        if _is_in_test():
            return
        self._ini()
        print("self.data: %s" % self.data)
        self._env()
        print("self.data: %s" % self.data)
        self._args()
        print("self.data: %s" % self.data)


config = Config().data
