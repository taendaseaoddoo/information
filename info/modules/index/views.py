from info import redis_store
from . import index_blu


@index_blu.route('/')
def index():
    redis_store.set("name", "sd")
    return 'index'