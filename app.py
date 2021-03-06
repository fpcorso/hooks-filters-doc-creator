from flask import Flask, render_template, redirect, url_for, flash
import json

import models
import forms
import config


app = Flask(__name__)
app.secret_key = config.SECRET_KEY


@app.route('/', methods=('GET', 'POST'))
def main_page():
	"""Main page. Shows a form that can be used to add repo to queue"""
	form = forms.AddRepoForm()
	if form.validate_on_submit():
		flash("New repo added!")
		models.Queue.create_queue_entry(form.user.data, form.repo.data, form.email.data)
		return redirect(url_for('submitted'), code=302)
	return render_template('index.html', form=form)


@app.route('/submitted', methods=('GET', 'POST'))
def submitted():
	"""Thank you page shown after repo is submitted."""
	return render_template('submitted.html')


@app.route('/<id>', methods=('GET', 'POST'))
def repo_page(id):
	"""Page for a repo. Shows hooks and filters of the repo."""
	hooks = dict()
	filters = dict()
	try:
		repo = models.Queue.select().where(models.Queue.id == id).get()
		if repo.hooks:
			hooks = json.loads(repo.hooks)
			filters = json.loads(repo.filters)
		return render_template('repo.html', repo=repo.repo, user=repo.user, hooks=hooks, filters=filters)
	except models.DoesNotExist:
		return redirect(url_for('main_page'), code=302)


if __name__ == '__main__':
	models.initialize()
	app.run(debug=config.DEBUG, host=config.HOST, port=config.PORT)
