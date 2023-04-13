from flask import Blueprint, redirect, render_template, url_for
from ..shipping_form import ShippingForm
from map import map

bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    return 'Package Tracker'


@bp.route('/new_package', methods=['GET', 'POST'])
def new_package():
    form = ShippingForm()
    cities = map.map
    form.origin.choices = [(key) for key in cities]
    form.destination.choices = [(key) for key in cities]

    if form.validate_on_submit():
        if form.cancel.data:
            return redirect(url_for('.new_package'))
        return redirect(url_for('.index'))

    return render_template('shipping_request.html', form=form)
