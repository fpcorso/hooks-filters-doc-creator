# App: Hooks Filters Doc Creator
# Author: Frank Corso
# Date created: 09/25/17
# Date last modified: 09/25/17
# Python Version: 3.6.1

import os
import sys
from glob import glob

import locate


def clear_screen():
	os.system("cls" if os.name == 'nt' else 'clear')


def get_hooks_filters(files):
	"""Gets all hooks and filters from files (path strings)"""
	hooks = dict()
	filters = dict()
	for file in files:
		print("Opening file: {}...".format(file))
		with open(file) as f:
			hooks_filters = locate.locate_hooks_filters(f.readlines())
			hooks.update(hooks_filters['hooks'])
			filters.update(hooks_filters['filters'])
	return hooks, filters

if __name__ == '__main__':
	clear_screen()
	if (len(sys.argv) > 1):
		project_files = [y for x in os.walk(sys.argv[1]) for y in glob(os.path.join(x[0], '*.php'))]
		print("Found {} files...".format(len(project_files)))
		hooks, filters = get_hooks_filters(project_files)
		print("We found {} hooks and {} filters!".format(len(hooks), len(filters)))
		for hook, desc in hooks.items():
			print("{}: {}".format(hook, desc))
		for filter, desc in filters.items():
			print("{}: {}".format(filter, desc))