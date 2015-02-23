django-zxcvbn-password
=======

A combination of
[piran’s django-zxcvbn](https://github.com/piran/django-zxcvbn) and
[aj-may’s django-password-strength](https://github.com/aj-may/django-password-strength)
Django apps.

It combines back-end and front-end validation with strength meter display.

Installation
------------

Run `pip install django-zxcvbn-password`  
Then in your settings:

```python
INSTALLED_APPS = (
    ...
    ‘django_zxcvbn_password’,
    ...
)
```

Usage
-----

```python
# forms.py

from django import forms
from django_zxcvbn_password.fields import PasswordField, PasswordConfirmationField

class RegisterForm(forms.Form):
    password1 = PasswordField()
    password2 = PasswordConfirmationField(confirm_with=’password1’)
```

Remember to include `{{ form.media }}` in your template.
Please refer to the documentation of the two upstream repository for more information.

Screenshot
----------

![Screenshot](http://img15.hostingpics.net/pics/295712Capturedu20150201153746.png)


Configuration
-------------

You can configure minimum and maximum length of the password,
and the minimum entropy (refer to zxcvbn documentation for more details).
The following values are the default:

```python
# settings.py

PASSWORD_MIN_LENGTH = 8
PASSWORD_MAX_LENGTH = 128
PASSWORD_MIN_ENTROPY = 25
```

License
-------

zxcvbn (https://github.com/lowe/zxcvbn),
django-zxcvbn (https://github.com/piran/django-zxcvbn) and
django-password-strength (https://github.com/aj-may/django-password-strength)
are redistributed under the terms of the BSD license, hence django-zxcvbn-password (https://github.com/Pawamoy/zxcvbn-password) is also redistributed under the terms of the BSD license:

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

