CSRF_ENABLED = True
SECRET_KEY = 'some-passphrase'
MONGODB_SETTINGS = {'DB': 'youtwo'}

MAIL_HOST = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USER = 'some@email.com'
MAIL_PASS = 'somepass'
MAIL_TARGETS = ['someadmin@email.com']

# You can get these by creating a new app at
# https://apps.twitter.com/
TWITTER_CONSUMER_KEY = 'fill_me_in'
TWITTER_CONSUMER_SECRET = 'fill_me_in'
TWITTER_ACCESS_TOKEN = 'fill_me_in'
TWITTER_ACCESS_SECRET = 'fill_me_in'

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
