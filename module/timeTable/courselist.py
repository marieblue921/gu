from module.db import dbc

allCourse = []
def getAllCourse():
    try:
        sql = "select curriculum_code from management where student_code = %s"
        row = dbc.executeAll(sql, ())


    except Exception as e:
        return str(e)


def getCourseList(srl):
    try:
        sql = "select curriculum_code from management where student_code = %s"
        row = dbc.executeAll(sql, (srl))
        #courses= list(row.values())
        courses=[]
        my_table={}
        for i in row:
            courses.append(i.get('curriculum_code'))
        print(courses)
        for i in courses:
            sql = "select  curriculum_name, lecture_start_time,lecture_building_number,lecture_building_name from curriculum where curriculum_code = %s"
            row2 = dbc.executeOne(sql, (i))
            day_time=list(map(int,str(row2.get('lecture_start_time'))))
            day_time.append(row2.get('lecture_building_number'))
            day_time.append(row2.get('curriculum_name'))
            day_time.append(row2.get('lecture_building_name'))
            my_table[i]=day_time
            
        print(my_table)
        return my_table

    except Exception as e:
        return str(e)


