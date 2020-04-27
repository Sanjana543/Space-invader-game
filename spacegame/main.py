import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1,1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url,full_name)

download_web_image("https://t7.rbxcdn.com/bbd46fc8bcdcec9dbb4b53f7f153f910")