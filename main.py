#!/usr/bin/env python3

import logging
import sys

import config

import jotoapp.controllers.server
logging.basicConfig(level=logging.CRITICAL,
                    stream=sys.stdout,
                    #filename=config.LOG_FILE
                    )


jotoapp.controllers.server.run()
