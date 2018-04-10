from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import NumberRange

...

class GarageForm(FlaskForm):
    tag = StringField('Označení')
    period = IntegerField('Perioda hlášení (minuty)', 
        validators=[
        NumberRange(1, 999, 
            message='Perioda musí být mezi 1 a 999')
        ])
    phone = StringField('Telefonní číslo', 
        validators=[
        validate_phone_number
        ])
    note = TextAreaField('Poznámka')