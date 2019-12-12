# -*- coding: utf-8 -*-

"""Validators for form fields."""

from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from zxcvbn import zxcvbn
from zxcvbn.matching import add_frequency_lists


DEFAULT_MIN_SCORE = 3


class ZXCVBNValidator(object):
    """ZXCVBN validator."""

    code = 'password_too_weak'
    DEFAULT_USER_ATTRIBUTES = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, min_score=DEFAULT_MIN_SCORE,
                 user_attributes=DEFAULT_USER_ATTRIBUTES,
                 frequency_lists=None):
        """
        Init method.

        Args:
            min_score (int): minimum score to accept (between 0 and 4).
            user_attributes (tuple): list of user attributes to check.
        """
        if min_score < 1:
            min_score = 1
        elif min_score > 4:
            min_score = 4

        self.min_score = min_score
        self.user_attributes = user_attributes
        self.frequency_lists = frequency_lists or {}

    def __call__(self, value):
        """Call method, run self.validate (can be used in form fields)."""
        return self.validate(value)

    def validate(self, password, user=None):
        """Validate method, run zxcvbn and check score."""
        user_inputs = []
        if user is not None:
            for attribute in self.user_attributes:
                if hasattr(user, attribute):
                    user_inputs.append(getattr(user, attribute))

        add_frequency_lists(self.frequency_lists)

        results = zxcvbn(password, user_inputs=user_inputs)
        if results.get('score', 0) < self.min_score:
            suggestions = results.get('feedback', {}).get('suggestions', [])
            warnings = [results.get('feedback', {}).get('warning', [])]
            raise ValidationError([_(msg) for msg in [*warnings, *suggestions]], code=self.code, params={})

    # pylama:ignore=R0201
    def get_help_text(self):
        """Help text displayed in User forms."""
        return _("Your password can't contain repeated words or characters.")
