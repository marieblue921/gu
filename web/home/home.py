from flask import render_template, redirect, url_for, session, Blueprint
from module.db import dbc
home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/')
def root():
    if not session.get('logged_in'):
        return redirect(url_for('managing_bp.login'))
    else:
        return render_template('home/home.html', usersrl=session.get('logged_user_srl'), schoolsrl=session.get('logged_school_srl'))


@home_bp.route('/home', methods = ['get'])
def home():
    print('a')

    if not session.get('logged_in'):
        return redirect(url_for('sess_bp.login'))
    sql = 'select * from curriculum'
    row = dbc.executeAll(sql,())
    return render_template('home/home.html', title = "A유치원", usersrl=session.get('logged_user_srl'), schoolsrl=session.get('logged_school_srl'))

