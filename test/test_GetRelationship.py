import sys
sys.path.insert(0, '../')

from FamilyTree import FamilyTree
from Relationship import GetRelationship
from geektrust import read_initial_tree
import unittest
import os

relation=GetRelationship()

class TestGetRelationship(unittest.TestCase):
	family=read_initial_tree()


	def test_get_siblings_when_exists(self):

		# Positive Scenario: Tests get_siblings() for the case when the siblings exists

		person_name="Ish"
		siblings=["Chit", "Vich", "Aras", "Satya"]
		person = self.family.get_family_member(person_name)
		siblings_result = relation.get_siblings(person).split()

		for name in siblings_result:
			self.assertTrue(name in siblings)
		for name in siblings:
			self.assertTrue(name in siblings_result)


	def test_get_siblings_when_not_exists(self):

		# Negative Scenario: Tests get_siblings() for the case when the siblings do not exists
		# Returns None

		person_name="Yodhan"
		person = self.family.get_family_member(person_name)
		siblings_result = relation.get_siblings(person)
		self.assertIsNone(siblings_result)


	def test_get_son_when_exists(self):

		# Positive Scenario: Tests get_son() for the case when the son exists

		person_name = "Amba"
		sons = "Vritha"
		person = self.family.get_family_member(person_name)
		sons_result = relation.get_son(person)
		for name in sons_result:
			self.assertTrue(name in sons)	


	def test_get_son_when_not_exists(self):

		# Negative Scenario: Tests get_son() for the case when the son does not exists
		# Returns None

		person_name="Atya"
		person = self.family.get_family_member(person_name)
		sons_result = relation.get_son(person)
		self.assertIsNone(sons_result)


	def test_get_daughter_when_exists(self):

		# Positive Scenario: Tests get_daughter() for the case when the daughter exists

		person_name = "Amba"
		daughters=["Dritha","Tritha"]
		person = self.family.get_family_member(person_name)
		daughters_result = relation.get_daughter(person).split()
		for name in daughters_result:
			self.assertTrue(name in daughters)
		for name in daughters:
			self.assertTrue(name in daughters_result)	


	def test_get_daughter_when_not_exists(self):


		# Negative Scenario: Tests get_daughter() for the case when the daughter does not exists
		# Returns None

		person_name="Atya"
		person = self.family.get_family_member(person_name)
		daughters_result = relation.get_daughter(person)
		self.assertIsNone(daughters_result)

		

	def test_get_paternal_uncle_when_exists(self):

		# Positive Scenario: Tests get_paternal_uncle() for the case when the paternal_uncle exists

		person_name = "Kriya"
		paternal_uncle_names = "Asva"
		person = self.family.get_family_member(person_name)
		paternal_uncle_result = relation.get_paternal_uncle(person)
		self.assertEqual(paternal_uncle_result,paternal_uncle_names)


	def test_get_paternal_uncle_when_not_exists(self):

		# Negative Scenario: Tests get_paternal_uncle() for the case when the paternal_uncle does not exists
		# Returns None

		person_name="Atya"
		person = self.family.get_family_member(person_name)
		paternal_uncle_result = relation.get_paternal_uncle(person)
		self.assertIsNone(paternal_uncle_result)


	def test_get_maternal_uncle_when_exists(self):

		# Positive Scenario: Tests get_maternal_uncle() for the case when the maternal_uncle exists

		person_name = "Yodhan"
		maternal_uncle_names = "Vritha"
		person = self.family.get_family_member(person_name)
		maternal_uncle_result = relation.get_maternal_uncle(person)
		self.assertEqual(maternal_uncle_result,maternal_uncle_names)


	def test_get_maternal_uncle_when_not_exists(self):

		# Negative Scenario: Tests get_maternal_uncle() for the case when the maternal_uncle does not exists
		# Returns None

		person_name="Vasa"
		person = self.family.get_family_member(person_name)
		maternal_uncle_result = relation.get_maternal_uncle(person)
		self.assertIsNone(maternal_uncle_result)


	def test_get_paternal_aunt_when_exists(self):

		# Positive Scenario: Tests get_paternal_aunt() for the case when the paternal_aunt exists

		person_name = "Vasa"
		paternal_aunt_names = "Atya"
		person = self.family.get_family_member(person_name)
		paternal_aunt_result = relation.get_paternal_aunt(person)
		self.assertEqual(paternal_aunt_result, paternal_aunt_names)


	def test_get_paternal_aunt_when_not_exists(self):

		# Negative Scenario: Tests get_paternal_aunt() for the case when the paternal_aunt does not exists
		# Returns None

		person_name="Yodhan"
		person = self.family.get_family_member(person_name)
		paternal_aunt_result = relation.get_paternal_aunt(person)
		self.assertIsNone(paternal_aunt_result)


	def test_get_maternal_aunt_when_exists(self):

		# Positive Scenario: Tests get_maternal_aunt() for the case when the maternal_aunt exists

		person_name = "Yodhan"
		maternal_aunt_names = "Tritha"
		person = self.family.get_family_member(person_name)
		maternal_aunt_result = relation.get_maternal_aunt(person)
		self.assertEqual(maternal_aunt_result, maternal_aunt_names)


	def test_get_maternal_aunt_when_not_exists(self):

		# Negative Scenario: Tests get_maternal_aunt() for the case when the maternal_aunt does not exists
		# Returns None

		person_name="Laki"
		person = self.family.get_family_member(person_name)
		maternal_aunt_result = relation.get_maternal_aunt(person)
		self.assertIsNone(maternal_aunt_result)


	def test_get_sister_in_law_female(self):

		# Positive Scenario: Tests get_sister_in_law() for the case when the person is female

		person_name="Chitra"
		sister_in_law_name="Satya"	
		person = self.family.get_family_member(person_name)
		sister_in_law_result = relation.get_sister_in_law(person)
		self.assertEqual(sister_in_law_result, sister_in_law_name)
	

	def test_get_sister_in_law_male(self):

		# Positive Scenario: Tests get_sister_in_law() for the case when the person is male
		
		person_name="Vyas"
		sister_in_law_name="Satvy"
		person = self.family.get_family_member(person_name)
		sister_in_law_result = relation.get_sister_in_law(person)
		self.assertEqual(sister_in_law_result, sister_in_law_name)


	def test_get_brother_in_law_female(self):
		
		# Positive Scenario: Tests get_brother_in_law() for the case when the person is female

		person_name="Chitra"
		brother_in_law_name=["Chit","Ish","Vich"]		
		person = self.family.get_family_member(person_name)
		brother_in_law_result = relation.get_brother_in_law(person).split()
		for name in brother_in_law_result:
			self.assertTrue(name in brother_in_law_name)
		for name in brother_in_law_name:
			self.assertTrue(name in brother_in_law_result)
	

	def test_get_brother_in_law_male(self):

		# Positive Scenario: Tests get_brother_in_law() for the case when the person is male

		person_name="Arit"
		brother_in_law_name="Ahit"
		person = self.family.get_family_member(person_name)
		brother_in_law_result = relation.get_brother_in_law(person)
		self.assertEqual(brother_in_law_result, brother_in_law_name)


if __name__ == '__main__': 
    unittest.main()
