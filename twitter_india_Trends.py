
# coding: utf-8

# In[1]:

import tweepy
import pandas as pd
import string
import numpy as np
import matplotlib as plt
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


# In[2]:

consumer_key='TNV2Q9CJXsyQFIM0JK056SFYu'
consumer_secret='kN85WMtSewDoKi8FSCD0fa3iQ6i22PKUGD9ykT6aQOgHOmtXQN'
access_token='851355451270733824-LsNyqUOr0yiwSI2BqQ1ndGB5Ka3lRYi'
access_token_secret='hahXmRqh51m8uAsMtTEpLyLzzvE4RxBij6QGYXgR3xZe8'
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
trends1=api.trends_place(23424848)


# In[3]:

class StdOutListener(StreamListener):
    def on_data(self,data):
        print data
        return True
    def on_error(self,status):
        print status
        
        
if __name__=='__main__':
    
    le=StdOutListener()
    stream=Stream(auth,le)
    stream.filter(track=['datascience'])


# In[12]:

import json
import pandas as pd
import matplotlib.pyplot as plt


# In[13]:

tweets_data_path='C:\Users\Deepak Kumar\Desktop/twitterread.txt'
tweets=


# In[ ]:



