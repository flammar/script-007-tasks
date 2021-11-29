from logging.config import dictConfig


def logger_setup():
    dictConfig({
        'version': 1,
        'formatters': {
            'default': {
                'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
            },
            'to_file': {
                'format': '!!! [%(asctime)s] %(levelname)s in %(module)s: %(message)s',
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'INFO',
                'formatter': 'default',
                'stream': 'ext://sys.stdout',
            },
            'file': {
                'class': 'logging.handlers.RotatingFileHandler',
                'formatter': 'to_file',
                'filename': 'server.log',
                'maxBytes': 500,
                'backupCount': 3,
                'level': 'DEBUG',
            },
        },
        'root': {
            'level': 'DEBUG',
            'handlers': ['console', 'file'],
        },
        'loggers': {
            "server.FileService":
                {
                    'level': 'DEBUG',
                    'handlers': ['console', 'file'],
                }
        },
    })