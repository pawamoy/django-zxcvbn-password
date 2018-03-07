from django.conf import settings

from .validators import DEFAULT_MIN_SCORE


def zxcvbn_min_score():
    zxcvbn_validator = None
    for validator in settings.AUTH_PASSWORD_VALIDATORS:
        if validator['NAME'] == 'zxcvbn_password.ZXCVBNValidator':
            zxcvbn_validator = validator
            break

    if zxcvbn_validator is not None:
        zxcvbn_min_score = zxcvbn_validator.get(
            'OPTIONS', {}).get('min_score', DEFAULT_MIN_SCORE)
    else:
        zxcvbn_min_score = DEFAULT_MIN_SCORE

    return int(zxcvbn_min_score)

