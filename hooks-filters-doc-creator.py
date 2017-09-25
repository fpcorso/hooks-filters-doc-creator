# App: Hooks Filters Doc Creator
# Author: Frank Corso
# Date created: 09/25/17
# Date last modified: 09/25/17
# Python Version: 3.6.1

import os
import sys

import locate
import github
import models


def clear_screen():
	os.system("cls" if os.name == 'nt' else 'clear')


def get_hooks_filters(user, repo):
	"""Gets all hooks and filters from files (path strings)"""
	return locate.locate_all_hooks_filters(user, repo)

if __name__ == '__main__':
	clear_screen()
	models.initialize()
	if len(sys.argv) > 0:
		hooks, filters = get_hooks_filters(sys.argv[1], sys.argv[2])
		print("Found {} hooks and {} filters".format(len(hooks), len(filters)))