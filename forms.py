from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class AddRepoForm(Form):
	user = StringField(
		'user',
		validators=[DataRequired()]
	)
	repo = StringField(
		'repo',
		validators=[DataRequired()]
	)
	email = StringField(
		'email',
		validators=[DataRequired()]
	)
