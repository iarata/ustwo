"""
Tasks
-------------------------

Configure worker tasks.
"""

from app.models import Clone
from celery import Celery
import config

# For sending mail.
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

celery = Celery()
celery.config_from_object(config)


@celery.task
def imprint(username):
    """
    Imprint a user's Twitter activity onto the clone.
    """
    c = Clone.objects.get(username=username)
    c.imprint()
    c.imprinting = False
    c.save()
    notify.delay('Imprinting complete', 'Imprinting complete for user {0}'.format(username))


@celery.task
def notify(subject, body):
    """
    Send an e-mail notification.
    """
    from_addr = config.MAIL_USER

    # Construct the message.
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the mail server.
    server = smtplib.SMTP(config.MAIL_HOST, config.MAIL_PORT)
    server.starttls()
    server.login(from_addr, config.MAIL_PASS)

    for target in config.MAIL_TARGETS:
        msg['To'] = target
        server.sendmail(from_addr, target, msg.as_string())

    server.quit()
