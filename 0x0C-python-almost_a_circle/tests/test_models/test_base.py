#!/usr/bin/python3
"Unittests for `Base` class"
import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    "Unittest for `Base` class."

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
    "Unittest for `to_json_string` method"

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

    def test_two_square_dict(self):
        s1 = Square(5)
        s2 = Square(9)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        result = str(list_dicts).replace("'", '"')
        self.assertEqual(Base.to_json_string(list_dicts), result)


class TestBase_save_to_file(unittest.TestCase):
    "Unittests for `save_to_file` method"

    def test_None_arg(self):
        Rectangle(1, 2).save_to_file(None)
        with open('Rectangle.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), '[]')

    def test_empty_arg_list(self):
        Rectangle(1, 2).save_to_file([])
        with open('Rectangle.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), '[]')

    def test_save_one_rectangle(self):
        r = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([r])
        with open('Rectangle.json', 'r', encoding='utf-8') as f:
            self.assertEqual(json.loads(f.read())[0], r.to_dictionary())

    def test_save_one_square(self):
        s = Square(1, 2, 3, 4)
        Square.save_to_file([s])
        with open('Square.json', 'r', encoding='utf-8') as f:
            self.assertEqual(json.loads(f.read())[0], s.to_dictionary())

    def test_save_two_rectangles(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(6, 7, 8, 9, 10)
        Rectangle.save_to_file([r1, r2])
        with open('Rectangle.json', 'r', encoding='utf-8') as f:
            result = [r1.to_dictionary(), r2.to_dictionary()]
            self.assertEqual(json.loads(f.read()), result)

    def test_save_two_squares(self):
        r1 = Square(1, 2, 3, 4)
        r2 = Square(6, 7, 8, 9)
        Square.save_to_file([r1, r2])
        with open('Square.json', 'r', encoding='utf-8') as f:
            result = [r1.to_dictionary(), r2.to_dictionary()]
            self.assertEqual(json.loads(f.read()), result)


class TestBase_from_json_string(unittest.TestCase):
    "Unittests for `from_json_string` method"

    def test_return_type(self):
        self.assertTrue(type(Base.from_json_string('')), list)

    def test_list_elements_type(self):
        self.assertTrue(type(Base.from_json_string('[{}]')[0]), dict)

    def test_None_arg(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_arg(self):
        self.assertEqual(Base.from_json_string(''), [])

    def test_one_rectangle(self):
        list_input = [{'id': 89, 'width': 10, 'height': 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_two_rectangles(self):
        list_intput = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_intput)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_intput, list_output)

    def test_one_rectangle(self):
        list_input = [{'id': 89, 'width': 10, 'height': 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_two_rectangles(self):
        list_intput = [
            {'id': 89, 'width': 10, 'height': 4, 'x': 14, 'y': 12},
            {'id': 7, 'width': 1, 'height': 7, 'x': 3, 'y': 2}
        ]
        json_list_input = Rectangle.to_json_string(list_intput)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_intput, list_output)

    def test_one_square(self):
        list_input = [{'id': 89, 'size': 10, 'x': 4, 'y': 7}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_two_squares(self):
        list_intput = [
            {'id': 89, 'size': 10, 'x': 14, 'y': 12},
            {'id': 7, 'size': 1, 'x': 3, 'y': 2}
        ]
        json_list_input = Square.to_json_string(list_intput)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_intput, list_output)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.from_json_string('[]', 2)


class TestBase_create(unittest.TestCase):
    "Unittests for `create` method"

    def test_rectangle_return_type(self):
        r = Rectangle(3, 5, 1)
        r_dict = r.to_dictionary()
        self.assertEqual(type(Rectangle.create(**r_dict)), Rectangle)

    def test_create_rectangle(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())

    def test_is_rectangle(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertIsNot(r1, r2)

    def test_equal_rectangle(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_square_return_type(self):
        s = Square(3)
        s_dict = s.to_dictionary()
        self.assertEqual(type(Square.create(**s_dict)), Square)

    def test_create_square(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square.create(**s1.to_dictionary())
        self.assertEqual(s1.to_dictionary(), s2.to_dictionary())

    def test_is_square(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square.create(**s1.to_dictionary())
        self.assertIsNot(s1, s2)

    def test_equal_square(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square.create(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)


class TestBase_load_from_file(unittest.TestCase):
    "Unittests for `load_from_file` method"
    pass


class TestBase_save_to_file_csv(unittest.TestCase):
    "Unittests for `save_to_file_csv` method"
    pass


class TestBase_load_from_file_csv(unittest.TestCase):
    "Unittests for `load_from_file_csv` method"
    pass


if __name__ == '__main__':
    unittest.main()
