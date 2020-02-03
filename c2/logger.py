import os
import logging
import loggly.handlers

logging_key = os.getenv('LOGGING_KEY')

if logging_key:
    print('Using loggly for log capture')
    logurl = f'https://logs-01.loggly.com/inputs/{logging_key}/tag/python'
    handler = loggly.handlers.HTTPSHandler(url=logurl)
    handler.setLevel(logging.INFO)
    chandler = logging.StreamHandler()
    chandler.setLevel(logging.INFO)

    logger = logging.getLogger('root')
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    logger.addHandler(chandler)
else:
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger('root')