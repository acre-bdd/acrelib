import os
import sys
import logging
from termcolor import colored

log = logging.getLogger()

log.NOTSET = logging.NOTSET
log.DEBUG = logging.DEBUG
log.INFO = logging.INFO
log.HIGHLIGHT = logging.INFO + 3
log.TRACE = logging.INFO + 5
log.WARNING = logging.WARNING
log.ERROR = logging.ERROR
log.CRITICAL = logging.CRITICAL


class ColoredFormatter(logging.Formatter):

    format = "%(message)s"

    FORMATS = {
        logging.DEBUG: colored(format, "grey"),
        logging.INFO: colored(format, "white"),
        log.HIGHLIGHT: colored(format, "cyan"),
        log.TRACE: colored(format, "magenta"),
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


def trace(*args, **kwargs):
    log.log(log.TRACE, *args, **kwargs)


def highlight(*args, **kwargs):
    log.log(log.HIGHLIGHT, *args, **kwargs)


log.fatal = fatal
log.trace = trace
log.highlight = highlight

os.environ['FORCE_COLOR'] = "yes"

streamhandler = logging.StreamHandler()
streamhandler.setFormatter(ColoredFormatter())
log.addHandler(streamhandler)
log.setLevel(logging.INFO)
