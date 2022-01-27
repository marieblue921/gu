from flask import Flask, request, render_template, redirect, Blueprint, url_for, session, jsonify
from module.registration.DbUtil import *

reg_bp = Blueprint('reg_bp', __name__)

@reg_bp.route('/registration/api', methods = ['post'])
def RegistrationAPI():
    ##startTime이거 변경해야함 Query짤 시간이 없기에 그냥 ....
    if request.method == 'POST':
        if True==Registration(request.form['curriculumCode'],session.get('usercode'),request.form['startTime']):
            return {'result':"success"}
        else :
            return {'result':"fail"}

@reg_bp.route('/registration', methods = ['post','get'])
def registration():
    if not session.get('logged_in'):
        return redirect(url_for('web_bp.login'))

    curriculumList=GetCurriculumList()
    print(curriculumList)
    for i in curriculumList:
        strTmp = ""
        lectureTmp = int(i['lecture_start_time'])
        day = int(lectureTmp/100)
        time = lectureTmp%100
        if day==1:
            strTmp = "월 "
        elif day==2:
            strTmp = "화 "
        elif day==3:
            strTmp = "수 "
        elif day==4:
            strTmp = "목 "
        elif day==5:
            strTmp = "금 "
        strTmp = strTmp + str(time) + " / " + str(time+1)
        i['lecture_start_time'] = strTmp
    return render_template('registration/registration.html', title ="수강 신청", curriculumList =curriculumList)