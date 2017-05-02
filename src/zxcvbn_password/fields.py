# -*- coding: utf-8 -*-

"""
Fields module.

It provides a password field and a password confirmation field.
"""

from __future__ import unicode_literals

from django.contrib.auth.password_validation import validate_password
from django.forms import CharField

from zxcvbn_password.widgets import (
    PasswordConfirmationInput, PasswordStrengthInput)


class GlobalValidator(object):
    """Validator that uses all validators declared in settings."""

    def __call__(self, value):
        """Call method, run django's validate_password method."""
        return validate_password(value)


class PasswordField(CharField):
    """Password field."""

    default_validators = [GlobalValidator()]

    def __init__(self, *args, **kwargs):
        """
        Init method.

        Args:
            *args (): Django's args for a form field.
            **kwargs (): Django's kwargs for a form field.
        """
        if "widget" not in kwargs:
            kwargs["widget"] = PasswordStrengthInput(render_value=False)

        super(PasswordField, self).__init__(*args, **kwargs)


class PasswordConfirmationField(CharField):
    """Password confirmation field."""

    def __init__(self, *args, **kwargs):
        """
        Init method.

        Args:
            *args (): Django's args for a form field.
            **kwargs (): Django's kwargs for a form field. Should contain a
                confirm_with keyword argument to point to the password field.
        """
        if "widget" not in kwargs:
            kwargs["widget"] = PasswordConfirmationInput(
                confirm_with=kwargs.pop('confirm_with', None))

        super(PasswordConfirmationField, self).__init__(*args, **kwargs)
