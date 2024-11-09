import logging
from src.utils.logger_config import setup_logging, log_error

def test_setup_logging():
    logger = setup_logging()
    assert isinstance(logger, logging.Logger)

def test_log_error():
    logger = setup_logging()
    try:
        raise ValueError('テストエラー')
    except Exception as e:
        log_error(logger, e, {'test': 'context'})