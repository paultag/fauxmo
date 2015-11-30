from fauxmo import UPNPBroadcastResponder, Poller, Fauxmo
from fauxmo.log import logger, Loggable
import logging

import time
import sys


def serve(*devices):
    poller = Poller()
    responder = UPNPBroadcastResponder()
    responder.init_socket()
    poller.add(responder)

    for device in devices:
        responder.add_device(device(poller=poller))

    while True:
        try:
            poller.poll(100)
            time.sleep(0.1)
        except Exception as e:
            logger.error(e)
            break
