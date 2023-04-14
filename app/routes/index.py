from flask import Blueprint, redirect, render_template, url_for
from ..shipping_form import ShippingForm
from ..models import Package
from map import map
from map.map import advance_delivery, DELIVERED

from ..models import db


bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    packages = Package.query.all()

    return render_template('package_status.html', packages=packages)


@bp.route('/new_package', methods=['GET', 'POST'])
def new_package():
    form = ShippingForm()
    cities = map.map
    form.origin.choices = [(key) for key in cities]
    form.destination.choices = [(key) for key in cities]

    if form.validate_on_submit():
        if form.cancel.data:
            return redirect(url_for('.new_package'))

        package = Package(
            sender=form.senderName.data,
            recipient=form.recipientName.data,
            origin=form.origin.data,
            destination=form.destination.data,
            location=form.origin.data
        )

        db.session.add(package)
        db.session.commit()
        Package.advance_all_locations()
        return redirect(url_for('.index'))

    return render_template('shipping_request.html', form=form)
