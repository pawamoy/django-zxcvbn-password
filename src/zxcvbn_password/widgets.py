# -*- coding: utf-8 -*-

"""Widgets for form fields."""

from __future__ import unicode_literals

from django.forms import PasswordInput
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _

from .utils import zxcvbn_min_score


class PasswordStrengthInput(PasswordInput):
    """Form widget to show the user how strong his/her password is."""

    def render(self, name, value, attrs=None, **kwargs):
        """Widget render method."""
        min_score = zxcvbn_min_score()
        message_title = _('Warning')
        message_body = _(
            'This password would take '
            '<em class="password_strength_time"></em> to crack.')

        strength_markup = """
        <div class="progress-bloc" style="margin-top: 10px;">
            <div class="progress" style="margin-bottom: 10px;">
                <div class="progress-bar
                            progress-bar-warning
                            password_strength_bar"
                     role="progressbar"
                     aria-valuenow="0"
                     aria-valuemin="{min_score}"
                     aria-valuemax="4"
                     style="width: 0%%">
                </div>
            </div>
            <p class="text-muted password_strength_info hidden">
                <span class="label label-danger">
                    {title}
                </span>
                <span style="margin-left:5px;">
                    {body}
                </span>
            </p>
        </div>
        """

        strength_markup = strength_markup.format(
            title=message_title,
            body=message_body,
            min_score=min_score)

        try:
            self.attrs['class'] = '%s password_strength'.strip() % self.attrs['class']  # noqa
        except KeyError:
            self.attrs['class'] = 'password_strength'

        return mark_safe(super(PasswordStrengthInput, self).render(  # nosec
            name, value, attrs) + strength_markup)

    class Media(object):
        """Media class to use in templates."""

        js = (
            'zxcvbn_password/js/zxcvbn.js',
            'zxcvbn_password/js/password_strength.js',
        )


class PasswordConfirmationInput(PasswordInput):
    """Widget to confirm the user password by letting him/her type it again."""

    def __init__(self, confirm_with=None, attrs=None, render_value=False):
        """Init method."""
        super(PasswordConfirmationInput, self).__init__(attrs, render_value)
        self.confirm_with = confirm_with

    def render(self, name, value, attrs=None, **kwargs):
        """Widget render method."""
        if self.confirm_with:
            self.attrs['data-confirm-with'] = 'id_%s' % self.confirm_with

        confirmation_markup = """
        <div style="margin-top: 10px;" class="hidden password_strength_info">
            <p class="text-muted">
                <span class="label label-danger">
                    %s
                </span>
                <span style="margin-left:5px;">%s</span>
            </p>
        </div>
        """ % (_('Warning'), _("Your passwords don't match."))

        try:
            self.attrs['class'] = '%s password_confirmation'.strip() % self.attrs['class']  # noqa
        except KeyError:
            self.attrs['class'] = 'password_confirmation'

        return mark_safe(super(PasswordConfirmationInput, self).render(  # nosec
            name, value, attrs) + confirmation_markup)
