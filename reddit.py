import praw
import json
from config import getConfig

config = getConfig()

reddit = praw.Reddit(
    client_id=config["reddit_client_id"],
    client_secret=config["reddit_client_secret"],
    password=config["reddit_password"],
    username=config["reddit_username"],
    user_agent=config["reddit_user_agent"],
)

try:
    open("alreadyPosted.txt", 'r')
except FileNotFoundError:
    open("alreadyPosted.txt", 'w')

def getHot():
    alreadyPosted = open("alreadyPosted.txt", 'r').read().split("\n")
    for submission in reddit.subreddit(config["subreddit"]).hot(limit=6):
        url = submission.url
        if url.endswith(".png") or url.endswith(".jpg") or url.endswith(".jpeg") or url.endswith(".gif") or url.endswith(".mp4"):
            if url not in alreadyPosted:
                with open("alreadyPosted.txt", 'a') as f:
                    f.write(url+"\n")
                return submission
            else:
                return None