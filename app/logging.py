"""
Logging
-------------------------

Sets up a mail handler for logging errors.
"""

from app import app

cfg = app.config

# Email error messages.
if not app.debug:
    import logging
    from logging.handlers import SMTPHandler
    mail_handler = SMTPHandler(
            (cfg['MAIL_HOST'], cfg['MAIL_PORT']),
            cfg['MAIL_USER'],
            cfg['MAIL_TARGETS'],
            'CLONES IN TROUBLE',
            (cfg['MAIL_USER'], cfg['MAIL_PASS']),
            secure=())
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)

