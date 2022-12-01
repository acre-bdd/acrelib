import os
import sys
import logging
from termcolor import colored

log = logging.getLogger()

logging.addLevelName(23, "HIGHLIGHT")
logging.addLevelName(25, "TRACE")
logging.HIGHLIGHT = 23
logging.TRACE = 25

log.NOTSET = logging.NOTSET
log.DEBUG = logging.DEBUG
log.INFO = logging.INFO
log.HIGHLIGHT = logging.HIGHLIGHT
log.TRACE = logging.TRACE
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


logging.Logger.fatal = fatal
logging.Logger.trace = trace
logging.Logger.highlight = highlight

os.environ['FORCE_COLOR'] = "yes"

log.console = logging.StreamHandler()
log.console.setFormatter(ColoredFormatter())
log.addHandler(log.console)
log.console.setLevel(log.TRACE)
logging.getLogger().setLevel(log.DEBUG)
