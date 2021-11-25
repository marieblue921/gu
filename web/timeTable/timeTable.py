from flask import Flask, request, render_template, redirect, Blueprint, url_for, session, jsonify
from module.timeTable import courselist
table_bp = Blueprint('table_bp',__name__)
null='Null'

@table_bp.route('/timetable', methods=['GET', 'POST'])
def timetable():
    try:
        color_arr = [
            ["#F2D8D8", null, '', ''], ["#FBABAB", null, '', '' ], ["#F7DDA0", null, '', ''], ["#DEEF70", null, '', '' ], ["#F2D8D8", null,'' , ''],
            ["#F7DDA0", null, '', ''], ["#DEEF70", null, '', '' ], ["#F2D8D8", null, '', ''], ["#FBABAB", null, '', '' ], ["#A3EE5C", null, '', ''],
            ["#CBE8AF", null, '', ''], ["#B0F7DE", null, '', '' ], ["#5FF3FA", null, '', ''], ["#54A7E7", null, '', '' ], ["#C6D2EB", null,'' , ''],
            ["#F2D8D8", null, '', ''], ["#FBABAB", null, '', '' ], ["#F7DDA0", null, '', ''], ["#DEEF70", null, '', '' ], ["#F2D8D8", null,'' , ''],
        ]
       #if not session.get('logged_in'):
       #    return redirect(url_for('web_main_bp.login'))
        #row = courselist(session.get('logged_student_code'))
        tmp = courselist.getCourseList(session.get('usercode'))
        print(session.get('usercode'))
        for i in tmp:
            j=tmp.get(i)
            if j[0]==1:
                if j[2]==1: 
                    color_arr[0][1:]=[j[4],j[5],j[3]]
                elif j[2]==3:
                    color_arr[5][1:]=[j[4],j[5],j[3]]
                elif j[2]==5:
                    color_arr[10][1:]=[j[4],j[5],j[3]] 
                elif j[2]==7:
                    color_arr[15][1:]=[j[4],j[5],j[3]]   
            elif j[0]==2:
                if j[2]==1:
                    color_arr[1][1:]=[j[4],j[5],j[3]]
                elif j[2]==3:
                    color_arr[6][1:]=[j[4],j[5],j[3]]
                elif j[2]==5:
                    color_arr[11][1:]=[j[4],j[5],j[3]]
                elif j[2]==7:
                    color_arr[16][1:]=[j[4],j[5],j[3]]
            elif j[0]==3:
                if j[2]==1:
                    color_arr[2][1:]=[j[4],j[5],j[3]]
                elif j[2]==3:
                    color_arr[7][1:]=[j[4],j[5],j[3]]
                elif j[2]==5:
                    color_arr[12][1:]=[j[4],j[5],j[3]]
                elif j[2]==7:
                    color_arr[17][1:]=[j[4],j[5],j[3]]
            elif j[0]==4:
                if j[2]==1:
                    color_arr[3][1:]=[j[4],j[5],j[3]]
                elif j[2]==3:
                    color_arr[8][1:]=[j[4],j[5],j[3]]
                elif j[2]==5:
                    color_arr[13][1:]=[j[4],j[5],j[3]]
                elif j[2]==7:
                    color_arr[18][1:]=[j[4],j[5],j[3]]
            elif j[0]==5:
                if j[2]==1:
                    color_arr[4][1:]=[j[4],j[5],j[3]]
                elif j[2]==3:
                    color_arr[9][1:]=[j[4],j[5],j[3]]
                elif j[2]==5:
                    color_arr[14][1:]=[j[4],j[5],j[3]]
                elif j[2]==7:
                    color_arr[19][1:]=[j[4],j[5],j[3]]
        for j in range(0,len(color_arr)):
            if color_arr[j][1]=='Null':
                color_arr[j][0] ="White"
                color_arr[j][1] =''
        return render_template('timeTable/timeTable.html', title = "나의 수업시간표",array=color_arr)
    except Exception as e:
        return str(e)