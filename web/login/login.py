from flask import request, render_template, redirect, url_for, session, Blueprint
from module.db import dbc

managing_bp = Blueprint('managing_bp', __name__)

@managing_bp.route('/logout', methods = ['get'])
def logout():
    session.clear()
    return redirect('/')

@managing_bp.route('/login', methods = ['post','get'])
def login():
    if request.method == 'POST':
        usercode = request.form['usercode']
        password = request.form['password']
        sql = 'select * from student where student_code = %s AND student_password  = %s'
        row = dbc.executeOne(sql,(usercode, password))
        if row:
            session['usercode'] = row['student_code']
            session['password'] = row['student_password']
            session['logged_in'] = True
            return redirect(url_for("home_bp.home") )
        else:
            msg = 'Incorrect username/password!'
    return render_template('login/login.html', title = "로그인")