import os
from messageboard import app


'''
数据库配置
'''
dev_db = 'sqlite:///' + os.path.join(os.path.dirname(app.root_path),'data.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False 
# 如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', dev_db) 
# 若不存在环境变量DATABASE_URI时，使用dev_db

SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
