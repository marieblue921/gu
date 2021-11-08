from flask import Flask, request, render_template, redirect, Blueprint, url_for, session, jsonify
from module import db
import re

web_class_bp = Blueprint('web_class_bp',__name__)
dbc = db.Database()


@web_class_bp.route('/classes', methods = ['get'])
def classes():
    try:
        if not session.get('logged_in'):
            return redirect(url_for('web_main_bp.login'))
        row = getClassInfoBySchoolSrl(session.get('logged_school_srl'))
        tmp = getTeacherInfoBySchoolSrl(session.get('logged_school_srl'))
        teachers = {}
        for i in tmp:
            teachers[str(i['teacher_srl'])] = i['teacher_name']
        return render_template('class/class_manager.html', title = "학급 관리", usersrl=session.get('logged_user_srl'), schoolsrl=session.get('logged_school_srl'), rows = row, teachers = teachers)
    except Exception as e:
        return str(e)