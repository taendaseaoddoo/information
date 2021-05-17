from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis


class Config(object):
    """项目配置"""
    DEBUG = True

    # 数据库添加配置
    SQLALCHEMY_DATABASE_URI =  "mysql://root:mysql@127.0.0.1:3306/information27"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Redis的配置
    REDIS_host = "127.0.0.1"
    REDIS_PORT = "6379"


app = Flask(__name__)
# 加载配置
app.config.from_object(Config)

# 初始化数据库
db = SQLAlchemy(app)
# 初始化redis存储对象
redis_store  = StrictRedis(host=Config.REDIS_host,port=Config.REDIS_PORT)
# 开启当前项目CSRF保护，只做服务器验证功能
CSRFProtect()


@app.route('/index')
def index():
    pass


if __name__ == '__main__':
    app.run()