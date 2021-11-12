from flask import Flask, request, render_template, redirect, url_for, session, Blueprint
from module import db

web_bp = Blueprint('web_bp', __name__)


@web_bp.route('/')
def root():
    if not session.get('logged_in'):
        return redirect(url_for('web_bp.login'))
    else:
        return render_template('main/main.html', usersrl=session.get('logged_user_srl'), schoolsrl=session.get('logged_school_srl'))

@web_bp.route('/login', methods = ['post','get'])
def login():
    if request.method == 'POST':
        user_id = request.form['id']
        user_pwd = request.form['pwd']
        print(user_id)
    
        if user_id=="admin" and user_pwd=="0000":
            session['logged_in'] = True
            return redirect(url_for("web_bp.main") )
    return render_template('login/login.html', title = "로그인")


# @web_bp.route('/login', methods = ['post','get'])
# def login():
#     dbc = db.Database()
#     error = None
#     if request.method == 'POST':
#         user_id = request.form['id']
#         user_pwd = request.form['pwd']
#         sql = 'select * from sf_customer where customer_id = %s AND customer_password = %s'
#         row = dbc.executeOne(sql,(user_id, user_pwd))
#         if row:
#             session['logged_in'] = True
#             session['logged_school_srl'] = row['customer_school_srl']
#             session['logged_user_srl'] = row['customer_srl']
#             return redirect(url_for("app.main") )
#     return render_template('login/login.html', title = "로그인")


@web_bp.route('/main', methods = ['get'])
def main():
    if not session.get('logged_in'):
        return redirect(url_for('web_bp.login'))
    dbc = db.Database()
    sql = 'select * from curriculum'
    row = dbc.executeAll(sql,())
    print(row)
    return render_template('main/main.html', title = "A유치원", usersrl=session.get('logged_user_srl'), schoolsrl=session.get('logged_school_srl'))

@web_bp.route('/logout', methods = ['get'])
def logout():
    session.clear()
    return redirect('/')