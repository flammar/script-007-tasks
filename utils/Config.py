import argparse
import configparser
import logging
import os

import dotted_dict

from utils.Singleton import singleton


class LayeredConfig:
    """
    Configuration storage that reads data from (from high to low priority):
    - command line
    - environment variables
    - configuration file
    If a value for specific key not found then default value is used.

    You can use dot notation to access specific values.

    There are the following values:
    config    - name of configuration file
    dir       - directory to keep files
    log.level - logging level
    log.file  - log filename
    port      - port for web-server
    """

    def __init__(self) -> None:
        self._logger = logging.getLogger('config')
        self._env_prefix = 'SERVER'
        self._arg_parser = None
        self._args = None
        self.data = dotted_dict.DottedDict()
        self._set_defaults()
        self._create_parser()

    def _set_defaults(self) -> None:
        """Set default values."""
        self.data.update({
            'config': 'config.ini',
            'dir': 'data',
            'log': {
                'level': 'warning',
                'file': None,  # 'server.log'
            },
            'port': 8080,
        })

    def _read_config(self) -> None:
        """Read values from configuration file."""
        if not os.path.exists(self.data.config):
            self._logger.info(f"config file '{self.data.config}' not found")
            return
        with open(self.data.config) as stream:
            ini_parser = configparser.ConfigParser()
            ini_parser.read_string('[default]\n' + stream.read())
            ini_params = ini_parser['default']
            self.data.dir = ini_params.get('dir', self.data.dir)
            self.data.log.level = ini_params.get('log.level', self.data.log.level)
            self.data.log.file = ini_params.get('log.file', self.data.log.file)
            self.data.port = ini_params.getint('port', self.data.port)

    def _read_envvars(self) -> None:
        """Read values from environment variables."""
        prefix = self._env_prefix.upper()
        self.data.config = os.getenv(f'{prefix}_CONFIG', self.data.config)
        self.data.dir = os.getenv(f'{prefix}_DIR', self.data.dir)
        self.data.log.level = os.getenv(f'{prefix}_LOG_LEVEL', self.data.log.level)
        self.data.log.file = os.getenv(f'{prefix}_LOG_FILE', self.data.log.file)
        self.data.port = int(os.getenv(f'{prefix}_PORT', self.data.port))

    def _create_parser(self) -> None:
        """Create command line parser.

        Command line options:
        -d --dir       - working directory (absolute or relative path).
           --log-level - set verbosity level
        -l --log-file  - set log filename
        -p --port      - port for web-server
        """
        self._arg_parser = argparse.ArgumentParser()
        self._arg_parser.add_argument('-c', '--config', type=str,
                                      help=f'config filename (default: {self.data.config})')
        self._arg_parser.add_argument('-d', '--dir', type=str,
                                      help=f'working directory (default: {self.data.dir})')
        self._arg_parser.add_argument('--log-level', choices=['debug', 'info', 'warning', 'error'],
                                      help=f'Log level to console (default: {self.data.log.level})')
        self._arg_parser.add_argument('-l', '--log-file', type=str, help='Log file')
        self._arg_parser.add_argument('-p', '--port', type=int, help='Port for web-server')

    def _parse_arguments(self) -> None:
        """Helper method for argument parsing."""
        self._args = self._arg_parser.parse_args()

    def _read_arguments(self) -> None:
        if self._args.dir:
            self.data.dir = self._args.dir
        if self._args.log_level:
            self.data.log.level = self._args.log_level
        if self._args.log_file:
            self.data.log.file = self._args.log_file
        if self._args.port:
            self.data.port = self._args.port

    def _validate(self) -> None:
        pass

    def update(self) -> None:
        """Read values from different sources.

        CLI arguments may redefine config filename, thus we need to split the whole process of config file processing
        to separate steps:

        - _create_parser (done once)
        - _parse_arguments (find custom config filename if any)
        - _read_arguments (read values from CLI arguments)
        """
        self._set_defaults()
        self._read_envvars()
        self._parse_arguments()
        if self._args.config:
            self.data.config = self._args.config
        self._read_config()
        self._read_arguments()
        self._validate()

    def dump_config(self):
        # print to sys.file.stdout or specified file
        pass


@singleton
class SingletonConfig:

    def __init__(self) -> None:
        self.layered_config = LayeredConfig()
        self.layered_config.update()


config = SingletonConfig().layered_config.data
