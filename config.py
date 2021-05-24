from redis import StrictRedis


class Config(object):
    """项目配置"""
    DEBUG = True

    SECRET_KEY = "uegfdsbwiqoyqigfwfqiqgfugfwiqdigi"

    # 数据库添加配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information27"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Redis的配置
    REDIS_host = "127.0.0.1"
    REDIS_PORT = "6379"

    # Session保存配置
    SESSION_TYPE = "redis"
    # 开启session签名
    SESSION_USE_SIGNER = True
    # 指定Session 保存的 redis
    SESSION_REDIS = StrictRedis(host=REDIS_host,port=REDIS_PORT)
    # 设置需要过期
    SESSION_PERMANENT = False
    # 设置过期时间
    PERMANENT_SESSION_LIFETIME = 86400 * 2