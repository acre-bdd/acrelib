import os
import sys
import logging
from termcolor import colored

log = logging.getLogger()

class ColoredFormatter(logging.Formatter):

    format = "%(message)s"

    FORMATS = {
        logging.DEBUG: colored(format, "grey"),
        logging.INFO: colored(format, "white"),
        logging.WARNING: colored(format, "yellow"),
        logging.ERROR: colored(format, "red"),
        logging.CRITICAL: colored(format, "red", attrs=['bold'])
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def fatal(*args, **kwargs):
    log.critical(*args, **kwargs)
    sys.exit(255)


def trace(message, *args, **kwargs):
    log.info(colored(message, "magenta"), *args, **kwargs)


log.NOTSET = logging.NOTSET
log.DEBUG = logging.DEBUG
log.INFO = logging.INFO
log.WARNING = logging.WARNING
log.ERROR = logging.ERROR
log.CRITICAL = logging.CRITICAL
log.fatal = fatal
log.trace = trace

os.environ['FORCE_COLOR'] = "yes"

streamhandler = logging.StreamHandler()
streamhandler.setFormatter(ColoredFormatter())
log.addHandler(streamhandler)
log.setLevel(logging.INFO)
