from flask import Flask
from web.home.home import home_bp
from web.login.login import managing_bp
from web.timeTable.timeTable import table_bp
from web.registration.registration import reg_bp
 
app = Flask(__name__)

app.register_blueprint(home_bp, url_prefix='/')
app.register_blueprint(managing_bp, url_prefix='/')
app.register_blueprint(table_bp, url_prefix='/')
app.register_blueprint(reg_bp, url_prefix='/')
app.config['SECRET_KEY'] = 'abcdefgh'


if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0')   