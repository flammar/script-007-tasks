import logging

logging.basicConfig(
    encoding='utf-8',
    level=logging.DEBUG,
    filename='myapp.log',
)
logging.debug('my debug 🙄 message')
logging.info('my info message')
logging.warning('my warning ☝ message')
logging.error('my error 😱 message')
