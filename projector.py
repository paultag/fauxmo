from fauxmo import HTTPSwitch
import fauxmo
import fauxmo.log
import logging


class ProjectorPower(HTTPSwitch):
    name = "testing"
    host = "http://192.168.1.50"
    on_url = "projector/power/on"
    off_url = "projector/power/off"


if __name__ == "__main__":
    fauxmo.log.logger.setLevel(logging.DEBUG)
    fauxmo.serve(ProjectorPower)
