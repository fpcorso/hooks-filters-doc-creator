# App: Hooks Filters Doc Creator
# Author: Frank Corso
# Date created: 09/25/17
# Date last modified: 09/25/17
# Python Version: 3.6.1

import os

import locate


def clear_screen():
	os.system("cls" if os.name == 'nt' else 'clear')


def get_hooks_filters(files):
	"""Gets all hooks and filters from files (path strings)"""
	hooks = dict()
	filters = dict()
	for file in files:
		with open(file) as f:
			hooks_filters = locate.locate_hooks_filters(f.readlines())
			hooks.update(hooks_filters['hooks'])
			filters.update(hooks_filters['filters'])
	return hooks, filters

if __name__ == '__main__':
	clear_screen()
	files = ['class-qmn-quiz-manager.php', 'class-qmn-quiz-creator.php']
	hooks, filters = get_hooks_filters(files)
	print("We found {} hooks and {} filters!".format(len(hooks), len(filters)))