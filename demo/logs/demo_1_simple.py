import logging

logging.basicConfig()
logger = logging.getLogger('myprogram')
logger.setLevel(logging.DEBUG)
logging.error('example of error message / logging')
logger.critical('example of critical message / logger')
logger.error('example of error message / logger')
logger.warning('example of warning message')
logger.info('example of information message')
logger.debug('example of debug message')

# use formatting
logger.debug('get %i bytes', 5)

# and often used:
logging.info('{} + {} = {}'.format(1, 3, 4))
