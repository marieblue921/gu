##사용하는 DB 접근 방식을 확인하고 하나의 Util 모듈로 통일 하면 깔끔하게 좋을것 같은데. 과연..

from module.db import dbc

    #구성을 어떻게 할것인지에 따라 달라진다.
    ##이거 왜 필요했지 ㅋㅋㅋㅋ?
    ###아 이거 사용자 세션 정보에  학번이 없으면 사용하려고 했다!
def GetStudentNumber():
    studentNumber=2014
    return studentNumber



#학번과 원하는 수강 과목 코드를 비교하여 해당 시간의 중복이 있는지 혹은 중복된 과목인지
def CheckOverlap( studentCode, startTime):

    try:
        sql="SELECT lecture_start_time FROM curriculum WHERE curriculum_code in (SELECT curriculum_code FROM management WHERE student_code = %s)"
        row=dbc.executeAll(sql, (studentCode))

        if row :
            for curTime in row:
                if int(curTime['lecture_start_time'])==int(startTime):
                    return False
        else:
            return True
    except Exception as e:
        print(e)

    return True

def CheckFull(curriculumCode ):
    #원하는 과목이 사람이 모두 차 있는지 확인
    try:
        sql="SELECT number_of_students, now_students_number FROM curriculum WHERE curriculum_code = %s"

        row=dbc.executeOne(sql,(curriculumCode))

        if row :
            if row['number_of_students'] > row['now_students_number']:
                return True
            else:
                return False
        else :
            print("CheckFull Error")
            return False 
    except Exception as e:
        print(e)
    return False

def GetCurriculumList():
    # 수강신청한 List 반환
    #myList = [["A10","Database","수1목12","3학년"],["A11","AI","월1화12","3학년"]]
    emptyList=[]
    try:
        sql="SELECT curriculum_code, curriculum_name ,major_name,professor_name,lecture_start_time, number_of_students , now_students_number FROM curriculum "

        curriculumList = dbc.executeAll(sql)

        return curriculumList


    except Exception as e:
        print(e)
        return emptyList

def GetSubjectList():
    
    try:
        sql="SELECT curriculum_code, curriculum_name,major_name,professor_name FROM curriculum AS CC JOIN management AS MG ON CC.curriculum_code = MG.curriculum_code"

        myCurriculumList = dbc.executeAllexecute(sql)


        if myCurriculumList:
            pass
        else:
            pass

    except Exception as e:
        print(e)

def Registration(curriculumCode,studentCode,startTime):
        
    if False==CheckFull(curriculumCode):
       return False
    if False==CheckOverlap(studentCode,startTime):
       return False

    try:
        ##트렌잭션 관리해야함 Update 랑 Insert 동시에 해야함
        insertQuery="INSERT INTO management (student_code,curriculum_code) SELECT %s , %s"
        dbc.execute(insertQuery,(studentCode,curriculumCode))

        ##Update Query 넣어야함. 만약 트리거가 없다면.
        ##updateQuery="UPDATE curriculum SET now_students_number = now_students_number +1 WHERE curriculum_code = %s AND number_of_students > now_students_number"
        ##dbc.execute(updateQuery,(curriculumCode))

        dbc.commit()
    except Exception as e:
        print(e)
        return False

        
    #문제가 없다면 수강신청 execute 결과에 따라 성공 실패여부 return 웹페이지에서는 알림 기능 사용하면될듯.
    return True


#각 함수에서 사용할때는 항상 null check 해야한다. 특히 DB Connection과 WHERE 조건문에 들어가는 변수들