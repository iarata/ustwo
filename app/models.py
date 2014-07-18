import datetime
import random
import re
import config

from textblob import TextBlob
from app import db, twitter

class Clone(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    username = db.StringField(required=True, unique=True)
    imprinting = db.BooleanField(default=False)

    # Mad-lib Tweet patterns.
    patterns = db.ListField(db.StringField(), default=[])

    # { POS tag: words }
    vocabulary = db.DictField(default={})

    meta = {
            'allow_inheritance': True,
            'indexes': ['-created_at', 'username'],
            'ordering': ['-created_at']
    }

    def imprint(self):
        """
        Generate a clone for a given Twitter user
        by analyzing their Twitter history.
        """
        user_tweets = twitter.tweets(self.username, count=2000)

        for tweet in user_tweets:
            text = tweet['body']
            if '@' not in text: # Trying without any @mentions.

                # Remove urls and @mentions
                text = re.sub(r'(?:\@|https?\://)\S+', '', text)
                pattern = text

                # Extract parts of speech.
                for t in TextBlob(text).pos_tags:
                    token = t[0]
                    tag = t[1]

                    # Preserve hashtags.
                    # Skip untagged tokens.
                    # Skip tokens which are too short.
                    if token[0] == '#' or tag == '-NONE-' or len(token) <= 2:
                        continue

                    if tag in config.ELIGIBLE_TAGS:
                        # Build the pattern.
                        pattern = pattern.replace(token, '{{{{ {0} }}}}'.format(tag))

                        # Add new tokens to the vocabulary.
                        if tag not in self.vocabulary:
                            self.vocabulary[tag] = []
                        self.vocabulary[tag].append(token.lower())

                self.patterns.append(pattern)

    def speak(self):
        pattern = random.choice(self.patterns)
        tweet = pattern

        # Extract the tags to be replaced.
        p = re.compile(r'\{\{\s*([A-Za-z]+)\s*\}\}')
        tags = p.findall(pattern)

        # Replace the tags with selections from the vocabulary.
        for tag in tags:
            token = random.choice(self.vocabulary[tag])
            tweet = re.sub(r'(\{\{\s*' + re.escape(tag) + r'\s*\}\})', token, tweet, 1)
        return tweet
