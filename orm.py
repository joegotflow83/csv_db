class ORM:


	def __init__(self, file_contents=[]):
		"""Initiazlie variables"""
		self.file_contents = self.read_file(self)
		self.cleaned_data = self.clean_file(self, self.file_contents)

	@staticmethod
	def clean_file(self, file_contents):
		"""Read the file contents in a formatted manner"""
		return [line.strip().split(',') for line in file_contents]

	@staticmethod
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

	def delete_user_info(self, username):
		"""Delete a users info"""
		user = self.pull_user_info(username)
		for line in self.cleaned_data:
			if line == user:
				line = self.cleaned_data.remove(line)
				return True	

	def welcome(self, username):
		"""Display user info when "logged in" """
		user = self.pull_user_info(username)
		return "Welcome back {}!".format(user[0])
		
	def actions(self, action):
		"""Allow the user to take an action on his account"""
		if action == 1:
			return 1
		elif action == 2:
			return 2
		elif action == 3:
			return 3
		elif action == 4:
			return 4

	def add_user(self, username, password, full_name, email):
		"""Add a user to the db"""
		with open('database.txt', 'a') as f:
			new_user = [username, password, full_name, email]
			if self.get_username(new_user[0]):
				return 'That username already exists! Use a different username'
			else:
				f.write('\n' + ' '.join(new_user))
		return new_user

	def change_password(self, username, new_password):
		"""Allow a user to change their password"""
		user = self.pull_user_info(username)
		update_user = self.pull_user_info(username)
		update_user[1] = new_password
		with open('database.txt', 'a') as f:
			f.write('\n' + ' '.join(update_user))
		with open('database.txt', 'r') as f:
			data = f.readlines()
		with open('database.txt', 'w') as f:
			for line in data:
				if line != user:
					f.write(line)
		user = self.delete_user_info(username)
		return update_user

	def change_email(self, username, new_email):
		"""Allow a user to change their email"""
		user = self.pull_user_info(username)
		update_user = self.pull_user_info(username)
		update_user[3] = new_email
		with open('database.txt', 'a') as f:
			f.write('\n' + ' '.join(update_user))
		with open('database.txt', 'r') as f:
			data = f.readlines()
		with open('database.txt', 'w') as f:
			for line in data:
				if line != user:
					f.write(line)
		user = self.delete_user_info(username)
		return update_user

	def logout(self, username, password):
		"""Allow a user to log out"""
		username = None
		password = None
		return (False, username, password)
