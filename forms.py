from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired


class AddRepoForm(Form):
	user = StringField(
		'GitHub Username',
		validators=[DataRequired()]
	)
	repo = StringField(
		'GitHub Repo',
		validators=[DataRequired()]
	)
	email = StringField(
		'Your Email',
		validators=[DataRequired()]
	)
