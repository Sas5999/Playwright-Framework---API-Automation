import logging

from src.core.config_manager.config_manager import ConfigManager


class LoggerManager:

    _logger = None

    @classmethod
    def get_logger(cls, env="dev"):

        if cls._logger is None:

            config = ConfigManager(env=env)

            log_level = config.get("log_level")

            logger = logging.getLogger(
                "PlaywrightFrameworkLogger"
            )

            logger.setLevel(
                getattr(logging, log_level.upper())
            )

            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s"
            )

            file_handler = logging.FileHandler(
                "logs/framework.log"
            )

            file_handler.setFormatter(formatter)

            console_handler = logging.StreamHandler()

            console_handler.setFormatter(formatter)

            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

            cls._logger = logger

        return cls._logger