import structlog

from app.setup import app
from app.views import *  # noqa

logger = structlog.getLogger(__name__)

if __name__ == '__main__':
    logger.info("Starting tv-backlight-api")
    app.run(host='0.0.0.0', debug=True, port=8001)
