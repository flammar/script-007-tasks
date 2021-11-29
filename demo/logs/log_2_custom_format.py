import logging
import time

fmt1 = '%(asctime)s %(name)s - %(levelname)s : %(message)s'
fmt2 = '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=fmt1)

print('started')
logging.debug('my debug 🙄 message')
time.sleep(0.1)
logging.info('my info message')
time.sleep(0.2)
logging.warning('my warning ☝ message')
logging.error('my error 😱 message')
print('finished')
