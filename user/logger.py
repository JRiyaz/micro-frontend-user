import json
import logging
from logging.config import dictConfig

from .config import config

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "standard": {"format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"},
        "custom_formatter": {
            "format": (
                "%(asctime)s [%(processName)s: %(process)d] [%(threadName)s: %(thread)d] "
                "[%(levelname)s] %(name)s: %(message)s"
            )
        },
        # "custom_formatter": {
        #     "format": (
        #         "{'time':'%(asctime)s', 'process_name': '%(processName)s', 'process_id': '%(process)s', "
        #         "'thread_name': '%(threadName)s', 'thread_id': '%(thread)s','level': '%(levelname)s', "
        #         "'logger_name': '%(name)s', 'message': '%(message)s'}"
        #     )
        # },
    },
    "handlers": {
        "default": {
            "formatter": "standard",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",  # Default is stderr
        },
        "stream_handler": {
            "formatter": "custom_formatter",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",  # Default is stderr
        },
        "file_handler": {
            "formatter": "custom_formatter",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": "app.log",
            "maxBytes": 1024 * 1024 * 1,  # = 1MB
            "backupCount": 3,
        },
    },
    # "loggers": {
    #     "uvicorn": {"handlers": ["default", "file_handler"], "level": "TRACE", "propagate": False},
    #     "uvicorn.access": {"handlers": ["stream_handler", "file_handler"], "level": "TRACE", "propagate": False},
    #     "uvicorn.error": {"handlers": ["stream_handler", "file_handler"], "level": "TRACE", "propagate": False},
    #     "uvicorn.asgi": {"handlers": ["stream_handler", "file_handler"], "level": "TRACE", "propagate": False},
    # },
    "loggers": {
        "uvicorn": {"handlers": ["default"], "level": config.LOG_LEVEL, "propagate": False},
        "uvicorn.access": {"handlers": ["stream_handler"], "level": config.LOG_LEVEL, "propagate": False},
        "uvicorn.error": {"handlers": ["stream_handler"], "level": config.LOG_UVICORN, "propagate": False},
        "uvicorn.asgi": {"handlers": ["stream_handler"], "level": config.LOG_LEVEL, "propagate": False},
    },
}


def get_log(record):
    d = {
        "time": record.asctime,
        "process_name": record.processName,
        "process_id": record.process,
        "thread_name": record.threadName,
        "thread_id": record.thread,
        "level": record.levelname,
        "logger_name": record.name,
        "pathname": record.pathname,
        "line": record.lineno,
        "message": record.message,
    }

    if hasattr(record, "extra_info"):
        d["req"] = record.extra_info["req"]
        d["res"] = record.extra_info["res"]

    return d


class CustomJSONFormatter(logging.Formatter):
    def __init__(self, fmt):
        logging.Formatter.__init__(self, fmt)

    def format(self, record):
        logging.Formatter.format(self, record)
        return json.dumps(get_log(record), indent=2)


def setup_logging():
    dictConfig(LOGGING_CONFIG)
