import logging
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '%(asctime)s %(name)s - %(levelname)s : %(message)s',
        },
        'to_file': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
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
            'filename': 'myapp.log',
            'maxBytes': 500,
            'backupCount': 3,
            'level': 'DEBUG',
        },
    },
    'root': {
        'level': 'DEBUG',
        'handlers': ['console', 'file'],
    }
})

print('started')
logger = logging.getLogger('myprogram')
logger.error('example of error message')
logger.warning('example of warning message')
logger.info('example of information message')
logger.debug('example of debug message')
print('finished')
