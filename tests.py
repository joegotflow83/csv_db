import unittest

from orm import ORM


class ViewsTest(unittest.TestCase):


	def test_db_file_is_formatted_correctly(self):
		"""Test that the db file is correctly formatted for searching"""
		sample_data = ['joegotflow83,admin,joseph moran,joe@absolutod.com',
			'yoshi,dinosaur,yoshi the dinosaur,yoshi@eggs.com']
		formatted_data = [['joegotflow83', 'admin', 'joseph moran', 'joe@absolutod.com'],
			['yoshi', 'dinosaur', 'yoshi the dinosaur', 'yoshi@eggs.com']]
		self.assertEquals(ORM.clean_file(self, sample_data), formatted_data)

	def test_db_can_find_username(self):
		"""Test that the db can find a username based on an input"""
		file_input = ['joegotflow83,admin,joseph moran,joe@absolutod.com',
			'yoshi,dinosaur,yoshi the dinosaur,yoshi@eggs.com']
		orm = ORM(file_contents=file_input)
		self.assertTrue(orm.get_username('joegotflow83') == True)
