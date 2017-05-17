from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired('Necesito un E-mail'), Email('Debe tener un formato válido')])
    password = PasswordField('Contraseña', validators=[DataRequired('No me has indicado una contraseña')])


class SignupForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired('Debes indicarnos un nombre de usuario'), Length(5, 30, 'Debe estar entre 5 y 30 carácteres')])
    email = StringField('E-mail', validators=[DataRequired('Necesito un E-mail'), Email('Debe tener un formato válido'), Length(1, 254, 'Es demasiado largo')])
    password = PasswordField('Contraseña', validators=[DataRequired('No me has indicado una contraseña'), EqualTo('password_confirm', 'No coinciden las contraseñas')])
    password_confirm = PasswordField('Repetir contraseña')
    accept_tos = BooleanField('Aceptar condiciones', validators=[DataRequired('Necesito que aceptes mis condiciones. Aqui mando yo.')])


class EmailResetPasswordForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired('Necesito un E-mail'), Email('Debe tener un formato válido')])


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Contraseña', validators=[DataRequired('No me has indicado una contraseña'), EqualTo('password_confirm', 'No coinciden las contraseñas')])
    password_confirm = PasswordField('Repetir contraseña')

