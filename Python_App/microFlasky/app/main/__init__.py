from flask import Blueprint
main = Blueprint('main',__name__)	#实例化蓝本，第一个参数：蓝本名称，第二个参数：蓝本所在包或模块
from .import views,errors
from ..models import Permission

#在蓝本中编写视图函数主要有两点不同：第一，和前面的错误处理程序一样，路由修饰器由蓝本提供;第二， url_for() 函数的用法不同。你可能还记得， url_for() 函数的第一个参数是路由的端点名， 在程序的路由中，默认为视图函数的名字.在蓝本中就不一样了， Flask 会为蓝本中的全部端点加上一个命名空间，这样就可以在不同的蓝本中使用相同的端点名定义视图函数， 而不会产生冲突。命名空间就是蓝本的名字（ Blueprint 构造函数的第一个参数），所以视图函数 index() 注册的端点名是 main.index，其 URL 使用 url_for('main.index') 获取。url_for() 函数还支持一种简写的端点形式，在蓝本中可以省略蓝本名，例如 url_for('.index')。在这种写法中，命名空间是当前请求所在的蓝本。这意味着同一蓝本中的重定向可以使用简写形式，但跨蓝本的重定向必须使用带有命名空间的端点名

@main.app_context_processor     #Permission类加入模板上下文
def inject_permissions():
    return dict(Permission=Permission)