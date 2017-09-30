import re

import github

hook_pattern = re.compile('\s*do_action\(\s*[\'\"]*([A-Za-z_-]+)[\'\"]*.*\);\s*')
filter_pattern = re.compile('.*apply_filters\(\s*[\'\"]*([A-Za-z_-]+)[\'\"]*.*\);\s*')
doc_pattern = re.compile('\s*//\s*(.+)')


def locate_all_hooks_filters(user, repo):
	"""Returns all hooks and filters in repo"""
	hooks = dict()
	filters = dict()
	repo_files = github.get_paths(user, repo)
	for file in repo_files:
		print("Opening file: {}...".format(file))
		file_contents = github.get_file_lines(user, repo, file)
		hooks_filters = search_file_for_hooks_filters(file_contents, file)
		hooks.update(hooks_filters['hooks'])
		filters.update(hooks_filters['filters'])
	return hooks, filters


def search_file_for_hooks_filters(contents, filename):
	"""Scans contents and returns hooks and filters"""
	hooks = dict()
	filters = dict()
	previous_line = ''
	line_number = 0

	# Cycle through each line of the file
	for line in contents:

		# Increases line number
		line_number += 1
		
		# Check for a hook on the line
		hook_match = hook_pattern.match(line)
		if hook_match:
			add_hook_filter(line_number, filename, hooks, hook_match.group(1), previous_line)
		
		# Check for a filter on the line
		filter_match = filter_pattern.match(line)
		if filter_match:
			add_hook_filter(line_number, filename, filters, filter_match.group(1), previous_line)

		# Save line as previous line for next cycle in loop
		previous_line = line
	return {'hooks': hooks, 'filters': filters}


def add_hook_filter(line_number, filename, list_of_items, new_item, previous_line):
	"""Adds hook/filter to list of hooks/filters if not already in list"""
	doc = prepare_documentation(previous_line)
	if new_item in list_of_items:
		list_of_items[new_item]['loc'].append({
			'file': filename,
			'line': line_number
		})
		if len(list_of_items[new_item]['doc']) = 0 and len(doc) > 0:
			list_of_items[new_item]['doc'] = doc
	else:
		list_of_items[new_item] = {
			'doc': doc,
			'loc': [
				{
					'file': filename,
					'line': line_number
				}
			]
		}
	return list_of_items


def prepare_documentation(previous_line):
	"""Prepares the documentation for the hook/filter"""
	doc_match = doc_pattern.match(previous_line)
	if doc_match:
		return doc_match.group(1)
	return ''