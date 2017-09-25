import re

hook_pattern = re.compile('\s*do_action\(\s*[\'\"]*([A-Za-z_-]+)[\'\"]*.*\);\s*')
filter_pattern = re.compile('.*apply_filters\(\s*[\'\"]*([A-Za-z_-]+)[\'\"]*.*\);\s*')
doc_pattern = re.compile('\s*//\s*(.+)')


def locate_hooks_filters(contents):
	"""Scans contents and returns hooks and filters"""
	hooks = dict()
	filters = dict()
	previous_line = ''

	# Cycle through each line of the file
	for line in contents:
		
		# Check for a hook on the line
		hook_match = hook_pattern.match(line)
		if hook_match:
			add_hook(hooks, hook_match[1], previous_line)
		
		# Check for a filter on the line
		filter_match = filter_pattern.match(line)
		if filter_match:
			add_filter(filters, filter_match[1], previous_line)

		# Save line as previous line for next cycle in loop
		previous_line = line
	return {'hooks': hooks, 'filters': filters}


def add_hook(hooks, hook, previous_line):
	"""Adds hook to list hooks if not already in list"""
	doc_match = doc_pattern.match(previous_line)
	if doc_match:
		hooks[hook] = doc_match[1]
	else:
		hooks[hook] = ''
	return hooks


def add_filter(filters, filter, previous_line):
	"""Adds filter to list filters if not already in list"""
	doc_match = doc_pattern.match(previous_line)
	if doc_match:
		filters[filter] = doc_match[1]
	else:
		filters[filter] = ''
	return filters