import logging

logging.basicConfig(encoding='utf-8', level=logging.DEBUG)
logging.debug('my debug 🙄 message')
logging.info('my info message')
logging.warning('my warning ☝ message')
logging.error('my error 😱 message')

# use formatting
logging.debug('got %i bytes', 5)

# this is often used too:
logging.info('{} + {} = {}'.format(1, 3, 4))
