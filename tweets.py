import os
import numpy as np
import pandas as pd
import re
import pymongo
from textblob import TextBlob
import time
from dotenv import load_dotenv

load_dotenv()

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# myclient = pymongo.MongoClient("mongodb+srv://" + os.getenv('DBUSER') + ":" + os.getenv('DBPASS') + "@cluster0.3vutd3c.mongodb.net/test")
myclient = pymongo.MongoClient('mongodb://' + os.getenv('DBUSER') + ':' + os.getenv('DBPASS') + '@ac-o877xyo-shard-00-00.3vutd3c.mongodb.net:27017,ac-o877xyo-shard-00-01.3vutd3c.mongodb.net:27017,ac-o877xyo-shard-00-02.3vutd3c.mongodb.net:27017/?ssl=true&replicaSet=atlas-8u5z2a-shard-0&authSource=admin&retryWrites=true&w=majority')
mydb = myclient["socialdb"]
# mycol = mydb["kenya"]
mycol = mydb["TwitterDB"]

"""Fetch tweets from database"""


def get_tweets(a=7000):
    twets = pd.DataFrame(list(mycol.find())).drop(['_id', 'Tweet_id'], axis=1)
    twets = twets.drop_duplicates()
    twets['Accout Creation'] = pd.to_datetime(twets['Accout Creation']).dt.date
    twets['Tweet Date'] = pd.to_datetime(twets['Tweet Date']).dt.time
    twets.sort_values(by=['Tweet Date'], inplace=True)
    return twets.head(a)


"""Fetch top tweets. Most retweeted tweets."""


def getTopTweets(a=10):
    df_twets = get_tweets()[['Author', 'Tweet Date', 'Retweets', 'Tweet Text', 'Profile']]
    df_twets.sort_values(by=['Retweets'], inplace=True, ascending=False)
    df_twets = df_twets.drop_duplicates()
    return df_twets.head(a)


"""Fetch users with highest nnumber of followers."""


def getTopAccount(a=10):
    df_twets = get_tweets()[['Author', 'Accout Creation', 'Follower Count', 'Profile']]
    df_twets.sort_values(by=['Follower Count'], inplace=True, ascending=False)
    df_twets = df_twets.drop_duplicates()
    return df_twets.head(a)


def getDevice(a=6):
    df_location = get_tweets()[['Device']]
    df_grouped = df_location.groupby(["Device"]).agg(Total=pd.NamedAgg(column="Device", aggfunc="count")).reset_index(
        "Device")
    df_grouped.sort_values(by=['Total'], inplace=True, ascending=False)
    df_grouped = df_grouped.head(a)
    df_grouped['df_pct'] = (round(df_grouped.Total / df_grouped.Total.sum(),2))*100
    return df_grouped.head(a)


def getLocations(a=6):
    df_location = get_tweets()[['Location']]
    df_grouped = df_location.groupby(["Location"]).agg(
        Total=pd.NamedAgg(column="Location", aggfunc="count")).reset_index("Location")
    df_grouped.at[0, 'Location'] = 'No Location'
    df_grouped.sort_values(by=['Total'], inplace=True, ascending=False)
    df_grouped = df_grouped.iloc[1:].head(a)
    df_grouped['df_pct'] = (round(df_grouped.Total / df_grouped.Total.sum(),2))*100
    return df_grouped.head(a)


def clean_tweet():
    """
    Utility function to clean tweet text by removing links, special characters
    using simple regex statements.
    """
    df_tweet = get_tweets()[['Tweet Text']]
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", df_tweet).split())

def remove_pattern(input_txt, pattern):
    r = re.findall(pattern, input_txt)
    for i in r:
        input_txt = re.sub(i, '', input_txt)
    return input_txt

def clean_tweets(a=100000):
    df_tweet = get_tweets(a)
    """Remove twitter user handles"""
    df_tweet['df_Tweet'] = np.vectorize(remove_pattern)(df_tweet['Tweet Text'], "@[\w]*")
    """Remove Punctuations and special characters."""
    df_tweet['df_Tweet'] = df_tweet['df_Tweet'].str.replace("[^a-zA-Z#]", " ",regex=True)
    """Remove links."""
    df_tweet['df_Tweet'] = df_tweet['df_Tweet'].str.replace("[https://]", " ",regex=True)
    """Let us now remove all short words as they are usally connectors and have less meaning."""
    df_tweet['df_Tweet'] = df_tweet['df_Tweet'].apply(lambda x: ' '.join([w for w in x.split() if len(w)>3]))
    """Add total number of interactions a tweet has had"""
    df_tweet['Interactions'] = df_tweet[['Favorite Count', 'Retweets']].sum(axis=1)
    return df_tweet.head(a)

def getSummary(a = 'ttl'):
    df_total = clean_tweets(10000)
    df_interactions = clean_tweets(10000)['Interactions']
    if a == 'ttl':
        x= df_total.shape[0]
    else:
        x= df_interactions.sum()
    return x

def sentiment_calc(text):
    try:
        return TextBlob(text).sentiment.polarity
    except:
        return None

def get_tweet_sentiment(a=100000):
    df_twit = clean_tweets(a)
    df_twit['sentiment'] = round(df_twit['Tweet Text'].apply(sentiment_calc),1)
    return df_twit.head(a)

def getNegativeTweets(a=10):
    df_twets = get_tweet_sentiment()[['Author','Tweet Date','sentiment','Retweets','Tweet Text','Profile']]
    df_twets.sort_values(by=['sentiment'], inplace=True,ascending=True)
    return df_twets.head(a)