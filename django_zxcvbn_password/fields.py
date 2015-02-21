from django.forms import CharField
from django_zxcvbn_password.validators import (
    length_validator, zxcvbn_validator, max_length_validator)
from django_zxcvbn_password.widgets import (
    PasswordStrengthInput, PasswordConfirmationInput)


class PasswordField(CharField):
    default_validators = [length_validator, zxcvbn_validator]

    def __init__(self, *args, **kwargs):
        if "widget" not in kwargs:
            kwargs["widget"] = PasswordStrengthInput(render_value=False)

        super(PasswordField, self).__init__(*args, **kwargs)


class PasswordConfirmationField(CharField):
    default_validators = [max_length_validator, ]

    def __init__(self, *args, **kwargs):
        if "widget" not in kwargs:
                kwargs["widget"] = PasswordConfirmationInput(
                    confirm_with=kwargs.pop('confirm_with', None))

        super(PasswordConfirmationField, self).__init__(*args, **kwargs)
