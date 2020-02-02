# coding: utf-8

# In[1]:


import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob


# In[2]:


consumer_key = 'GIw0j8Nm3Qx9YYQCo5SLnqljh'
consumer_secret = 'HMLyZMmeGbhV9hnQkYeAFKJp0ynPsVWri3RT4FHTxNwQ2gad3g'
access_token = '2748454529-gTBtq6YTLRTRdMhUMiVISbFp3BPlP5pmfB9wRST'
access_token_secret = '1Fofwl74IXKOxFLkLHgKK42nLKg65OA3PMaEyKIlkkFDF'


# In[3]:


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# In[4]:


# want to find a way to ignore tweets that are affiliate links ie. robinhood links
def clean_tweet(self, tweet):
    '''
    Utility function to clean tweet text by removing links, special characters
    using simple regex statements.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


# In[10]:


def get_tweets(self, query, count):
    tweets = []
    try:
            # call twitter api to fetch tweets
        fetched_tweets = self.search(q = query, count = count)

            # parsing tweets one by one
        for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
            parsed_tweet = {}

                # saving ticker query of tweet
            parsed_tweet['query'] = query
                # saving text of tweet
            parsed_tweet['text'] = tweet.text
                # saving sentiment of tweet
            parsed_tweet['sentiment'] = get_tweet_sentiment(api, tweet.text)
                # saving time of tweet
            parsed_tweet['created_at'] = str(tweet.created_at)

                # appending parsed tweet to tweets list
            if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                if parsed_tweet not in tweets:
                    tweets.append(parsed_tweet)
            else:
                tweets.append(parsed_tweet)

            # return parsed tweets
        return tweets

    except tweepy.TweepError as e:
            # print error (if any)
        print("Error : " + str(e))


# In[12]:


def get_tweet_sentiment(self, tweet):
        # create TextBlob object of passed tweet text
    analysis = TextBlob(clean_tweet(api, tweet))
        # set sentiment
    return analysis.sentiment.polarity

def change_tweet_to_utf8(tweets):
	for tweet in tweets:
		tweet["text"] = tweet["text"].encode("utf-8")
		print(tweet)
	print()
# In[13]:

def twitter_handler(event, context):
    tweets = get_tweets(api, query = '$aapl', count = 100)
    change_tweet_to_utf8(tweets)
    tweets2 = get_tweets(api, query = '$googl', count = 100)
    change_tweet_to_utf8(tweets2)
    tweets3 = get_tweets(api, query = '$mmm', count = 100)
    change_tweet_to_utf8(tweets3)
    tweets4 = get_tweets(api, query = '$xom', count = 100)
    change_tweet_to_utf8(tweets4)
    tweets5 = get_tweets(api, query = '$csco', count = 100)
    change_tweet_to_utf8(tweets5)
    tweets6 = get_tweets(api, query = '$ge', count = 100)
    change_tweet_to_utf8(tweets6)
    tweets7 = get_tweets(api, query = '$hd', count = 100)
    change_tweet_to_utf8(tweets7)
    tweets8 = get_tweets(api, query = '$psx', count = 100)
    change_tweet_to_utf8(tweets8)
    tweets9 = get_tweets(api, query = '$mlpx', count = 100)
    change_tweet_to_utf8(tweets9)
    tweets10 = get_tweets(api, query = '$oxy', count = 100)
    change_tweet_to_utf8(tweets10)
    tweets11 = get_tweets(api, query = '$regi', count = 100)
    change_tweet_to_utf8(tweets11)
    tweets12 = get_tweets(api, query = '$mro', count = 100)
    change_tweet_to_utf8(tweets12)
    tweets13 = get_tweets(api, query = '$nrg', count = 100)
    change_tweet_to_utf8(tweets13)
    tweets14 = get_tweets(api, query = '$enbl', count = 100)
    change_tweet_to_utf8(tweets14)
    tweets15 = get_tweets(api, query = '$intc', count = 100)
    change_tweet_to_utf8(tweets15)

    return {
        'statusCode': 200,
        'body': "Successful"
    }

# picking positive tweets from tweets
#ptweets = [tweet for tweet in tweets if tweet['sentiment'] > 0]
# percentage of positive tweets
#print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))
# picking negative tweets from tweets
#ntweets = [tweet for tweet in tweets if tweet['sentiment'] < 0]
# percentage of negative tweets
#print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))
# percentage of neutral tweets
#print("Neutral tweets percentage: {} %  ".format(100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets)))
# get data in some form
