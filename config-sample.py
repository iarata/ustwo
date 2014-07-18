CSRF_ENABLED = True
SECRET_KEY = 'some-passphrase'
MONGODB_SETTINGS = {
    'DB': 'youtwo',
    'HOST': 'localhost'

    # If necessary:
    #'USERNAME': 'username',
    #'PASSWORD': 'pw'
}

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

# Celery config.
# Broker (message queue) url.
BROKER_URL = 'amqp://guest@localhost:5672//'

# Try connecting ad infinitum.
BROKER_CONNECTION_MAX_RETRIES = None

# Result backend.
CELERY_RESULT_BACKEND = 'mongodb'
CELERY_MONGODB_BACKEND_SETTINGS = {
    'host': 'localhost',
    'port': 27017,
    'database': 'celery',
    'taskmeta_collection': 'my_taskmeta' # Collection name to use for task output
}

# What modules to import on start.
# Note that in production environments you will want to
# remove the 'tests' tasks module.
CELERY_IMPORTS = ('app.tasks',)

# Send emails on errors
CELERY_SEND_TASK_ERROR_EMAILS = True
ADMINS = [
    ('Francis Tseng', 'ftzeng@gmail.com')
]

SERVER_EMAIL = 'clone.bot@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'clone.bot@gmail.com'
EMAIL_HOST_PASSWORD = 'your-pass'
EMAIL_USE_TLS = True

# Setting a maximum amount of tasks per worker
# so the worker processes get regularly killed
# (to reclaim memory). Not sure if this is the best
# approach, but see:
# https://github.com/publicscience/argos/issues/112
CELERYD_MAX_TASKS_PER_CHILD=100
