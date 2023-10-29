import json
import os
import urllib
from urllib.request import urlopen, urlretrieve

BingUrl = "https://www.bing.com/"
BingJSON_URL = BingUrl + "HPImageArchive.aspx?format=js&idx=0&n=1&mkt=pl-PL"
with urllib.request.urlopen(BingJSON_URL) as url:
    data = json.load(url)
    imgUrl = data["images"][0]["url"]
    urlretrieve(BingUrl + imgUrl, "wallpaper.jpg")
