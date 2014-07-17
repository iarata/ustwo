from flask_wtf import Form
from wtforms import TextField
from wtforms.validators import Required

class CloneForm(Form):
    username = TextField('Twitter Username', validators=[Required()])
