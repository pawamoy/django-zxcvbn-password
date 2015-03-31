django-zxcvbn-password
======================

A combination of
`piran’s django-zxcvbn`_ and `aj-may’s django-password-strength`_ Django apps.
It combines back-end and front-end validation with strength meter display.

.. _piran’s django-zxcvbn: https://github.com/piran/django-zxcvbn
.. _aj-may’s django-password-strength: https://github.com/aj-may/django-password-strength

Installation
------------

Run ``pip install django-zxcvbn-password``. Then in your settings:

.. code:: python

    INSTALLED_APPS = (
        ...
        ‘zxcvbn_password’,
        ...
    )

Usage
-----

.. code:: python

    # forms.py

    from django import forms
    from zxcvbn_password.fields import PasswordField, PasswordConfirmationField

    class RegisterForm(forms.Form):
        password1 = PasswordField()
        password2 = PasswordConfirmationField(confirm_with=’password1’)


.. note::

    Remember to include ``{{ form.media }}`` in your template.
    Please refer to the documentation of the two upstream repositories for more information.

Screenshot
----------

.. image:: http://img15.hostingpics.net/pics/295712Capturedu20150201153746.png


Configuration
-------------

You can configure minimum and maximum length of the password,
and the minimum entropy (refer to zxcvbn documentation for more details).
The following values are the default:

.. code:: python

    # settings.py

    PASSWORD_MIN_LENGTH = 8
    PASSWORD_MAX_LENGTH = 128
    PASSWORD_MIN_ENTROPY = 25
    
You can also configure the messages that are displayed when one of these criteria is not respected.
For minimum and maximum length messages, you may use a ``%s``:
it will take the value of the minimum / maximum length.
These options are optional, there already are default messages.

.. code:: python

    # settings.py
    
    from django.utils.translation import ugettext_lazy as _

    PASSWORD_MIN_LENGTH_MESSAGE = _("Please use at least %s characters!")
    PASSWORD_MAX_LENGTH_MESSAGE = _("Wow, there are too much now! The maximum is %s.")
    PASSWORD_MIN_ENTROPY_MESSAGE = _("The complexity of your password is not sufficient...")

License
-------

zxcvbn (https://github.com/lowe/zxcvbn),
django-zxcvbn (https://github.com/piran/django-zxcvbn) and
django-password-strength (https://github.com/aj-may/django-password-strength)
are redistributed under the terms of the BSD license, hence django-zxcvbn-password (https://github.com/Pawamoy/zxcvbn-password) is also redistributed under the terms of the BSD license:

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
