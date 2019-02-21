=========
Changelog
=========

2.0.3 (2019-02-21)
==================

- Use new location for package ``python-zxcvbn``, now ``zxcvbn`` (2ea1b69).


2.0.2 (2018-08-21)
==================

Documented
----------
- Improve usage notes (7a1ed42). Related issues/PRs: #31.

Fixed
-----
- Fix call to super in PasswordConfirmationInput (fc551b8).
- Improve password validator help text (c5d21a1). Related issues/PRs: #46.
- Strength bar color go green only when superior to min score (9a44fd8). Related issues/PRs: #3.

Tests
-----
- Add django 1.11 tests (815aaef).
- Add py37/pypy plus django 2.0 tests, remove py34 tests (05711cd).

2.0.1 (2017-02-17)
==================

* Fix call to super in PasswordStrengthInput.

2.0.0 (2017-02-17)
==================

* Drop Django 1.8 support in favor of AUTH_PASSWORD_VALIDATORS setting
  introduced in Django 1.9.
* Update zxcvbn to more recent version (dwolfhub/zxcvbn-python on GitHub).
* Update JavaScript code to latest version.
* Remove all settings (they now go in AUTH_PASSWORD_VALIDATOR options).
* Change license to ISC.

Thanks to Nick Stefan and Daniel Wolf.

1.1.0 (2016-10-18)
==================

* Cookiecutterize the project.

1.0.5 (2015-03-31)
==================

* I don't remember.

1.0.3 (2015-03-12)
==================

* Switch README to rst.
* Fix manifest rules.

1.0.2 (2015-03-12)
==================

* Change package name from django_zxcvbn_password to zxcvbn_password.

1.0.0 (2015-02-21)
==================

* Beta release on PyPI.

0.1.0 (2015-02-01)
==================

* Alpha release on PyPI.
