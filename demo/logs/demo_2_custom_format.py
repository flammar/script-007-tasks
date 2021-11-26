import logging
import time

format = '%(asctime)s %(name)s - %(levelname)s : %(message)s'
# format = 'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=format, filename='mylog.txt')
print('started')
logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)
logger.error('example of error message')
time.sleep(0.1)
logger.warning('example of warning message')
time.sleep(0.2)
logger.info('example of information message')
logger.debug('example of debug message')
print('finished')
