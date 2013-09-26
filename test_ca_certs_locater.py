
import ca_certs_locater

import mock

import unittest


class TestLocator(unittest.TestCase):

    @ mock.patch('os.path.exists')
    def test_linux_exists(self, exists):
        # If the file exists, return it
        exists.return_value = True
        fn = ca_certs_locater.get()
        self.assertEqual(fn, ca_certs_locater.LINUX_PATH)

    @ mock.patch('os.path.exists')
    def test_linux_does_not_exist(self, exists):
        # If the file does not exist, fall back
        exists.return_value = False
        self.assertRaises(ImportError, ca_certs_locater.get)
