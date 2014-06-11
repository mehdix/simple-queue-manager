from flask import flash, url_for, request, redirect, render_template
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.login import login_user, logout_user, login_required

from sqmpy import app, admin
from sqmpy.security import login_manager
from sqmpy.security.forms import LoginForm
from sqmpy.security.models import User
from sqmpy.database import db_session


class UserView(ModelView):
    """
    User view for admin interface
    """
    def __init__(self):
        super(UserView, self).__init__(User, db_session)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # login and validate the user...
        login_user(user)
        flash("Logged in successfully.")
        return redirect(request.args.get('next') or url_for('index'))
    return render_template('security/login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

#Add admin views
admin.add_view(UserView())