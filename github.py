import requests
import os


def get_paths(user, repo, file_type='.php'):
	"""Returns list of file paths from GitHub repo"""
	tree = requests.get(
		'https://api.github.com/repos/{}/{}/git/trees/master?recursive=1'.format(user, repo)
	).json()
	files = list()
	for file in tree['tree']:
		filename, ext = os.path.splitext(file['path'])
		if ext == file_type:
			files.append(file['path'])
	return files


def get_file_lines(user, repo, path):
	"""Returns a list of lines of file in GitHub repo"""
	file = requests.get(
		'https://raw.githubusercontent.com/{}/{}/master/{}'.format(user, repo, path)
	).text
	return file.split('\n')