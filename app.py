from flask import Flask
from module.web.main import web_bp
##init을 만들고 하나만 init 하도록
from module.registration.CourseRegistration import web_bpr
 
app = Flask(__name__)

app.register_blueprint(web_bp, url_prefix='/')
##init 을 만들고 이거 빼야함
app.register_blueprint(web_bpr, url_prefix='/')
app.config['SECRET_KEY'] = 'abcdefgh'


if __name__=='__main__':
    app.debug=True
    app.run()   