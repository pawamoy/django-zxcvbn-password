# -*- coding: utf-8 -*-

"""Main test script."""


from django.test import TestCase

import zxcvbn_password


class MainTestCase(TestCase):
    """Main Django test case."""

    def setUp(self):
        """Setup method."""
        self.package = zxcvbn_password

    def test_main(self):
        """Main test method."""
        assert self.package

    def tearDown(self):
        """Tear down method."""
        del self.package
