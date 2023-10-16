#!/usr/bin/python3
"Unittests for Base class"
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    "Unittest for Base class."

    def test_id_auto_increment(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, b1.id + 1)

    def test_given_id(self):
        self.assertEqual(Base(99).id, 99)

    def test_mixed_given_auto_id(self):
        b1 = Base()
        b2 = Base(99)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)
        self.assertEqual(b2.id, 99)

    def test_update_id(self):
        b = Base(66)
        self.assertEqual(b.id, 66)
        b.id = 100
        self.assertEqual(b.id, 100)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(11, 7)


class TestBase_to_json_string(unittest.TestCase):
    "Unittest for to_json_string method"

    def test_return_type(self):
        self.assertEqual(type(Base.to_json_string([])), str)

    def test_None_arg(self):
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_empty_arg(self):
        self.assertEqual(Base.to_json_string([]), '[]')

    def test_one_rectangle_dict(self):
        r = Rectangle(5, 9, 7, 3, 2)
        result = str([r.to_dictionary()]).replace("'", '"')
        self.assertEqual(Base.to_json_string([r.to_dictionary()]), result)


if __name__ == '__main__':
    unittest.main()
