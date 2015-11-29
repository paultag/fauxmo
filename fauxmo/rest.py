

class RESTAPIHandler(object):
    def __init__(self, on_cmd, off_cmd):
        self.on_cmd = on_cmd
        self.off_cmd = off_cmd

    def on(self):
        r = requests.get(self.on_cmd)
        return r.status_code == 200

    def off(self):
        r = requests.get(self.off_cmd)
        return r.status_code == 200
