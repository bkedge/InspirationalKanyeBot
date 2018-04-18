#Brady Kedge
#May 25, 2017
#bradykedge.com

import tweepy
import time, random, os
import re
import textwrap
from PIL import Image, ImageDraw, ImageFont
from PIL import ImageFile
from config import *

#Setup OAuth
auth = tweepy.OAuthHandler(Consumer_Key, Consumer_Secret)

auth.set_access_token(Access_Key, Access_Secret)

api = tweepy.API(auth)

#Backup to get User ID
#user = api.get_user(screen_name = 'OfficiaIKanye')
#user = api.get_user(screen_name = 'kanyewest')

KanyeID = 74346390
lastTweet = None

#Gets latest tweet
def getTweet():

    global lastTweet

    #Get most recent tweet
    recentTweet = api.user_timeline('kanyewest')[0]
    print("Getting last tweet\n")

    #If tweet is new make a new picture
    if recentTweet != lastTweet:
        print("New tweet found, making photo\n")
        makePic(recentTweet)
        lastTweet = recentTweet
    else:
        print("Tweet already found\n")

#Makes picture
def makePic(newTweet):
    txt = newTweet.text
    txt.upper()
    print("Photo text is: " + newTweet.text + "\n")
    path = r"/home/brady/Code/Python/Twitter/KanyeBot/img"

    #Get pictures
    pic = random.choice(os.listdir(path))
    imgPath = os.path.join(path, pic)
    loadPath = os.path.abspath(imgPath)
    filename = 'temp.jpg'

    font = ImageFont.truetype("/usr/share/fonts/truetype/DejaVuSans-Bold.ttf", 55)

    print("Random Picutre is: " + pic + "\n")
    print("Image path is: " + loadPath)

    try:
        #Setup image and text
        img = Image.open(loadPath)
        temp = img.copy()
        draw = ImageDraw.Draw(temp)
        width, height = temp.size
        textWidth, textHeight = draw.textsize(txt, font = font)

        #Setup wrapping
        lines = textwrap.wrap(txt, width = 40)

        #Border
        #draw.text((((width - textWidth)/2)-1, ((height-textHeight)/2)-1), txt, font = font, fill = "black")
        #draw.text((((width - textWidth)/2)+1, ((height-textHeight)/2)-1), txt, font = font, fill = "black")
        #draw.text((((width - textWidth)/2)-1, ((height-textHeight)/2)+1), txt, font = font, fill = "black")
        #draw.text((((width - textWidth)/2)+1, ((height-textHeight)/2)+1), txt, font = font, fill = "black")

        #Draw Text
        for line in lines:
            draw.text(((width - textWidth)/2, (height-textHeight)/2), txt, font = font, fill = "white")

        #Save it
        temp.save('/home/brady/Code/Python/Twitter/KanyeBot/img/final.jpg')

        #Upload picture
        api.update_with_media('/home/brady/Code/Python/Twitter/KanyeBot/img/final.jpg')
        print("Posted tweet\n")
    except Exception, e:
        print(e)

if __name__ == "__main__":
    while(1):
        try:
            #Try stuff
            getTweet()
            time.sleep(600)
        except Exception, e:
            print(e)
