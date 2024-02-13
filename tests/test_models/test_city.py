#!/usr/bin/python3
"""test city class"""
import unittest
from models.base_model import BaseModel
from models.city import City
import datetime
import os


class Test_city(unittest.TestCase):
    """test city class """

    def setUp(self):
        """setup test inviroment for city calss"""

        self.q1 = City()
        self.q2 = City()

        self.q1.name = "Addis Ababa"

    def test_city_name(self):
        """ test city names """

        self.assertEqual(self.q1.name, "Addis Ababa")
        self.assertNotEqual(self.q2.name, "Addis Ababa")
        self.assertNotEqual(self.q1.name, self.q2.name)
        self.assertEqual(self.q2.name, "")
        self.q2.name = "Asebe Tefri"
        self.assertNotEqual(self.q2.name, "")
        self.assertEqual(self.q2.name, "Asebe Tefri")

    def tearDown(self):
        """Breaks down the testing environment"""

        del self.q1
        del self.q2
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_checks_attributes(self):
        """Checks for class specific attributes"""

        self.assertTrue(hasattr(City(), "state_id"))
        self.assertTrue(hasattr(City(), "name"))

    def test_new_instances(self):
        """Checks that new instances were created"""

        self.assertTrue(self.q1)
        self.assertTrue(self.q2)

    def test_new_instances_attribute_creation(self):
        """Checks that new instances have designated attributes"""
        self.q2.name = "Santa_Cruz"
        self.assertIn("name", self.q2.__dict__)
        self.assertEqual(self.q2.name, "Santa_Cruz")

    def test_non_existant_instance(self):
        """Checks for a non-existant instance"""

        self.c3 = City()
        self.assertIsInstance(self.c3, City)

    def test_inheritence(self):
        """Checks to make sure City inherits from BaseModel"""

        self.assertTrue(issubclass(City, BaseModel))
