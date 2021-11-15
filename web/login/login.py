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
        # 쉬운 checking을 위해 변수에 값 넣기
        usercode = request.form['usercode']
        password = request.form['password']
        # MySQL DB에 해당 계정 정보가 있는지 확인
        sql = 'select * from student where student_code = %s AND student_password  = %s'
        # 값이 유무 확인 결과값 account 변수로 넣기
        row = dbc.executeOne(sql,(usercode, password))
        # 정상적으로 유저가 있으면 새로운 세션 만들고, 없으면 로그인 실패 문구 출력하며 index 리다이렉트
        if row:
            session['usercode'] = row['student_code']
            session['password'] = row['student_password']
            session['logged_in'] = True
            return redirect(url_for("home_bp.home") )
        else:
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('login/login.html', title = "로그인")