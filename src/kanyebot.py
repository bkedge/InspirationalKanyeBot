#Brady Kedge
#May 25, 2017
#bradykedge.com

import tweepy
import time, random, os
import re
import textwrap
from time import ctime
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
    print("Getting last tweet at %s\n" % time.ctime())

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

    #check for link. If so ignore
    regex = r"(http|https)"

    if re.search(regex, txt, re.IGNORECASE):
        print("Tweet is a link, skipping\n")
        return

    #Dont want paragraph tweets
    if len(txt) > 50:
        print("Tweet is too long to look good\n")
        return

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
        #lines = textwrap.wrap(txt, width = 40)
        #current_h = 50
        #pad = 10

        #Border

        #Old style for border. May not be applicable with wrapping text. Need to find another way
        draw.text((((width - textWidth)/2)-1, ((height-textHeight)/2)-1), txt, font = font, fill = "black")
        draw.text((((width - textWidth)/2)+1, ((height-textHeight)/2)-1), txt, font = font, fill = "black")
        draw.text((((width - textWidth)/2)-1, ((height-textHeight)/2)+1), txt, font = font, fill = "black")
        draw.text((((width - textWidth)/2)+1, ((height-textHeight)/2)+1), txt, font = font, fill = "black")

        #Draw Text
        draw.text(((width - textWidth)/2, (height-textHeight)/2), txt, font = font, fill = "white")

        '''
        for line in lines:
            textWidth, textHeight = draw.textsize(line, font = font)
            #Old way
            #draw.text(((width - textWidth)/2, (height-textHeight)/2), txt, font = font, fill = "white")
            draw.text(((width - textWidth)/2, (height-textHeight)/2), line, font = font, fill = "white")
            
            #Draw the text
            #draw.text(((width - textWidth)/2, current_h), line, font = font, fill = "white")
            #current_h += textHeight + pad
        '''

        #Save it
        temp.save('/home/brady/Code/Python/Twitter/KanyeBot/img/final.jpg')

        #Upload picture
        api.update_with_media('/home/brady/Code/Python/Twitter/KanyeBot/img/final.jpg')
        print("Posted tweet\n")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    while(1):
        try:
            #Try stuff
            getTweet()
            time.sleep(600)
        except Exception as e:
            print(e)
