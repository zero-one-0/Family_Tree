import sys
sys.path.insert(0, '../')

from FamilyTree import FamilyTree, CHILD_ADDITION_FAILED, PERSON_NOT_FOUND, CHILD_ADDITION_SUCCEEDED
from Person import Person
from geektrust import read_initial_tree
import unittest
from contextlib import contextmanager
import os


class TestPerson(unittest.TestCase):
	family=read_initial_tree()

	@contextmanager
	def assertNotRaises(self, exc_type):
		try:
			yield None
		except exc_type:
			raise self.failureException('{} raised'.format(exc_type.__name__))


	def test_add_partner(self):

		# Tests Partner Additon for a Person
		
		person_name = "Ish"
		partner_name = "Isha"
		gender = "Female"
		partner=Person(partner_name, gender)
		person = self.family.get_family_member(person_name)
		person.add_partner(partner)

		self.assertEqual(partner_name, person.partner.name)


	def test_add_children(self):

		# Tests Child Additon for a Person
		
		parent_name = "Dritha"
		child_name = "Yuvaan"
		gender= "Female"
		child = Person(child_name, gender)
		person = self.family.get_family_member(parent_name)
		person.add_children(child)
		children = person.get_children()
		self.assertTrue(child_name in children)

	
	def test_get_child(self):

		# Tests Partner Retrieval for a Person

		parent_name = "Dritha"
		child_name = ["Yodhan"]
		gender="M"
		person = self.family.get_family_member(parent_name)
		response = person.get_child(gender)
		self.assertEqual(child_name, response)


	def test_get_siblings(self):

		# Tests Sibling Retrieval for a Person

		person_name= "Laki"
		siblings=["Lavnya"]
		person = self.family.get_family_member(person_name)	
		response = person.get_siblings()
		response = [c.name for c in response]
		self.assertEqual(siblings, response)	


if __name__ == '__main__': 
    unittest.main()
