from module.registration.CourseRegistration import *

reg_bp = Blueprint('reg_bp', __name__)

@reg_bp.route('/registration', methods = ['post','get'])
def registration():
    if not session.get('logged_in'):
        return redirect(url_for('web_bp.login'))

    curriculumList=GetCurriculumList()

    #세션 처리 후 변경 해야함
    studentCode=2014
    
    return render_template('registration/registration.html', title ="수강 신청", curriculumList =curriculumList , studentCode=studentCode)