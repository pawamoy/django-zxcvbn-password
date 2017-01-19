# -*- coding: utf-8 -*-

"""Validators for form fields."""

from __future__ import unicode_literals

from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from zxcvbn import zxcvbn

# Settings
PASSWORD_MIN_LENGTH = getattr(settings, "PASSWORD_MIN_LENGTH", 8)
PASSWORD_MAX_LENGTH = getattr(settings, "PASSWORD_MAX_LENGTH", 128)
PASSWORD_MIN_ENTROPY = getattr(settings, "ZXCVBN_MIN_ENTROPY", 25)
PASSWORD_MIN_LENGTH_MESSAGE = getattr(
    settings, "PASSWORD_MIN_LENGTH_MESSAGE",
    _("Password must be %s characters or more."))
PASSWORD_MAX_LENGTH_MESSAGE = getattr(
    settings, "PASSWORD_MAX_LENGTH_MESSAGE",
    _("Password must be %s characters or less."))
PASSWORD_MIN_ENTROPY_MESSAGE = getattr(
    settings, "PASSWORD_MIN_ENTROPY_MESSAGE",
    _("Password must be more complex"))


def clean_user_inputs(password, user_inputs):
    return zxcvbn(password, user_inputs)


class LengthValidator(object):
    """Validate the length of the password."""

    code = "length"

    def __init__(self, min_length=None, max_length=None):
        """
        Init method.

        Args:
            min_length (int): the minimum length.
            max_length (int): the maximum length.
        """
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, value):
        """
        Call method.

        Args:
            value (str): value to validate.

        Raises:
            ValidationError: when length < min_length or length > max_length.
        """
        if self.min_length and len(value) < self.min_length:
            raise ValidationError(
                message=PASSWORD_MIN_LENGTH_MESSAGE % self.min_length,
                code=self.code)
        elif self.max_length and len(value) > self.max_length:
            raise ValidationError(
                message=PASSWORD_MAX_LENGTH_MESSAGE % self.max_length,
                code=self.code)


class ZXCVBNValidator(object):
    """ZXCVBN validator."""

    code = "zxcvbn"

    def __call__(self, value):
        """
        Call method.

        Args:
            value (str): value to validate.

        Raises:
            ValidationError: when password entropy < minimum entropy.
        """
        res = zxcvbn(value)
        if res['score'] < PASSWORD_MIN_ENTROPY:
            raise ValidationError(PASSWORD_MIN_ENTROPY_MESSAGE, code=self.code)


length_validator = LengthValidator(PASSWORD_MIN_LENGTH, PASSWORD_MAX_LENGTH)
max_length_validator = LengthValidator(max_length=PASSWORD_MAX_LENGTH)
zxcvbn_validator = ZXCVBNValidator()
