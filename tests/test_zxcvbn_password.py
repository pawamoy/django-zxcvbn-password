# -*- coding: utf-8 -*-

from django.test import TestCase

import zxcvbn_password


class MainTestCase(TestCase):
    def setUp(self):
        pass

    def test_main(self):
        assert zxcvbn_password

    def tearDown(self):
        pass
