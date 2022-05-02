#!/usr/bin/python
import tweepy
import json
import time

def get_all_tweets(screen_name, poli_file):

    #twitter authorization
    CONSUMER_KEY = 'UKBuIR0J7ciQRXnFMKaIxKpX9'
    CONSUMER_SECRET = 'oGJwAzCUVVCAPmfJTgwkMrJPkqlqxsYIrpyacdiRlLfDVHPi9I'
    ACCESS_TOKEN = '1140988802-HoucbjQIBlLtlEz5YFkD5eYZI9KSFqFPEZZ3RhO'
    ACCESS_TOKEN_SECRET = 'jQAKiZbEcJhXaXQc0aUCz7Lywec5XRggLPFAfgRzi8lQ7'

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    #initialoze a list to hold all the tweepy Tweets
    alltweets = []

    #make initial request for most recent Tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name, count=200)

    #c=0
    #save most recent tweets
    alltweets.extend(new_tweets)
    #for tweet in new_tweets:
        #print(tweet.text)
        #c+=1
    #print(c)

    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    #keep grabing tweets until there are no tweets left to grab

    while len(new_tweets) > 0:
        #print("getting tweets before %s" %(oldest))

        #all subsequent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name, count = 200,max_id=oldest)
        time.sleep(6)
        #save most recent tweets
        alltweets.extend(new_tweets)

        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        #print("...%s tweets downloaded so far" %(len(alltweets)))


    
    #count= 0
    #for tweet in alltweets:
        #print(tweet.text + '\n')
        #count+=1
    #print(count)
        
    #transform the tweepy tweets into 2D array that will populate the csv
    #outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
    #for tweet in outtweets:
        #print(tweet)
    
    
    for tweet in alltweets:
        poli_file.write(tweet.text.encode("utf-8") + "*)^@")
        
        #count+=1

    #print(count)
    print("finished getting tweets from %s" %screen_name)
    poli_file.close()
    

if __name__ == '__main__':
    #read_f = open("screen_.txt", 'r')
    read_f = open("screen_name.txt", 'r')
    
    for name in read_f:
        t_handler = name.strip()
        print("getting tweets from %s" %(t_handler))
        write_f = open('%s_tweets.txt'%(t_handler), 'w')
        get_all_tweets(t_handler, write_f)
        
    #get_all_tweets("daveloebsack")
    read_f.close()
    
    

    
