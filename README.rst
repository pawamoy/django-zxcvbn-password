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
`pirandig’s django-zxcvbn`_ and `aj-may’s django-password-strength`_ Django apps.
It combines back-end and front-end validation with strength meter display.

.. _pirandig’s django-zxcvbn: https://github.com/pirandig/django-zxcvbn
.. _aj-may’s django-password-strength: https://github.com/aj-may/django-password-strength

License
=======

Software licensed under `ISC`_ license.

.. _ISC: https://www.isc.org/downloads/software-support-policy/isc-license/

Installation
============

::

    pip install django-zxcvbn-password

Usage
=====

.. code:: python

    # settings.py

    AUTH_PASSWORD_VALIDATORS = [{
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    }, {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    }, {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    }, {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    }, {
        'NAME': 'zxcvbn_password.ZXCVBNValidator',
        'OPTIONS': {
            'min_score': 3,
            'user_attributes': ('username', 'email', 'first_name', 'last_name')
        }
    }]

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


By default, other inputs won't be used to compute the score, but you can enforce it
like this:

.. code:: python

    # forms.py

    from zxcvbn_password import zxcbnn

    # in your form class
    def clean():
        password = self.cleaned_data.get('password')
        other_field1 = ...
        other_field2 = ...

        if password:
            score = zxcvbn(password, [other_field1, other_field2])['score']
            # raise forms.ValidationError if needed

        return self.cleaned_data

Screen-shot
===========

.. image:: https://cloud.githubusercontent.com/assets/3999221/23079032/5ae1513a-f54b-11e6-9d66-90660ad5fb2d.png


Development
===========

To run all the tests: ``tox``
