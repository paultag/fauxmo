import logging

logging.basicConfig()
logger = logging.getLogger('fauxmo')


class Loggable(object):
    def debug(self, *args, **kwargs):
        logger.debug(*args, **kwargs)

    def warning(self, *args, **kwargs):
        logger.warning(*args, **kwargs)
