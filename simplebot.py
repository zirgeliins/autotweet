import requests
from bs4 import BeautifulSoup
import random
import time
import tweepy
from set_variables import *


#Pull data from tumblr
def loadquotes(link, pages):
    postarray=[]
    for j in range(pages):
        res = requests.get(link + '/page/'+str(j)) #getting requests from tumblr page 
        textfile = res.text
        i=0
        string=''
        while i<len(textfile):
            string=string+textfile[i]
            if '<p>' in string:
                string=''
            if '</p>' in string:
                soup = BeautifulSoup(string, 'html.parser')
                postarray.append(soup.get_text())
                string=''
            i+=1
    return postarray

#clean data from tumblr - you may need to customize this depending on how messy the format is
def cleanup(postarray):
    twitterarr=[]
    for i in range(len(postarray)):
        """ HERE I HANDLE THE EXCEPTIONS
        if  i<1136 and i>1095:
            continue
        """
        postarray[i] = postarray[i].replace("\n", "") #replacing the strings that weren't cleaned up with BeautifulSoup
        postarray[i] = postarray[i].replace("\xa0", "") #replacing the strings that weren't cleaned up with BeautifulSoup
        if len(postarray[i])<141:
            twitterarr.append(postarray[i])
    return twitterarr


#integration with twitter
def integrate(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    return api

#tweet action
def tweet(iterable, api):
    tweet_choice=random.choice(iterable)
    api.update_status(tweet_choice)
    print("Wooooo the following tweet was just sent: "+tweet_choice) 
    iterable.remove(tweet_choice)
    

    
#Main function (uncomment if you want this to run automatically)
"""
def __main__:
    api=integrate(set_variables.CONSUMER_KEY, set_variables.CONSUMER_SECRET, set_variables.ACCESS_KEY, set_variables.ACCESS_SECRET):
    iterable=cleanup(loadquotes(set_variables.link, set_variables.pages))
    while len(iterable)>0:
        tweet(iterable, api)
        time.sleep(random.randrange(set_variables.min_delay, set_variables.max_delay))
        if len(iterable[n]==1:
               iterable=cleanup(loadquotes(set_variables.link, set_variables.pages))
               
"""
