# -*- coding: utf-8 -*-

"""Main test script."""



from django.test import TestCase

import zxcvbn_password


class MainTestCase(TestCase):
    """Main Django test case"""
    def setUp(self):
        pass

    def test_main(self):
        assert zxcvbn_password

    def tearDown(self):
        pass
