zxcvbn_password
=======

A combination of
[piran’s django-zxcvbn](https://github.com/piran/django-zxcvbn) and
[aj-may’s django-password-strength](https://github.com/aj-may/django-password-strength)
Django apps.

It combines back-end and front-end validation with strength meter display.

Usage
-----

```python
# forms.py

from django import forms
from zxcvbn_password.fields import PasswordField, PasswordConfirmationField

class RegisterForm(forms.Form):
    password1 = PasswordField()
    password2 = PasswordConfirmationField(confirm_with=’password1’)
```

Remember to include `{{ form.media }}` in your template.

Screenshot
----------

![Screenshot](http://img15.hostingpics.net/pics/295712Capturedu20150201153746.png)
