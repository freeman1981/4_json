import unittest
import pprint_json


class TestStringMethods(unittest.TestCase):

    def test_good_json(self):
        path_to_good_json = 'json_for_test'
        pprint_json.pretty_print_json(pprint_json.load_data(path_to_good_json))

    def test_bad_json(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_json_not_exists(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
