from flask import Flask, render_template, redirect, url_for, flash

import models
import forms
import config


app = Flask(__name__)
app.secret_key = config.SECRET_KEY


@app.route('/', methods=('GET', 'POST'))
def main_page():
	"""Single route in the Flask app. Shows a form that can be used to add repo to queue"""
	form = forms.AddRepoForm()
	if form.validate_on_submit():
		flash("New repo added!")
		models.Queue.create_queue_entry(form.user.data, form.repo.data, form.email.data)
	return render_template('index.html', form=form)


if __name__ == '__main__':
	models.initialize()
	app.run(debug=config.DEBUG, host=config.HOST, port=config.PORT)
