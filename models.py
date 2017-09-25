from peewee import *

import config


class Queue(Model):
	"""The model for our hook/filter queue table."""
	status = TextField()
	user = TextField()
	repo = TextField()
	email = TextField()

	@classmethod
	def create_quote(cls, user, repo, email):
		"""Adds a new quote to the database."""
		try:
			with config.DATABASE.transaction():
				cls.create(
					status='queued',
					user=user,
					repo=repo,
					email=email
				)
		except IntegrityError:
			pass

	class Meta:
		database = config.DATABASE

def initialize():
	"""Creates the tables if not already created"""
	config.DATABASE.connect()
	config.DATABASE.create_tables([Queue], safe=True)
	config.DATABASE.close()
