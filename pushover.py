#!/usr/bin/python

import httplib, urllib

conn = httplib.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
  urllib.urlencode({
    "token": "APP KEY HERE",                       # Insert app token here
    "user": "API KEY HERE",                       # Insert user token here
    "html": "1",                                # 1 for HTML, 0 to disable
    "title": "Motion Detected!",                # Title of the message
    "message": "<b>Office</b> camera!",     # Content of the message
    "sound": "siren",                           # Define the sound played	
  }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()
