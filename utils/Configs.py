import argparse
import configparser
import os

import dotted_dict

from utils.ActionUtils import store_and_pipe_to
from utils.ObjectUtils import keys, setpath, getpath, get_
from utils.Singleton import singleton

DEFAULT_CONFIG = "config.ini"

_env_prefix = 'SERVER'


def _init_settngs():
    """
    Returns:
            {"<section...>":{"<key...>":[<default>,[<extra keys...>],<type>,<help>,{extra options},converter]]}}
    """
    return {
        # 'config': ['config.ini'],
        'dir': ['data', ["-d"], str, "working directory (default: 'data')"],
        'log': {
            'level': ['warning', ["-l"], str, 'log level (default: warning)', {}, lambda s: s.upper()],
            'file': [None, [], str, 'log file.'],  # 'server.log'
        },
        'port': [8080, ["-p"], int, "server port"],
    }


def _init_config(my_settings):
    my_keys = keys(my_settings)
    res = {}
    for i in my_keys:
        setpath(res, i, getpath(my_settings, i)[0])
    return res


def _param_name(i):
    return i.replace(".", "_")


@singleton
class Config:
    settings = _init_settngs()
    params_keys = keys(settings)
    data = dotted_dict.DottedDict(_init_config(settings))

    # params_keys = ['dir', 'log_level', 'log_file', 'port']
    params = [['dir', 'data'], ['log_level', 'warning'], ['log_file', None], ['port', 8080]]

    def __init__(self):
        self.set_data()

    def _read_args(self):

        print("_read_args: start: data: %s" % self.data)
        parser = argparse.ArgumentParser()
        for i in self.params_keys:
            slot = getpath(self.settings, i)
            parser.add_argument(*(get_(slot, 1, [])), '--' + _param_name(i), default=getpath(self.data, i),
                                required=False,
                                type=get_(slot, 2, str), help=get_(slot, 3, slot), **(get_(slot, 4, {})),
                                action=store_and_pipe_to(lambda v: setpath(self.data, i, v),
                                                         get_(slot, 5, lambda x: x)))
        parser.parse_args()
        print("_read_args: end: data: %s" % self.data)

    def _read_env(self):
        print("_read_env: start: data: %s" % self.data)
        for i in self.params_keys:
            self.update_data(i, os.environ.get((_env_prefix + '_' + _param_name(i)).upper(), None))
        print("_read_env: end: data: %s" % self.data)

    def _read_ini(self):
        print("_read_ini: start: data: %s" % self.data)
        ini_params = []
        with open(DEFAULT_CONFIG) as stream:
            ini_parser = configparser.ConfigParser()
            ini_parser.read_string('[default]\n' + stream.read())
            ini_params = dict(list((ini_parser['default'] or []).items()))
        for i in self.params_keys:
            # if i in ini_params:
            self.update_data(i, get_(ini_params, i))
        # for section in parser.sections():
        #     for k, v in parser[section]с("rrrr"):
        #         self.data[k] = v
        print("_read_ini: end: data: %s" % self.data)

    def update_data(self, path, value):
        if value:
            setpath(self.data, path, value)

    def set_data(self):
        print("set_data: start: data: %s" % self.data)
        self._read_ini()
        self._read_env()
        self._read_args()
        print("set_data: end: data: %s" % self.data)


config_data = Config()
