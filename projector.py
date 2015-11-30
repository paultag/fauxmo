from fauxmo import HTTPSwitch, Switch
import fauxmo
import fauxmo.log
import logging
import pychromecast
import requests


class ChromecastSwitch(Switch):
    def get_chromecast(self):
        return pychromecast.get_chromecasts_as_dict().get(self.chromecast)

    def on(self):
        self.get_chromecast().play_media(self.url, self.media_type)
        return True

    def off(self):
        self.get_chromecast().quit_app()
        return True


class ProjectorPower(HTTPSwitch):
    name = "projector"
    host = "http://192.168.1.50"
    on_url = "projector/power/on"
    off_url = "projector/power/off"


class HackersSwitch(ChromecastSwitch):
    name = "hackers"
    url = "http://192.168.1.50/hackers/hackers.mp4"
    media_type = "video/mp4"
    chromecast = "Projector"

    def on(self):
        requests.get("http://192.168.1.50/projector/power/on")
        return super(HackersSwitch, self).on()

    def off(self):
        return super(HackersSwitch, self).off()


if __name__ == "__main__":
    fauxmo.log.logger.setLevel(logging.DEBUG)
    fauxmo.serve(ProjectorPower, HackersSwitch)
