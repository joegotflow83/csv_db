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

	def get_password(self, password):
		"""Return if the password is the password provided is in the db"""
		for hidden in self.cleaned_data:
			if hidden[1] == password:
				return True
		return False

	def check_credentials(self, username, password):
		"""When a user is logged in display the info"""
		if self.get_username(username) and self.get_password(password):
			return (True, username)
		else:
			return 'Invalid Credentials'

	def pull_user_info(self, username):
		"""Pull the user info to display to them"""
		for user in self.cleaned_data:
			if user[0] == username:
				return user
		return False

	def welcome(self, username):
		"""Display user info when "logged in" """
		user = self.pull_user_info(username)
		return "Welcome back {}!".format(user[0])
