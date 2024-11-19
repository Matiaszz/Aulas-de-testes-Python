'''
class Person:
    __init__:
        name str
        surname str
        receive_data bool

    API:
        receive_all_data -> method
            OK
            404

            (receive_data turns True if response of api has connected)
'''
try:
    import sys
    from pathlib import Path

    src_path = Path(__file__).parent.parent / 'src'
    sys.path.append(str(src_path))

except Exception:
    raise


import unittest
from unittest.mock import patch
from person import Person  # type: ignore


class TestPerson(unittest.TestCase):

    def setUp(self):
        self.p1 = Person('Allan', 'Matias')
        self.p2 = Person('Davi', 'Balieiro')

    def test_person_attr_NAME_has_value(self):
        self.assertEqual(self.p1.name, 'Allan')
        self.assertEqual(self.p2.name, 'Davi')

    def test_person_attr_SURNAME_has_value(self):
        self.assertEqual(self.p1.surname, 'Matias')
        self.assertEqual(self.p2.surname, 'Balieiro')

    def test_person_attr_RECEIVE_DATA_has_default_value_equals_to_FALSE(self):
        self.assertFalse(self.p1.receive_data)
        self.assertFalse(self.p2.receive_data)

    def test_person_attr_NAME_is_str(self):
        self.assertIsInstance(self.p1.name, str)
        self.assertIsInstance(self.p2.name, str)

    def test_person_attr_SURNAME_is_str(self):
        self.assertIsInstance(self.p1.surname, str)
        self.assertIsInstance(self.p2.surname, str)

    def test_receive_all_data_success_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.receive_all_data(), 'CONNECTED')
            self.assertTrue(self.p1.receive_data)

            self.assertEqual(self.p2.receive_all_data(), 'CONNECTED')
            self.assertTrue(self.p2.receive_data)

    def test_receive_all_data_fail_404(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False

            self.assertEqual(self.p1.receive_all_data(), 'Error 404')
            self.assertFalse(self.p1.receive_data)

            self.assertEqual(self.p2.receive_all_data(), 'Error 404')
            self.assertFalse(self.p2.receive_data)

    def test_receive_all_data_success_and_fail_sequential(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True

            self.assertEqual(self.p1.receive_all_data(), 'CONNECTED')
            self.assertTrue(self.p1.receive_data)

            self.assertEqual(self.p2.receive_all_data(), 'CONNECTED')
            self.assertTrue(self.p2.receive_data)

            fake_request.return_value.ok = False

            self.assertEqual(self.p1.receive_all_data(), 'Error 404')
            self.assertFalse(self.p1.receive_data)

            self.assertEqual(self.p2.receive_all_data(), 'Error 404')
            self.assertFalse(self.p2.receive_data)


if __name__ == '__main__':
    unittest.main(verbosity=2)
