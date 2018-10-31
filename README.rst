======================
Django ZXCVBN Password
======================

.. start-badges


|travis|
|codacygrade|
|codacycoverage|
|version|
|wheel|
|pyup|
|gitter|


.. |travis| image:: https://travis-ci.org/Pawamoy/django-zxcvbn-password.svg?branch=master
    :target: https://travis-ci.org/Pawamoy/django-zxcvbn-password/
    :alt: Travis-CI Build Status

.. |codacygrade| image:: https://api.codacy.com/project/badge/Grade/7f25070e9c46453c8ed054f00aa113b6
    :target: https://app.codacy.com/project/Pawamoy/django-zxcvbn-password/dashboard
    :alt: Codacy Code Quality Status

.. |codacycoverage| image:: https://api.codacy.com/project/badge/Coverage/7f25070e9c46453c8ed054f00aa113b6
    :target: https://app.codacy.com/project/Pawamoy/django-zxcvbn-password/dashboard
    :alt: Codacy Code Coverage

.. |pyup| image:: https://pyup.io/repos/github/pawamoy/django-zxcvbn-password/shield.svg
    :target: https://pyup.io/repos/github/pawamoy/django-zxcvbn-password/
    :alt: Updates

.. |version| image:: https://img.shields.io/pypi/v/django-zxcvbn-password.svg?style=flat
    :target: https://pypi.org/project/django-zxcvbn-password/
    :alt: PyPI Package latest release

.. |wheel| image:: https://img.shields.io/pypi/wheel/django-zxcvbn-password.svg?style=flat
    :target: https://pypi.org/project/django-zxcvbn-password/
    :alt: PyPI Wheel

.. |gitter| image:: https://badges.gitter.im/Pawamoy/django-zxcvbn-password.svg
    :target: https://gitter.im/Pawamoy/django-zxcvbn-password
    :alt: Join the chat at https://gitter.im/Pawamoy/django-zxcvbn-password



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


Requirements
============

The JavaScript code of this application uses JQuery, but JQuery is not bundled
with it. Please install it separately. You might also want to use Bootstrap.

Usage
=====

.. code:: python

    # settings.py

    INSTALLED_APPS = [
        ...
        'zxcvbn_password',
        ...
    ]

    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
        {
            'NAME': 'zxcvbn_password.ZXCVBNValidator',
            'OPTIONS': {
                'min_score': 3,
                'user_attributes': ('username', 'email', 'first_name', 'last_name')
            }
        }
    ]

.. code:: python

    # forms.py

    from django import forms
    from zxcvbn_password.fields import PasswordField, PasswordConfirmationField

    class RegisterForm(forms.Form):
        password1 = PasswordField()
        password2 = PasswordConfirmationField(confirm_with=’password1’)


.. code:: python

    # views.py

    if form.is_valid():
        user = User.objects.create_user(
            username=...,
            password=form.cleaned_data['password1']
        )


By default, other inputs won't be used to compute the score, but you can enforce it
like this:

.. code:: python

    # forms.py

    from django import forms
    from zxcvbn_password import zxcvbn
    from zxcvbn_password.fields import PasswordField, PasswordConfirmationField

    class RegisterForm(forms.Form):
        password1 = PasswordField()
        password2 = PasswordConfirmationField(confirm_with=’password1’)

        def clean(self):
            password = self.cleaned_data.get('password1')
            other_field1 = ...
            other_field2 = ...

            if password:
                score = zxcvbn(password, [other_field1, other_field2])['score']
                # score is between 0 and 4
                # raise forms.ValidationError if needed

            return self.cleaned_data


Screen-shot
===========

.. image:: https://cloud.githubusercontent.com/assets/3999221/23079032/5ae1513a-f54b-11e6-9d66-90660ad5fb2d.png


.. important::

    The password field's widget declares two JavaScript files that must be added to the HTML page.
    To do so, add ``{{ form.media }}`` in your template, something like:

    .. code:: html

        <form role="form" action="my_url" method="post">
          {% csrf_token %}
          {{ form }}
        </form>

        {% block js %}
          {{ block.super }}
          {{ form.media }}
        {% endblock %}


.. note::

    If you are not using Bootstrap, the strength bar will not have colors.
    You can fix this with these three CSS rules:

    .. code:: css

        .progress-bar-warning {
            background-color: yellow;
        }

        .progress-bar-danger {
            background-color: red;
        }

        .progress-bar-success {
            background-color: green;
        }


Documentation
=============

`On ReadTheDocs`_

.. _`On ReadTheDocs`: http://django-zxcvbn-password.readthedocs.io/

Development
===========

To run all the tests: ``tox``
