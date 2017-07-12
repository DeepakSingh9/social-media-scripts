
# coding: utf-8

# In[45]:

import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob


class MyTwitter(object): # main twitter class to start sentimental analytics.

    def __init__(self):
        consumer_key = 'apUoHzbOrC8n4waQpWQT6tf1C'
        consumer_secret = '1cA042bsAIv1t0MgGRhZp0945jpV38JbjL6omM9geYmYbEaHlv'
        access_token = '883181631866941440-E2qjMp3E1zeQR4BcOjLOw6r5ow4vbKZ'
        access_token_secret = 'PWDt3P6hMTNZLZRlfccbYEz4X8aFp0ac9QpxK2D1A6FgY'

    
        try:                                        # first get authenticated
            
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed!!! Check your keys")

    def cleaned_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])| (\w +:\ / \ / \S +)", " ", tweet).split())

    def sentiment(self, tweet):# we are using texblog here for sentiments
        analysis = TextBlob(self.cleaned_tweet(tweet))
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count=10):
        
        tweets = []

        try:
            
            fetched_tweets = self.api.search(q=query, count=count)

            
            for tweet in fetched_tweets:
                
                parsed_tweet = {}

                
                parsed_tweet['text'] = tweet.text # string
                # sentiment 
                parsed_tweet['sentiment'] = self.sentiment(tweet.text)

                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            
            return tweets          # final tweets

        except tweepy.TweepError as e:
            print("Error : " + str(e))       # errors


def main():
    # creating object of MyTwitter Class
    api = MyTwitter()
    
    tweets = api.get_tweets(query='donald trump', count=500)

    
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    
    print("Toatal Postive sentiments: {} percent".format(100 * len(ptweets) / len(tweets))) #postive tweets percentage
    
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] 
    
    print("Total Negetive Sentiments: {} percent".format(100 * len(ntweets) / len(tweets))) # negetive tweets percentage
    
    print("Total Nuetral sentiments: {} percent".format(100 * (len(tweets) - len(ntweets) - len(ptweets)) / len(tweets))) # neutral tweets percentage

    
    print("\n\nPositive tweets:")
    for tweet in ptweets[:10]:
        print(tweet['text'])                                  # printing postive tweets

    
    print("\n\nNegative tweets:")
    for tweet in ntweets[:10]: 
        print(tweet['text'])                                  # printing negetive tweets


if __name__ == "__main__":
    main()


# In[ ]:



