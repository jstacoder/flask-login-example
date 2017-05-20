from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, Form
from wtforms.validators import DataRequired, Email, Length, EqualTo

class EmailFieldMixin(Form):
    """
        mixin class to provide email field to forms
    """
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

class PasswordFieldMixin(Form):
    """
        mixin class to provide password field
    """
    def __init__(self, *args, **kwargs):
        super(PasswordFieldMixin, self).__init__(*args, **kwargs)
        password_field = self._fields.pop('password')
        self._fields['password'] = password_field
        if 'password_confirm' in self._fields:
            self._fields['password'].validators.append(
                EqualTo(
                    'password_confirm',
                    'Passwords are not the same.'
                )
            )
            confirm_password_field = self._fields.pop('password_confirm')
            self._fields['password_confirm'] = confirm_password_field
    password = PasswordField(
        'Password',
        validators=[
            DataRequired()
        ]
    )

class LoginForm(FlaskForm, EmailFieldMixin, PasswordFieldMixin):
    '''
    Form Login
    '''
    
class SignupForm(FlaskForm, EmailFieldMixin, PasswordFieldMixin):
    '''
    Form signup
    '''
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Length(
                5, # min
                30, # max
                'You can not have less than 5 characters or more 30.' # error message
            )
        ]
    )    
    password_confirm = PasswordField('Repeat password')
    accept_tos = BooleanField(
        'I accept the terms and conditions.',
        validators=[
            DataRequired('Please accept the terms and conditions.')
        ]
    )
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        tos = self._fields.pop('accept_tos')
        self._fields['accept_tos'] = tos

class EmailResetPasswordForm(FlaskForm, EmailFieldMixin):
    '''
    Form send email reset password
    '''

class ResetPasswordForm(FlaskForm):
    '''
    Form update password
    '''    
    password_confirm = PasswordField('Repeat password')
