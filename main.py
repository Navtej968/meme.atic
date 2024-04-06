from memeGenerator import ScrapMemes
from ensta import Host
import requests
from PIL import Image
import urllib.request
import time
import os

def get_meme():
  memeinfo = ScrapMemes()
  print(memeinfo)
  url = memeinfo["url"]
  urllib.request.urlretrieve(url,"meme.jpg")
  img = Image.open("meme.jpg")
  img.save("meme.jpg")
  caption = f". \n Stolen from: r/{memeinfo['subreddit']} \n {memeinfo['title']} \n\n\n\n #meme #reddit #supposedly#funny#dankmemes#memedaily#lmao#offensivememes#cringe#idk" 
  print(caption)
  return caption
def upload_meme(caption):
  host = Host(os.getenv("USERNAME"),os.getenv("pass"))
  upload_id = host.get_upload_id("meme.jpg")
  host.upload_photo(upload_id ,caption)
def main():
  while(True):
    try:
      caption = get_meme()
      upload_meme(caption)
      time.sleep(3000)
    except Exception as e:
      main()



main()