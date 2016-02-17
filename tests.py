import unittest

from orm import ORM


class ViewsTest(unittest.TestCase):


	def setUp(self):
		"""Set up testing env"""
		self.file_input = [['joegotflow83', 'admin', 'joseph moran', 'joe@absolutod.com'],
			['yoshi', 'dinosaur', 'yoshi the dinosaur', 'yoshi@eggs.com']]

	def tearDown(self):
		"""Tear down the testing env"""
		self.file_input = None

	def test_db_file_is_formatted_correctly(self):
		"""Test that the db file is correctly formatted for searching"""
		sample_data = ['joegotflow83,admin,joseph moran,joe@absolutod.com',
			'yoshi,dinosaur,yoshi the dinosaur,yoshi@eggs.com']
		self.assertEquals(ORM.clean_file(self, sample_data), self.file_input)

	def test_db_can_find_username(self):
		"""Test that the db can find a username based on an input"""
		orm = ORM(self.file_input)
		self.assertTrue(orm.get_username('joegotflow83') == True)

	def test_db_returns_false_if_no_username_in_db(self):
		"""Test that the db returns False if no username in db"""
		orm = ORM(self.file_input)
		self.assertTrue(orm.get_username('myusername') == False)

	def test_db_can_find_password(self):
		"""Test that the db can find a password based on an input"""
		orm = ORM(self.file_input)
		self.assertTrue(orm.get_password('admin') == True)

	def test_db_returns_false_if_no_password_in_db(self):
		"""Test that the db returns False if no password in db"""
		orm = ORM(self.file_input)
		self.assertFalse(orm.get_password('badpassword'))

	def test_user_can_log_on(self):
		"""Test that when a user provides the correct credentials return True"""
		orm = ORM(self.file_input)
		self.assertTrue(orm.check_credentials('joegotflow83', 'admin'))

	def test_error_occurs_if_invalid_credentials(self):
		"""Test that an exception is thrown if the credentials are invalid"""
		orm = ORM(self.file_input)
		self.assertIn(orm.check_credentials('username', 'password'), 'Invalid Credentials')

	def test_db_can_pull_all_of_users_info_when_logged_in(self):
		"""Test that the users info is pulled once "logged in" """
		orm = ORM(self.file_input)
		self.assertEquals(orm.pull_user_info('joegotflow83'), 
			['joegotflow83', 'admin', 'joseph moran', 'joe@absolutod.com'])

	def test_db_does_not_pull_user_if_username_not_in_db_for_pull_func(self):
		"""Test that if no username is in the db return False"""
		orm = ORM(self.file_input)
		self.assertFalse(orm.pull_user_info('mike'))

	def test_user_gets_welcome_message_when_logged_on(self):
		"""Test that a welcome message is displayed when the user is "logged in" """
		orm = ORM(self.file_input)
		username = self.file_input[0][0]
		self.assertIn(orm.welcome('joegotflow83'), 'Welcome back {}!'.format(username))
