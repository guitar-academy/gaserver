from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class ComposeForm(Form):
    title = StringField('title', validators=[DataRequired()])
    description = StringField('description', validators=[])
    notation = StringField('notation', validators=[])

