import logging

from app.views import *  # noqa
from app.setup import app

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info("Starting tv-backlight-api")
    app.run(host='0.0.0.0', debug=True, port=8001)
