import sys
sys.path.insert(0, '../')

from FamilyTree import FamilyTree, CHILD_ADDITION_FAILED, PERSON_NOT_FOUND, CHILD_ADDITION_SUCCEEDED
from geektrust import read_initial_tree
import unittest
from contextlib import contextmanager
import os


class TestFamilyTree(unittest.TestCase):
	family=read_initial_tree()

	@contextmanager
	def assertNotRaises(self, exc_type):
		try:
			yield None
		except exc_type:
			raise self.failureException('{} raised'.format(exc_type.__name__))


	def test_add_child_null_child_name(self):

		# Negative Scenario: Tests add_child() for the case when the child name is None
		# Returns Error Message

		parent_name = "Dritha"
		child_name = None
		gender="Female"
		response = self.family.add_child(parent_name, child_name, gender)
		self.assertEqual(response, CHILD_ADDITION_FAILED)


	def test_add_child_null_gender(self):

		# Negative Scenario: Tests add_child() for the case when the gender is None
		# Returns Error Message
		
		parent_name = "Dritha"
		child_name = "Yuvaan"
		gender=None
		response = self.family.add_child(parent_name, child_name, gender)
		self.assertEqual(response, CHILD_ADDITION_FAILED)


	def test_add_child_mother_not_present(self):

		# Negative Scenario: Tests add_child() for the case when the mother name doesn't exist
		# Returns Error Message
		
		parent_name = "Isha"
		child_name = "Yuvika"
		gender = "Female" 
		response = self.family.add_child(parent_name, child_name, gender)
		self.assertEqual(response, PERSON_NOT_FOUND)


	def test_add_child_through_father(self):

		# Negative Scenario: Tests add_child() for the case when added via father
		# Returns Error Message
		
		parent_name = "Jaya"
		child_name = "Yuvaan"
		gender = "Male"
		response = self.family.add_child(parent_name, child_name, gender)
		self.assertEqual(response, CHILD_ADDITION_FAILED)


	def test_child_correct_values(self):

		# Positive Scenario: Tests add_child() for the case when all params are there 
		# and addiiton happens via mother who exists
		
		parent_name = "Dritha"
		child_name = "Yuvaan"
		gender = "Male"
		response = self.family.add_child(parent_name, child_name, gender)
		self.assertEqual(response, CHILD_ADDITION_SUCCEEDED)

	
	def test_add_partner_positive(self):

		# Positive Scenario: Tests add_partner() for the case when all params are there 
		# and addiiton happens via person who exists and does not have a partner

		name = "Ish"
		partner_name = "Isha"
		gender = "Female"
		self.assertNotRaises(self.family.add_partner(name, partner_name, gender)) 


	@unittest.expectedFailure
	def test_add_partner_when_already_present(self):

		# Negative Scenario: Tests add_partner() for the case when partner already exists
		# Raises exception

		name = "Ish"
		partner_name = "Isha"
		gender = "Female"
		self.assertRaises(self.family.add_partner(name, partner_name, gender), Exception) 


	@unittest.expectedFailure
	def test_add_partner_when_person_not_present(self):

		# Negative Scenario: Tests add_partner() for the case when partner doesn't exists
		# Raises exception

		name = "Isha"
		partner_name = "Ish"
		gender = "Male"
		self.assertRaises(self.family.add_partner(name, partner_name, gender), Exception) 


	@unittest.expectedFailure
	def test_add_head_invalid_operation(self):

		# Negative Scenario: Tests add_head() for the case when head already exists
		# Raises exception

		name = "Anita"
		gender = "Female"
		self.assertRaises(Exception, self.family.add_head(name, gender)) 


if __name__ == '__main__': 
    unittest.main()