

import tweepy
from numpy import random

CONSUMER_KEY = "wySdB7K0NUCp8l26wQxl7LLfA"
CONSUMER_SECRET = "8jXVDwemtooE9cep8M4pkhIYSMEPB9MyePC3V4neE1EI6YHprh"
ACCESS_KEY = "1515196716282265602-oZLOQWTLmalM49RiG1CemkAD9EQAwy"
ACCESS_SECRET = "ZwLJw6MgjGOa0ojuLKhpnMKs3PrWe24BIIqpVYlUt1VPM"

"""
    Cette fonction permet de poster des Tweets contenant les
    nouvelles installations dans un compte Twitter

"""


def post_tweets(glissades, piscines, patinoires):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    msg = " est maintenant installé dans la ville de Montréal !"
    if len(glissades) != 0:
        for i in range(len(glissades)):
            tweet = "Le glissade avec le nom : " + \
                glissades[i] + msg + "#"+chr(random.randrange(ord('a'),
                                                              ord('z') + 1))
            api.update_status(status=tweet)
    if len(piscines) != 0:
        for i in range(len(piscines)):
            tweet = "La piscines avec le nom : " + \
                piscines[i] + msg + "#"+chr(random.randrange(ord('a'),
                                                             ord('z') + 1))
            api.update_status(status=tweet)
    if len(patinoires) != 0:
        for i in range(len(patinoires)):
            tweet = "Le patinoire avec le nom : " + \
                patinoires[i] + msg + "#"+chr(random.randrange(ord('a'),
                                                               ord('z') + 1))
            api.update_status(status=tweet)
