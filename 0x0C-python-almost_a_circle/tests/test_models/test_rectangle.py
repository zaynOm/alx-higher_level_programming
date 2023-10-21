#!/usr/bin/python3
""
import io
import unittest
import unittest.mock
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    ""

    def setUp(self):
        Base._Base__nb_objects = 0
        self.r = Rectangle(5, 9)

    def test_inherits_from_base(self):
        self.assertTrue(isinstance(self.r, Base))
        self.assertEqual(self.r.id, 1)

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

    def test_width_setter_and_getter(self):
        self.assertEqual(self.r.width, 5)
        self.r.width = 10
        self.assertEqual(self.r.width, 10)

    def test_height_setter_and_getter(self):
        self.assertEqual(self.r.height, 9)
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
        self.assertEqual(self.r.width, 5)
        self.assertEqual(self.r.height, 9)
        self.assertEqual(self.r.x, 0)
        self.assertEqual(self.r.y, 0)

    def test_init_with_all_args(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)


class TestRectangle_width(unittest.TestCase):

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle('invalid', 1)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle(5.0, 1)

    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle(None, 1)

    def test_bool_width(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle(True, 1)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle([4, 5], 2)

    def test_set_width(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle({4, 5}, 2)

    def test_dict_width(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle({'a': 4, 'b': 5}, 2)

    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            Rectangle((4, 5), 2)

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Rectangle(0, 1)

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            Rectangle(-5, 1)


class TestRectangle_height(unittest.TestCase):

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(1, 'invalid')

    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(1, 5.0)

    def test_None_height(self):
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(1, None)

    def test_bool_height(self):
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(1, True)

    def test_list_height(self):
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(1, [4, 5])

    def test_set_height(self):
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(1, {4, 5})

    def test_dict_height(self):
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(1, {'a': 4, 'b': 5})

    def test_tuple_height(self):
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(1, (4, 5))

    def test_zero_height(self):
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            Rectangle(1, 0)

    def test_negative_height(self):
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            Rectangle(1, -5)


class TestRectangle_x(unittest.TestCase):

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(1, 2, 'invalid')

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(1, 2, 5.0)

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(1, 2, None)

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(1, 2, True)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(1, 2, [4, 5], 3)

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(1, 2, {4, 5}, 3)

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(1, 2, {'a': 4, 'b': 5}, 3)

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            Rectangle(1, 2, (4, 5), 3)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            Rectangle(1, 2, -5)


class TestRectangle_y(unittest.TestCase):

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(1, 2, 3, 'invalid')

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(1, 2, 3, 5.0)

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(1, 2, 3, None)

    def test_bool_y(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(1, 2, 3, True)

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(1, 2, 3, [4, 5])

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(1, 2, 3, {4, 5})

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(1, 2, 3, {'a': 4, 'b': 5})

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            Rectangle(1, 2, 3, (4, 5))

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            Rectangle(1, 2, 3, -5)


class TestRectangle_area(unittest.TestCase):
    "Unittests for `area` method of the `Rectangle` class."

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 5).area(4)

    def test_simple_area(self):
        r = Rectangle(2, 5)
        self.assertEqual(r.area(), 10)

    def test_big_area(self):
        r = Rectangle(98898989899898798679867, 8986786796589898987)
        self.assertEqual(r.area(), 888784136628488299669764519379902480594729)

    def test_changed_attributes(self):
        r = Rectangle(2, 5)
        r.width = 44
        r.height = 12
        self.assertEqual(r.area(), 528)


class TestRectangle_display_and_str(unittest.TestCase):
    "Unittests for `display` & `__str__` methods of the `Rectangle` class."

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, fun, expected_output, mock_stdout):
        fun()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 5).display(5)

    def test_simple_display(self):
        self.assert_stdout(Rectangle(2, 2).display, '##\n##\n')

    def test_bigger_display(self):
        output = '#####\n#####\n#####\n#####\n#####\n#####\n#####\n#####\n'
        self.assert_stdout(Rectangle(5, 8).display, output)

    def test_display_with_x(self):
        self.assert_stdout(Rectangle(2, 3, 2).display, '  ##\n  ##\n  ##\n')

    def test_display_with_y(self):
        self.assert_stdout(Rectangle(2, 3, 0, 3).display, '\n\n\n##\n##\n##\n')

    def test_display_with_x_and_y(self):
        output = '\n\n\n  ##\n  ##\n  ##\n'
        self.assert_stdout(Rectangle(2, 3, 2, 3).display, output)

    def test_str(self):
        r = Rectangle(5, 3)
        self.assertEqual(str(r), f'[Rectangle] ({r.id}) 0/0 - 5/3')
        r.x = 9
        r.y = 7
        self.assertEqual(str(r), f'[Rectangle] ({r.id}) 9/7 - 5/3')

    def test_str_with_args(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 3).__str__(5)


class TestRectangle_update(unittest.TestCase):
    "Unittests for the `update` method of the `Rectangle` class."

    def setUp(self):
        self.r = Rectangle(1, 1, 1, 1, 1)

    def test_update_with_no_args(self):
        self.r.update()
        self.assertEqual(str(self.r), '[Rectangle] (1) 1/1 - 1/1')

    def test_update_id(self):
        self.r.update(6)
        self.assertEqual(self.r.id, 6)

    def test_update_width(self):
        self.r.update(6, 7)
        self.assertEqual(self.r.width, 7)

    def test_update_height(self):
        self.r.update(6, 7, 8)
        self.assertEqual(self.r.height, 8)

    def test_update_x(self):
        self.r.update(6, 7, 8, 9)
        self.assertEqual(self.r.x, 9)

    def test_update_y(self):
        self.r.update(6, 7, 8, 9, 10)
        self.assertEqual(self.r.y, 10)

    def test_invalid_width(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            self.r.update(1, "invalid")

    def test_negative_with(self):
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            self.r.update(1, 0)

    def test_invalid_height(self):
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            self.r.update(1, 2, "invalid")

    def test_negative_height(self):
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            self.r.update(1, 2, 0)

    def test_invalid_x(self):
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            self.r.update(1, 2, 3, "invalid")

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            self.r.update(1, 2, 3, -4)

    def test_invalid_y(self):
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            self.r.update(1, 2, 3, 4, "invalid")

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            self.r.update(1, 2, 3, 4, -5)

    def test_update_kwargs_id(self):
        self.r.update(id=12)
        self.assertEqual(self.r.id, 12)

    def test_update_kwargs_width(self):
        self.r.update(width=13)
        self.assertEqual(self.r.width, 13)

    def test_update_kwargs_height(self):
        self.r.update(height=14)
        self.assertEqual(self.r.height, 14)

    def test_update_kwargs_x(self):
        self.r.update(x=15)
        self.assertEqual(self.r.x, 15)

    def test_update_kwargs_y(self):
        self.r.update(y=16)
        self.assertEqual(self.r.y, 16)

    def test_update_kwargs(self):
        self.r.update(width=13, id=12, x=15, y=16, height=14)
        self.assertEqual(str(self.r), '[Rectangle] (12) 15/16 - 13/14')

    def test_invalid_kwargs_width(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            self.r.update(id=1, width="invalid")

    def test_negative_kwargs_with(self):
        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            self.r.update(x=1, width=0)

    def test_invalid_kwargs_height(self):
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            self.r.update(id=1, x=2, height="invalid")

    def test_negative_kwargs_height(self):
        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            self.r.update(height=0)


class TestRectangle_to_dictionary(unittest.TestCase):
    "Unittests for `to_dictionary` method of the `Rectangle` class."

    def test_return_type(self):
        self.assertEqual(type(Rectangle(1, 2).to_dictionary()), dict)

    def test_to_dictionary(self):
        r = Rectangle(1, 2, 3, 4, 5)
        result = {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        self.assertEqual(r.to_dictionary(), result)

    def test_to_dictionary_with_args(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2).to_dictionary(3)

    def test_not_the_same_obj(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(6, 7, 8, 9)
        r2.update(**r1.to_dictionary())
        self.assertFalse(r1 == r2)


if __name__ == '__main__':
    unittest.main()
