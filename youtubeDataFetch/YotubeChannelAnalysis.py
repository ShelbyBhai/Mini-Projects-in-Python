import urllib.request

import json

import GuiFile

key = "AIzaSyBZ8vlK9ImCvk0rUUxzclKqeC03z70cECk"


def Channel_date():
    channel_name = GuiFile._input.get()
    data = urllib.request.urlopen(
        "https://www.googleapis.com/youtube/v3/channels?part=statistics&id=" + channel_name + "&key=" + key).read()
    subCount = json.loads(data)['items'][0]['statistics']['subscriberCount']
    viewCount = json.loads(data)['items'][0]['statistics']['viewCount']
    videoCount = json.loads(data)['items'][0]['statistics']['videoCount']
    GuiFile.l2.config(text=subCount)
    GuiFile.l4.config(text=viewCount)
    GuiFile.l6.config(text=videoCount)
