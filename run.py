# -*- coding: utf-8 -*-
import sys
import string
import random
import json
import twitter
import re
from textblob import TextBlob

ELIGIBLE_TAGS = [
    'CD',   # numbers
    'JJ',   # adjectives
    'NN',   # nouns
    'NNP',  # proper nouns
    'NNPS', # plural proper nouns
    'NNS',  # plural nouns
    'VBN',
    'VBG',
    'VB',
    'RB'    # adverbs
]

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
        user_tweets += twitter.tweets('brian_justie', page=i)
    with open('data/data.txt', 'w') as outfile:
        json.dump(user_tweets, outfile)

def process():
    f = open('data/data.txt', 'r')

    # Words matched with POS tags.
    speech_parts = {}

    # Chains of POS tags to build
    # tweets out of.
    speech_patterns = []
    for tweet in json.load(f):
        if '@' not in tweet['body']:    # Trying without any @ mentions.
            text = tweet['body']

            # Remove urls and @mentions.
            text = re.sub(r"(?:\@|https?\://)\S+", "", text)
            pattern = text

            for t in TextBlob(text).pos_tags:
                token = t[0]
                tag = t[1]

                # Preserve hashtags.
                if token[0] == '#':
                    continue

                if tag in ELIGIBLE_TAGS and len(token) > 2:
                    pattern = pattern.replace(token, '{{{{ {0} }}}}'.format(tag))

                    if tag == '-NONE-':
                        continue

                    if tag not in speech_parts:
                        speech_parts[tag] = []
                    speech_parts[tag].append(token.lower())

            speech_patterns.append(pattern)

    with open('data/speech_parts.json', 'w') as outfile:
        json.dump(speech_parts, outfile, indent=4, sort_keys=True)

    with open('data/speech_patterns.json', 'w') as outfile:
        json.dump(speech_patterns, outfile, indent=4, sort_keys=True )

def generate():
    with open('data/speech_parts.json', 'r') as f:
        speech_parts = json.load(f)
    with open('data/speech_patterns.json', 'r') as f:
        speech_patterns = json.load(f)

    pattern = random.choice(speech_patterns)
    tweet = pattern

    p = re.compile(r'\{\{\s*([A-Za-z]+)\s*\}\}')
    tags = p.findall(pattern)

    for tag in tags:
        token = random.choice(speech_parts[tag])
        tweet = re.sub(r'(\{\{\s*' + re.escape(tag) + r'\s*\}\})', token, tweet, 1)
    print(tweet)



if __name__ == '__main__':
    main()

