import sys, os
from reddit import getHot
from tweet import tweet
from time import sleep


import urllib.request
while True:
    post = getHot()

    if post != None:
        sys.stdout.write("Post found: "+post.url+"\n")
        fileName = post.url.split("/")[-1]
        urllib.request.urlretrieve(post.url, fileName)

        tweet(post.title, fileName)

        os.remove(fileName) #delete the file
    else:
        sys.stdout.write("Post found: None\n")
    sleep(20)