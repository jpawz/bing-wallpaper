import json
import urllib3

retries = urllib3.Retry(total=5, backoff_factor=10)
http = urllib3.PoolManager(retries=retries)
BingUrl = "https://www.bing.com/"
BingJSON_URL = BingUrl + "HPImageArchive.aspx?format=js&idx=0&n=1&mkt=pl-PL"
response = http.request("GET", BingJSON_URL)

if response.status == 200:
    data = json.loads(response.data.decode("utf-8"))
    imgUrl = data["images"][0]["url"]

    wallpaper = http.request("GET", BingUrl + imgUrl)
    if wallpaper.status == 200:
        with open("wallpaper.jpg", "wb") as file:
            file.write(wallpaper.data)