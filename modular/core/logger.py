

# app/core/logger.py

import logging

logger = logging.getLogger(__name__)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
# handler = logging.StreamHandler()
# Create file handler
handler = logging.FileHandler('app.log')

handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
