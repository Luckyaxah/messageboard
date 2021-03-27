from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_pyfile('settings.py')

# 数据库handler实例
db = SQLAlchemy(app)



from messageboard import views, errors, commands, forms, models