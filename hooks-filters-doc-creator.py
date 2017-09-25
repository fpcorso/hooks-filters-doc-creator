# App: Hooks Filters Doc Creator
# Author: Frank Corso
# Date created: 09/25/17
# Date last modified: 09/25/17
# Python Version: 3.6.1

import os
import sys

import locate
import github


def clear_screen():
	os.system("cls" if os.name == 'nt' else 'clear')


def get_hooks_filters(user, repo, files):
	"""Gets all hooks and filters from files (path strings)"""
	hooks = dict()
	filters = dict()
	for file in files:
		print("Opening file: {}...".format(file))
		file_contents = github.get_file_lines(user, repo, file)
		hooks_filters = locate.locate_hooks_filters(file_contents)
		hooks.update(hooks_filters['hooks'])
		filters.update(hooks_filters['filters'])			
	return hooks, filters

if __name__ == '__main__':
	clear_screen()
	if (len(sys.argv) > 1):
		project_files = github.get_paths(sys.argv[1], sys.argv[2])
		hooks, filters = get_hooks_filters(sys.argv[1], sys.argv[2], project_files)
		print("We found {} hooks and {} filters!".format(len(hooks), len(filters)))
		for hook, desc in hooks.items():
			print("{}: {}".format(hook, desc))
		for filter, desc in filters.items():
			print("{}: {}".format(filter, desc))