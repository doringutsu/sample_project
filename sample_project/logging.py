import logging
import logging.config

from sample_project import settings


def configure_logging():
    logging.config.dictConfig(
        {
            'version': 1,
            'disable_existing_loggers': False,
            'formatters': {
                'sample_project': {
                    'format': '%(asctime)s - [%(levelname)s] %(name)s: %(message)s',
                },
            },
            'handlers': {
                'console': {
                    'level': 'DEBUG',
                    'class': 'logging.StreamHandler',
                    'formatter': 'sample_project',
                    'stream': 'ext://sys.stdout'
                },
                'scrapy': {
                    'level': 'DEBUG',
                    'class': 'logging.StreamHandler',
                    'formatter': 'sample_project',
                    'stream': 'ext://sys.stdout'
                }
            },
            'loggers': settings.LOGGERS
        }
    )


configure_logging()


def logger(name):
    return logging.getLogger(name)
