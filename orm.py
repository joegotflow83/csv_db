class ORM:


	def __init__(self, file_contents=[]):
		"""Initiazlie variables"""
		self.cleaned_data = file_contents

	@staticmethod
	def clean_file(self, file_contents):
		"""Read the file contents in a formatted manner"""
		return [line.split(',') for line in file_contents]

	def read_file(self):
		"""Open the database and read the contents"""
		with open("database.txt") as f:
			content = f.readlines()
		return content

	def get_username(self, username):
		"""Return if the username if the username provided is in the db"""
		for name in self.cleaned_data:
			if name[0] == username:
				return True
		return False