import os
import sys
import logging
from termcolor import colored


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


class ColoredLogger(logging.Logger):

    NOTSET = logging.NOTSET
    DEBUG = logging.DEBUG
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    CRITICAL = logging.CRITICAL

    def __init__(self, level=logging.NOTSET):
        super().__init__(level)

        self.streamhandler = logging.StreamHandler()
        self.streamhandler.setFormatter(ColoredFormatter())
        self.addHandler(self.streamhandler)
        self.setLevel(logging.INFO)

    def setLevel(self, level):
        super().setLevel(level)
        self.streamhandler.setLevel(level)

    def fatal(self, *args, **kwargs):
        self.critical(*args, **kwargs)
        sys.exit(255)

    def trace(self, message):
        self.info(colored(message, "magenta"))


os.environ['FORCE_COLOR'] = "yes"

logging.setLoggerClass(ColoredLogger)
log = logging.getLogger("acre")

