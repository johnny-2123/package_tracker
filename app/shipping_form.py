from flask_wtf import FlaskForm
from wtforms.fields import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired

v = [DataRequired()]


class ShippingForm(FlaskForm):
    senderName = StringField('sender name', v)
    recipientName = StringField('recipient name', v)
    origin = SelectField('origin', v)
    destination = SelectField('destination', v)
    expressShipping = BooleanField('express shipping')
    submit = SubmitField('submit')
    cancel = SubmitField('cancel')
