from logging.config import dictConfig

from .config import config

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,  # important when using uvicorn
    "formatters": {
        "default": {
            "format": "[%(asctime)s] [%(levelname)s] %(name)s: %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
    },
    "loggers": {
        "uvicorn": {
            "handlers": ["console"],
            "level": config.LOG_UVICORN,
        },
        "uvicorn.error": {
            "level": "ERROR",
        },
        "uvicorn.access": {
            "handlers": ["console"],
            "level": "INFO",
        },
        "myapp": {  # your custom logger
            "handlers": ["console"],
            "level": config.LOG_LEVEL,
            "propagate": False,
        },
    },
}


def setup_logging():
    dictConfig(LOGGING_CONFIG)
