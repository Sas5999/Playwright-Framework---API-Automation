from src.core.logger.logger_manager import LoggerManager


def test_logger():

    logger = LoggerManager.get_logger()

    logger.info("Framework logging initialized successfully")

    assert logger is not None