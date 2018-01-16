import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1,1000)
    # convert num to String
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

download_web_image("https://www.picmonkey.com/_/static/images/index/picmonkey_twitter_02.24fd38f81e59.jpg")