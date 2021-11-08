from flask import Flask
from module.web.main import web_bp
 
app = Flask(__name__)

app.register_blueprint(web_bp, url_prefix='/')
app.config['SECRET_KEY'] = 'abcdefgh'


if __name__=='__main__':
    app.debug=True
    app.run()   