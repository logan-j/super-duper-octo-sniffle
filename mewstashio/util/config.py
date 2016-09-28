import ConfigParser

from util import log

def make(filepath=None):
    config = ConfigParser.ConfigParser()

    try:
        config.read(filepath)
    except Exception as e:
        log.notice(e)
        raise

    return config
