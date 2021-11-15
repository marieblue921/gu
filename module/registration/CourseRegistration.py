##구성을 main 안에 넣겠다는건지 Page 별로 나누겠다는건지 확신이 없기에 일단 따로 구현
##이런식으로 구현 하면 블루포인터를 계속 생성해야 하는 문제점이 있음. web.main.__init__.py에 initialize 기능과 login, root 등 구분 하여 리펙토링 필요
from flask import request, render_template, redirect, url_for, session, Blueprint
from module.registration.DbUtil import *
#from flask_restful import Resourece

##리펙토링 후 import로 변경하면 될것으로 생각됨
web_bpr = Blueprint('web_bpr', __name__)


##파라미터 의미
##함수 동작정의
##구현한사람

    ##POST의 동작과 GET 동작 나누어 구현필요

    ##GET은 페이지 표시

    ##POST는 수강신청


@web_bpr.route('/registration/api', methods = ['post'])
def RegistrationAPI():

    ##startTime이거 변경해야함 Query짤 시간이 없기에 그냥 ....
    if request.method == 'POST':
        if True==Registration(request.form['curriculumCode'],request.form['studentCode'],request.form['startTime']):
            return {'result':"success"}
        else :
            return {'result':"fail"}