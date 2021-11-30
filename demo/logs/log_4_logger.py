import logging

logging.basicConfig(encoding='utf-8', level=logging.DEBUG)
logger = logging.getLogger('myprogram')

logging.debug('my debug 🙄 message')
logging.info('my info message')

logger.warning('my warning ☝ message')
logger.error('my error 😱 message')
