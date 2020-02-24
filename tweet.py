import tweepy
from config import getConfig

config = getConfig()

auth = tweepy.OAuthHandler(config["twitter_api_key"], config["twitter_api_secret"])
auth.set_access_token(config["twitter_access_token"], config["twitter_access_token_secret"])

api = tweepy.API(auth)

def tweet(title, filename):
    api.update_with_media(filename, title) #use media function