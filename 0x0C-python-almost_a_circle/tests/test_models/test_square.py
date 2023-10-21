#!/usr/bin/python3
""
import io
import unittest
import unittest.mock
from models.square import Square
from models.base import Base


class TestSquare(unittest.TestCase):
    ""

    def setUp(self):
        Base._Base__nb_objects = 0
        self.r = Square(5)

    def test_inherits_from_base(self):
        self.assertTrue(isinstance(self.r, Base))
        self.assertEqual(self.r.id, 1)

    def test_access_private_attribute_size(self):
        with self.assertRaises(AttributeError):
            print(self.r.__size)

    def test_access_private_attribute_width(self):
        with self.assertRaises(AttributeError):
            print(self.r.__width)

    def test_access_private_attribute_height(self):
        with self.assertRaises(AttributeError):
            print(self.r.__height)

    def test_access_private_attribute_x(self):
        with self.assertRaises(AttributeError):
            print(self.r.__x)

    def test_access_private_attribute_y(self):
        with self.assertRaises(AttributeError):
            print(self.r.__y)

    def test_size_setter_and_getter(self):
        self.assertEqual(self.r.size, 5)
        self.r.size = 10
        self.assertEqual(self.r.size, 10)

    def test_width_setter_and_getter(self):
        self.assertEqual(self.r.width, 5)
        self.r.width = 10
        self.assertEqual(self.r.width, 10)

    def test_height_setter_and_getter(self):
        self.assertEqual(self.r.height, 5)
        self.r.height = 2
        self.assertEqual(self.r.height, 2)

    def test_x_setter_and_getter(self):
        self.assertEqual(self.r.x, 0)
        self.r.x = 4
        self.assertEqual(self.r.x, 4)

    def test_y_setter_and_getter(self):
        self.assertEqual(self.r.y, 0)
        self.r.y = 8
        self.assertEqual(self.r.y, 8)

    def test_first_two_args(self):
        self.assertEqual(self.r.id, 1)
        self.assertEqual(self.r.size, 5)
        self.assertEqual(self.r.x, 0)
        self.assertEqual(self.r.y, 0)

    def test_init_with_all_args(self):
        r = Square(1, 2, 3, 4)
        self.assertEqual(r.id, 4)
        self.assertEqual(r.size, 1)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)


class TestSquare_size(unittest.TestCase):
    ""

    def test_str_size(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square('invalid', 1)

    def test_float_size(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square(5.0, 1)

    def test_None_size(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square(None, 1)

    def test_bool_size(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square(True, 1)

    def test_list_size(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square([4, 5], 2)

    def test_set_size(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square({4, 5}, 2)

    def test_dict_size(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square({'a': 4, 'b': 5}, 2)

    def test_tuple_size(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Square((4, 5), 2)

    def test_zero_size(self):
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Square(0, 1)

    def test_negative_size(self):
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Square(-5, 1)


class TestSquare_x(unittest.TestCase):

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Square(1, 'invalid')

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Square(1, 5.0)

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Square(1, None)

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Square(1, True)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Square(1, [4, 5], 3)

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Square(1, {4, 5}, 3)

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Square(1, {'a': 4, 'b': 5}, 3)

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Square(1, (4, 5), 3)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            Square(1, -5)


class TestSquare_y(unittest.TestCase):

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Square(1, 2, 'invalid')

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Square(1, 2, 5.0)

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Square(1, 2, None)

    def test_bool_y(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Square(1, 2, True)

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Square(1, 2, [4, 5])

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Square(1, 2, {4, 5})

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Square(1, 2, {'a': 4, 'b': 5})

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Square(1, 2, (4, 5))

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            Square(1, 2, -13)


class TestSquare_area(unittest.TestCase):
    "Unittests for `area` method of the `Square` class."

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Square(2).area(4)

    def test_simple_area(self):
        r = Square(2)
        self.assertEqual(r.area(), 4)

    def test_big_area(self):
        r = Square(98898989899898798679867)
        result = 9781010203220284593324609774393796661951137689
        self.assertEqual(r.area(), result)

    def test_changed_attributes(self):
        r = Square(2)
        r.size = 44
        self.assertEqual(r.area(), 1936)


class TestSquare_display_and_str(unittest.TestCase):
    "Unittests for `display` & `__str__` methods of the `Square` class."

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, fun, expected_output, mock_stdout):
        fun()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Square(2).display(5)

    def test_simple_display(self):
        self.assert_stdout(Square(2).display, '##\n##\n')

    def test_bigger_display(self):
        output = '#####\n#####\n#####\n#####\n#####\n'
        self.assert_stdout(Square(5).display, output)

    def test_display_with_x(self):
        self.assert_stdout(Square(2, 2).display, '  ##\n  ##\n')

    def test_display_with_y(self):
        self.assert_stdout(Square(2, 0, 3).display, '\n\n\n##\n##\n')

    def test_display_with_x_and_y(self):
        self.assert_stdout(Square(2, 3, 2).display, '\n\n   ##\n   ##\n')

    def test_str(self):
        r = Square(5)
        self.assertEqual(str(r), f'[Square] ({r.id}) 0/0 - 5')
        r.x = 9
        r.y = 7
        self.assertEqual(str(r), f'[Square] ({r.id}) 9/7 - 5')

    def test_str_with_args(self):
        with self.assertRaises(TypeError):
            Square(2).__str__(5)


class TestSquare_update(unittest.TestCase):
    "Unittests for the `update` method of the `Square` class."

    def setUp(self):
        self.r = Square(1, 1, 1, 1)

    def test_update_with_no_args(self):
        self.r.update()
        self.assertEqual(str(self.r), '[Square] (1) 1/1 - 1')

    def test_update_id(self):
        self.r.update(6)
        self.assertEqual(self.r.id, 6)

    def test_update_size(self):
        self.r.update(6, 7)
        self.assertEqual(self.r.size, 7)
        self.assertEqual(self.r.width, 7)
        self.assertEqual(self.r.height, 7)

    def test_update_x(self):
        self.r.update(6, 7, 8)
        self.assertEqual(self.r.x, 8)

    def test_update_y(self):
        self.r.update(6, 7, 8, 9)
        self.assertEqual(self.r.y, 9)

    def test_invalid_size(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            self.r.update(1, "invalid")

    def test_negative_size(self):
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            self.r.update(1, 0)

    def test_invalid_x(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            self.r.update(1, 2, "invalid")

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            self.r.update(1, 2, -4)

    def test_invalid_y(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            self.r.update(1, 2, 3, "invalid")

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            self.r.update(1, 2, 3, -5)

    def test_update_kwargs_id(self):
        self.r.update(id=12)
        self.assertEqual(self.r.id, 12)

    def test_update_kwargs_width(self):
        self.r.update(size=13)
        self.assertEqual(self.r.size, 13)
        self.assertEqual(self.r.width, 13)
        self.assertEqual(self.r.height, 13)

    def test_update_kwargs_x(self):
        self.r.update(x=15)
        self.assertEqual(self.r.x, 15)

    def test_update_kwargs_y(self):
        self.r.update(y=16)
        self.assertEqual(self.r.y, 16)

    def test_update_kwargs(self):
        self.r.update(size=13, id=12, x=15, y=16)
        self.assertEqual(str(self.r), '[Square] (12) 15/16 - 13')

    def test_invalid_kwargs_size(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            self.r.update(id=1, size="invalid")

    def test_negative_kwargs_size(self):
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            self.r.update(x=1, width=0)

    def test_invalid_kwargs_x(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            self.r.update(id=1, x="invalid")

    def test_negative_kwargs_x(self):
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            self.r.update(x=-5)

    def test_invalid_kwargs_y(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            self.r.update(id=1, y="invalid")

    def test_negative_kwargs_y(self):
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            self.r.update(y=-3)


class TestSquare_to_dictionary(unittest.TestCase):
    "Unittests for `to_dictionary` method of the Square class."

    def test_return_type(self):
        self.assertEqual(type(Square(1).to_dictionary()), dict)

    def test_to_dictionary(self):
        r = Square(1, 2, 3, 4)
        result = {'id': 4, 'size': 1, 'x': 2, 'y': 3}
        self.assertEqual(r.to_dictionary(), result)

    def test_to_dictionary_with_args(self):
        with self.assertRaises(TypeError):
            Square(1).to_dictionary(3)

    def test_not_the_same_obj(self):
        s1 = Square(1, 2, 3, 4)
        s2 = Square(6, 7, 8, 9)
        s2.update(**s1.to_dictionary())
        self.assertFalse(s1 == s2)


if __name__ == '__main__':
    unittest.main()
