# App: Hooks Filters Doc Creator
# Author: Frank Corso
# Date created: 09/25/17
# Date last modified: 09/25/17
# Python Version: 3.6.1

import os
import sys
import json
from time import sleep

import locate
import github
import models
import emails


def clear_screen():
	os.system("cls" if os.name == 'nt' else 'clear')


def main_loop():
	"""Monitiors queue and loads data for next repo in queue"""
	while True:
		repo = models.Queue.get_next_repo()
		if repo:
			print('*** Found repo: {} ***'.format(repo.repo))
			hooks, filters = locate.locate_all_hooks_filters(repo.user, repo.repo)
			repo.hooks = json.dumps(hooks)
			repo.filters = json.dumps(filters)
			repo.status = 'finished'
			print('*** Saving... ***')
			repo.save()
			print('*** Sending email... ***')
			emails.send_finished_email(repo.email, repo.user, repo.repo, repo.id)
		sleep(300) # sleep for a few minutes to not go over GitHub rate limit  			


if __name__ == '__main__':
	clear_screen()
	print('*** Checking database... ***')
	models.initialize()
	print('*** Starting loop... ***')
	main_loop()