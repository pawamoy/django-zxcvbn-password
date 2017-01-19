======================
Django ZXCVBN Password
======================

.. start-badges


|travis|
|codecov|
|landscape|
|version|
|wheel|
|pyup|
|gitter|


.. |travis| image:: https://travis-ci.org/Pawamoy/django-zxcvbn-password.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/Pawamoy/django-zxcvbn-password/

.. |codecov| image:: https://codecov.io/github/Pawamoy/django-zxcvbn-password/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/Pawamoy/django-zxcvbn-password/

.. |landscape| image:: https://landscape.io/github/Pawamoy/django-zxcvbn-password/master/landscape.svg?style=flat
    :target: https://landscape.io/github/Pawamoy/django-zxcvbn-password/
    :alt: Code Quality Status

.. |pyup| image:: https://pyup.io/repos/github/pawamoy/django-zxcvbn-password/shield.svg
    :target: https://pyup.io/repos/github/pawamoy/django-zxcvbn-password/
    :alt: Updates

.. |gitter| image:: https://badges.gitter.im/Pawamoy/django-zxcvbn-password.svg
    :alt: Join the chat at https://gitter.im/Pawamoy/django-zxcvbn-password
    :target: https://gitter.im/Pawamoy/django-zxcvbn-password?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

.. |version| image:: https://img.shields.io/pypi/v/django-zxcvbn-password.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/django-zxcvbn-password/

.. |wheel| image:: https://img.shields.io/pypi/wheel/django-zxcvbn-password.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/django-zxcvbn-password/


.. end-badges

Back-end and Front-end password validation with ZXCVBN.

A combination of
`piran’s django-zxcvbn`_ and `aj-may’s django-password-strength`_ Django apps.
It combines back-end and front-end validation with strength meter display.

.. _piran’s django-zxcvbn: https://github.com/piran/django-zxcvbn
.. _aj-may’s django-password-strength: https://github.com/aj-may/django-password-strength

Installation
============

::

    pip install django-zxcvbn-password


Usage
=====

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
==========

.. image:: http://img15.hostingpics.net/pics/295712Capturedu20150201153746.png


Configuration
=============

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

Development
===========

To run all the tests: ``tox``

License
=======

zxcvbn (https://github.com/lowe/zxcvbn),
django-zxcvbn (https://github.com/piran/django-zxcvbn) and
django-password-strength (https://github.com/aj-may/django-password-strength)
are redistributed under the terms of the BSD license, hence django-zxcvbn-password (https://github.com/Pawamoy/zxcvbn-password) is also redistributed under the terms of the BSD license:

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
