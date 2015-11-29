import requests
from . import Loggable


class RESTAPIHandler(Loggable):
    def __init__(self, on_cmd, off_cmd):
        self.on_cmd = on_cmd
        self.off_cmd = off_cmd

    def on(self):
        r = requests.get(self.on_cmd)
        self.debug("On!")
        return r.status_code == 200

    def off(self):
        r = requests.get(self.off_cmd)
        self.debug("Off!")
        return r.status_code == 200
