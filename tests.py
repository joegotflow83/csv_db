import unittest

from orm import ORM


class ViewsTest(unittest.TestCase):


	def setUp(self):
		"""Set up testing env"""
		self.file_input = [['joegotflow83', 'admin', 'joseph moran', 'joe@absolutod.com'],
			['yoshi', 'dinosaur', 'yoshi the dinosaur', 'yoshi@eggs.com']]
		self.orm = ORM(file_contents=self.file_input)

	def tearDown(self):
		"""Tear down the testing env"""
		self.file_input = None
		self.orm = None

	def test_db_file_is_formatted_correctly(self):
		"""Test that the db file is correctly formatted for searching"""
		sample_data = ['joegotflow83,admin,joseph moran,joe@absolutod.com',
			'yoshi,dinosaur,yoshi the dinosaur,yoshi@eggs.com']
		self.assertEquals(ORM.clean_file(self, sample_data), self.file_input)

	def test_db_can_find_username(self):
		"""Test that the db can find a username based on an input"""
		self.orm = ORM(self.file_input)
		self.assertTrue(self.orm.get_username('joegotflow83') == True)

	def test_db_returns_false_if_no_username_in_db(self):
		"""Test that the db returns False if no username in db"""
		self.orm = ORM(self.file_input)
		self.assertTrue(self.orm.get_username('myusername') == False)

	def test_db_can_find_password(self):
		"""Test that the db can find a password based on an input"""
		self.orm = ORM(self.file_input)
		self.assertTrue(self.orm.get_password('admin') == True)

	def test_db_returns_false_if_no_password_in_db(self):
		"""Test that the db returns False if no password in db"""
		self.orm = ORM(self.file_input)
		self.assertFalse(self.orm.get_password('badpassword'))

	def test_user_can_log_on(self):
		"""Test that when a user provides the correct credentials return True"""
		self.orm = ORM(self.file_input)
		self.assertTrue(self.orm.check_credentials('joegotflow83', 'admin'))

	def test_error_occurs_if_invalid_credentials(self):
		"""Test that an exception is thrown if the credentials are invalid"""
		self.orm = ORM(self.file_input)
		self.assertIn(self.orm.check_credentials('username', 'password'), 'Invalid Credentials')

	def test_db_can_pull_all_of_users_info_when_logged_in(self):
		"""Test that the users info is pulled once "logged in" """
		self.orm = ORM(self.file_input)
		self.assertEquals(self.orm.pull_user_info('joegotflow83'), 
			['joegotflow83', 'admin', 'joseph moran', 'joe@absolutod.com'])

	def test_db_does_not_pull_user_if_username_not_in_db_for_pull_func(self):
		"""Test that if no username is in the db return False"""
		self.orm = ORM(self.file_input)
		self.assertFalse(self.orm.pull_user_info('mike'))

	def test_user_info_gets_deleted(self):
		"""Test that the user info gets deleted"""
		self.orm = ORM(self.file_input)
		self.assertEquals(self.orm.delete_user_info('joegotflow83'), True)

	def test_user_gets_welcome_message_when_logged_on(self):
		"""Test that a welcome message is displayed when the user is "logged in" """
		self.orm = ORM(self.file_input)
		username = self.file_input[0][0]
		self.assertIn(self.orm.welcome('joegotflow83'), 'Welcome back {}!'.format(username))

	def test_user_can_pick_an_action(self):
		"""Test a user can perform an action when "logged in" """
		self.orm = ORM(self.file_input)
		self.assertEquals(self.orm.actions(4), 4)

	def test_user_can_create_new_user(self):
		"""Test a user can create a new user and save it to the db"""
		self.orm = ORM(self.file_input)
		username = 'joe'
		password = 'python'
		full_name = 'guiseppe moran'
		email = 'joe@daretheventure.com'
		new_user = ['joe', 'python', 'guiseppe moran', 'joe@daretheventure.com']
		self.assertEquals(self.orm.add_user(username, password, full_name, email),
			 new_user)

	def test_if_username_already_exists_throw_an_error(self):
		"""Test if a user creates a new username and it already exists
		have them create new username"""
		self.orm = ORM(self.file_input)
		username = 'joegotflow83'
		password = 'dummyadmin'
		full_name = 'joseph moran'
		email = 'ballion3@gmail.com'
		self.assertIn(self.orm.add_user(username, password, full_name, email), 
					'That username already exists! Use a different username')

	def test_user_can_change_current_password(self):
		"""Test that a user can change their password"""
		self.orm = ORM(self.file_input)
		new_password = 'newadmin'
		update_user = ['joegotflow83', 'newadmin', 'joseph moran', 'joe@absolutod.com']
		self.assertEquals(self.orm.change_password('joegotflow83', 
												new_password), update_user)

	def test_user_can_change_email(self):
		"""Test user can change their email"""
		self.orm = ORM(self.file_input)
		new_email = 'goat@obeythetestinggoat.com'
		update_user = ['joegotflow83', 'admin', 'joseph moran', 'goat@obeythetestinggoat.com']
		self.assertEquals(self.orm.change_email('joegotflow83',
												new_email), update_user)

	def test_user_can_logout(self):
		"""Test user can logout"""
		self.orm = ORM(self.file_input)
		self.assertEquals(self.orm.logout('joegotflow83', 'admin'), 
										(False, None, None))
