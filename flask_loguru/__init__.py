from config import LoguruConfig
from loguru import logger

logger.add(**LoguruConfig())
