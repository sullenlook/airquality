#!/usr/bin/python
# -*- coding: utf-8 -*-

from plugin import *
import json
import urllib2
import re

class airQuality(Plugin):
    
    @register("de-DE", ".*Luft.*")
    @register("en-US", ".*air.*")
    def airQuality(self, speech, language):
        url = "http://pipes.yahoo.com/pipes/pipe.run?_id=80b657af97c696c411220f31ef1380e6&_render=json"
        jsonString = None
        air = "Unknown"
        try:
            jsonString = urllib2.urlopen(url, timeout=3).read()
            if jsonString != None:
                response = json.loads(jsonString)
                air = re.match(".*\d+, (\w+).*", response["value"]["items"][0]['content']).group(1)
        except:
            pass
        self.say("The air in Beijing is " + air)
        self.complete_request()
        