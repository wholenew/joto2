import logging
import sys

import config

import jotoapp.controllers.server
logging.basicConfig(level=logging.INFO,
                    stream=sys.stdout,
                    #filename=config.LOG_FILE
                    )


if __name__ == '__main__':
    jotoapp.controllers.server.run()
