import itertools
import math

import tweepy
from tweepy import TweepError

import config

def _api():
    """
    Load auth info from config.
    Setup things on Twitter's end at:
    https://apps.twitter.com/
    """
    auth = tweepy.OAuthHandler(config.TWITTER_CONSUMER_KEY, config.TWITTER_CONSUMER_SECRET)
    auth.set_access_token(config.TWITTER_ACCESS_TOKEN, config.TWITTER_ACCESS_SECRET)

    # Return API object.
    return tweepy.API(auth)

api = _api()

MAX_COUNT = 200
def tweets(username, count=200):
    """
    Returns tweets for a user.
    """
    pages = math.ceil(count/MAX_COUNT) - 1
    count = min(MAX_COUNT, count)

    # This produces a list of lists.
    tweets_ = [api.user_timeline(screen_name=username, count=count, page=i) for i in range(pages)]

    # This flattens the list of lists.
    tweets = list(itertools.chain.from_iterable(tweets_))

    return [{
                'body': tweet.text,
                'tid': tweet.id,
                'protected': tweet.user.protected,
                'retweeted': tweet.retweeted
            } for tweet in tweets]

def user_exists(username):
    try:
        api.get_user(username)
    except TweepError as e:
        if e.response.status == 404:
            return False
        else:
            raise e
    return True

def retweet(id):
    """
    Retweet a tweet by id.
    """
    try:
        api.retweet(id)
    except TweepError as e:
        # Assume we may have violated some rate limit
        # and forget about it
        if e.response.status == 403:
            print('403 error when trying to retweet. Possibly hit a rate limit.')
        else:
            raise e


def tweet(text):
    """
    Tweet something from your account.
    """
    try:
        api.update_status(text)
    except TweepError as err:
        # Assume we may have violated some rate limit
        # and forget about it
        if '403' in err:
            logger.info('403 error when trying to tweet. Possibly hit a rate limit.')
        else:
            raise err