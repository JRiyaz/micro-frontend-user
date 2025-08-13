import json
import logging
from logging.config import dictConfig

from .config import config

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
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
            "level": config.LOG_LEVEL,
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
    # "loggers": {
    #     "uvicorn": {"handlers": ["default"], "level": config.LOG_LEVEL, "propagate": False},
    #     "uvicorn.access": {"handlers": ["stream_handler"], "level": config.LOG_LEVEL, "propagate": False},
    #     "uvicorn.error": {"handlers": ["stream_handler"], "level": config.LOG_UVICORN, "propagate": False},
    #     "uvicorn.asgi": {"handlers": ["stream_handler"], "level": config.LOG_LEVEL, "propagate": False},
    # },
    "root": {"handlers": ["stream_handler"], "level": "NOTSET"},
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


corr_logger = {
    "disable_existing_loggers": False,
    "filters": {"custom_filter": {"()": "jivacore.logger.log.LogFilter"}},
    "formatters": {
        "basic": {"datefmt": "%d %b %y %H:%M:%S", "format": "%(asctime)s %(name)s %(levelname)s: %(message)s"},
        "extended": {
            "datefmt": "%d %b %y %H:%M:%S",
            "format": "%(asctime)-15s %(name)-5s %(levelname)-8s %(message)s: http_method=%(http_method)-6s user=%(user)s host=%(host)s user_agent=%(user_agent)s remote_addr=%(remote_addr)s request_id=%(request_id)s",
        },
    },
    "handlers": {
        "StreamHandler": {
            "class": "logging.StreamHandler",
            "filters": ["custom_filter"],
            "formatter": "extended",
            "level": "DEBUG",
            "stream": "ext://sys.stdout",
        }
    },
    "root": {"handlers": ["StreamHandler"], "level": "NOTSET"},
    "version": 1,
}
