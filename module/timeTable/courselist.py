from module.db import dbc


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
            sql = "select  lecture_start_time,lecture_building_number from curriculum where curriculum_code = %s"
            row2 = dbc.executeOne(sql, (i))
            day_time=list(map(int,str(row2.get('lecture_start_time'))))
            day_time.append(row2.get('lecture_building_number'))
            my_table[i]=day_time
        return my_table

    except Exception as e:
        return str(e)


