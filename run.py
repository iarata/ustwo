# -*- coding: utf-8 -*-
import sys
import string
import random
import json
import twitter
import re
from textblob import TextBlob

def main():
    try:
        import config
    except ImportError:
        print('No config found. Have you renamed `config-sample.py` to `config.py` and filled in your info?')
        return

    if len(sys.argv) < 2:
        print('Please tell me what example to run!')
        return

    try:
        globals()[sys.argv[1]]();
    except KeyError:
        print('Doesn\'t seem to be an example by that name.')
        return

def tweets():
    user_tweets = []
    for i in range(10):
        user_tweets += twitter.tweets('frnsys', page=i)
    with open('data/data.txt', 'w') as outfile:
        json.dump(user_tweets, outfile)

def process():
    f = open('data/data.txt', 'r')

    # Words matched with POS tags.
    speech_parts = {}

    # Chains of POS tags to build
    # tweets out of.
    speech_patterns = {}
    for tweet in json.load(f):
        pattern_ = []

        if '@' not in tweet['body']:    # Trying without any @ mentions.
            text = tweet['body']

            # Remove urls
            text = re.sub(r"(?:\@|https?\://)\S+", "", text)

            for t in TextBlob(text).pos_tags:
                token = t[0]
                tag = t[1]

                pattern_.append(tag)

                if tag == '-NONE-':
                    continue

                if tag not in speech_parts:
                    speech_parts[tag] = []
                speech_parts[tag].append(token)

            pattern = '.'.join(pattern_)
            if pattern not in speech_patterns:
                speech_patterns[pattern] = 0
            speech_patterns[pattern] += 1

    with open('data/speech_parts.json', 'w') as outfile:
        json.dump(speech_parts, outfile)

    with open('data/speech_patterns.json', 'w') as outfile:
        json.dump(speech_patterns, outfile)

def generate():
    with open('data/speech_parts.json', 'r') as f:
        speech_parts = json.load(f)
    with open('data/speech_patterns.json', 'r') as f:
        speech_patterns = json.load(f)

    pattern = _weighted_choice(speech_patterns)

    tweet = []
    for tag in pattern.split('.'):
        token = random.choice(speech_parts[tag])
        tweet.append(token)
    print(' '.join(tweet))


def _weighted_choice(choices):
    """
    Random selects a key from a dictionary,
    where each key's value is its probability weight.
    """
    # Randomly select a value between 0 and
    # the sum of all the weights.
    rand = random.uniform(0, sum(choices.values()))

    # Seek through the dict until a key is found
    # resulting in the random value.
    summ = 0.0
    for key, value in choices.items():
        summ += value
        if rand < summ: return key

    # If this returns False,
    # it's likely because the knowledge is empty.
    return False


if __name__ == '__main__':
    main()

