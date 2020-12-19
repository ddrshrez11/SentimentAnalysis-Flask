import os
import tweepy
import pandas as pd
import webbrowser
import time
import re

import config


auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_uri)
api = tweepy.API(auth,wait_on_rate_limit=True)
auth.set_access_token(access_token, access_token_secret)

# redirect_url = auth.get_authorization_url()
# print(redirect_url)
# user_pint_input = input("What's the pin value? ")
# print(auth.get_access_token(user_pint_input))
tweet_data={}

def tweepy_run(url):
    try:    
        pattern='(https\:\//[a-z]+\.com)\/([a-zA-Z0-9]+)/(status*)/([0-9]+)'
        r = re.match(pattern,url)
        name =r.group(2)
        tweet_id=r.group(4)
        print (name,tweet_id)

        user = api.get_user(name)
        tweet_data["userid"] = user.id_str
        tweet_data["user_name"]=user.name
        tweet_data["screen_name"] = user.screen_name
        tweet_data["followers"] = str(user.followers_count)
        tweet_data["verified"]= user.verified
        
        # tweet
        tweet_data["tweet_id"]=tweet_id
        status = api.get_status((tweet_id), tweet_mode = "extended")
        tweet_data["tweet"]= status.full_text
        tweet_data["retweet_count"] = status.retweet_count 
        tweet_data["favorite_count"] = status.favorite_count 
        tweet_data["created_at"] = status.created_at
        

        #image
        str1 = user.profile_image_url_https
        lst_str=list(str1)
        del lst_str[-11:-4]
        user_img=''.join(lst_str)
        tweet_data["user_img"]=user_img

        #replies
        replies=[]
        for tweet in tweepy.Cursor(api.search,q='to:'+name, result_type='recent', timeout=999999).items(500):
            if hasattr(tweet, 'in_reply_to_status_id_str'):
                if (tweet.in_reply_to_status_id_str==tweet_id):
                    replies.append(tweet)
        
        tweet_list=[]
        for tweet in replies:
            tweet_list.append(tweet.text)
        
        tweet_data["replies_num"] = len(tweet_list)
        tweet_data["replies"]= tweet_list

        return tweet_data
    
    except Exception as err:
        print(err.message)
        for i in err.message:
            print(i)
    # except AttributeError:
    #     return 'There is an error in url'
#print(tweepy_run('https://twitter.com/bubblesenergy/status/1340181990478254081'))