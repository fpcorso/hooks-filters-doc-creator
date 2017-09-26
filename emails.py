import sendgrid
from sendgrid.helpers.mail import *

import config


def send_finished_email(to, user, repo, repo_id):
	"""Sends an email telling user that their repo has been analyzed."""
	subj = "Your repo's hooks and filters are ready!"
	body = "<h1>Your repo: {}/{} has been analyzed!</h1><a href='test/{}'>Click here to view results!</a><p>~Frank Corso</p><p>Twitter: <a href='https://twitter.com/fpcorso'>@fpcorso</a></p>".format(
		user, repo, repo_id
	)
	send_email(to, subj, body)


def send_email(to, subj, body):
	"""Sends an email to "to" with Subject of "subj" and contents of "body"."""
	sg = sendgrid.SendGridAPIClient(apikey=config.SENDGRID_API_KEY)
	from_email = Email("frank@frankcorso.me")
	to_email = Email(to)
	subject = subj
	content = Content("text/html", '<html>{}</html>'.format(body))
	mail = Mail(from_email, subject, to_email, content)
	response = sg.client.mail.send.post(request_body=mail.get())
	print(response.status_code)
	print(response.body)
	print(response.headers)