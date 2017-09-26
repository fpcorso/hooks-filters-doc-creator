from peewee import *

import config


class Queue(Model):
	"""The model for our hook/filter queue table."""
	status = TextField()
	user = TextField()
	repo = TextField()
	email = TextField()
	hooks = TextField()
	filters = TextField()

	@classmethod
	def create_queue_entry(cls, user, repo, email):
		"""Adds a new repo to the queue."""
		try:
			with config.DATABASE.transaction():
				cls.create(
					status='queued',
					user=user,
					repo=repo,
					email=email,
					hooks='',
					filters=''
				)
		except IntegrityError:
			pass

	@staticmethod
	def get_next_repo():
		"""Returns the next repo in queue"""
		try:
			return Queue.select().where(Queue.status == 'queued').get()
		except DoesNotExist:
			return None

	class Meta:
		database = config.DATABASE

def initialize():
	"""Creates the tables if not already created"""
	config.DATABASE.connect()
	config.DATABASE.create_tables([Queue], safe=True)
	config.DATABASE.close()
