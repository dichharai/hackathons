#!/usr/bin/python
import tweepy
import json
def get_screen_name(name):
    #twitter authorization
    CONSUMER_KEY = 'UKBuIR0J7ciQRXnFMKaIxKpX9'
    CONSUMER_SECRET = 'oGJwAzCUVVCAPmfJTgwkMrJPkqlqxsYIrpyacdiRlLfDVHPi9I'
    ACCESS_TOKEN = '1140988802-HoucbjQIBlLtlEz5YFkD5eYZI9KSFqFPEZZ3RhO'
    ACCESS_TOKEN_SECRET = 'jQAKiZbEcJhXaXQc0aUCz7Lywec5XRggLPFAfgRzi8lQ7'

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    #def process(user):
        #print(json.dumps(user))
    max_follower = 0
    screen_name = ""
    users = api.search_users(q=name)
    #process(users)
    
    for user in users:
        #print(user)
        num_follower = user.followers_count
        if num_follower > max_follower:
            screen_name = user.screen_name
            max_follower = num_follower

    #print(max_follower)
    #print(screen_name)
    return screen_name
            
    #public_tweets = api.home_timeline()
    #for tweet in public_tweets:
        #print(tweet.text)


if __name__ == '__main__':
    poli_list=[]
    read_f = open("top_politicians.txt", 'r')
    write_f = open("screen_name.txt", 'w')
    
    for raw_name in read_f:
        #print(line.strip())
        name = raw_name.strip()
        t_handler = get_screen_name(name)
        #print(t_handler)
        write_f.write(t_handler.encode("utf-8") + "\n")
        
        #poli_list.append(poli_name)

    #for name in poli_list:
        #get_screen_name(name)
    write_f.close()
    read_f.close()
