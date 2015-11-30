import requests
import os.path
from . import Loggable, Fauxmo


class Switch(Fauxmo):
    def __init__(self, poller, ip_address=None, port=0, **kwargs):
        self.port = port
        super(Switch, self).__init__(
            self.name,
            ip_address=ip_address,
            poller=poller,
            port=port,
            action_handler=self,
        )

    def on(self, *args, **kwargs):
        raise NotImplementedError()

    def off(self, *args, **kwargs):
        raise NotImplementedError()


class HTTPSwitch(Switch):
    def request(self, url):
        r = requests.get(url)
        return r.status_code == 200

    def on(self):
        return self.request(os.path.join(self.host, self.on_url))

    def off(self):
        return self.request(os.path.join(self.host, self.off_url))
