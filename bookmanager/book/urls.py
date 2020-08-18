from django.conf.urls import url
from book.views import index, detail, set_cookie, get_cookie, set_session, get_session

urlpatterns = [
    # index/
    # url 的第一个参数是正则
    # 第二个参数是视图函数名

    # name就是给url起一个名字
    # 我们可以通过name找到这个路由
    url(r'^index/$', index, name='index'),

    # 位置参数
    # re分组来获取正则匹配中的内容
    # 正则分组的参数会传递给视图，视图定义的时间需要定义接收
    # url(r'^(\d+)/(\d+)/$', detail),

    # 关键字参数 视图中参数位置可变，关键字对应就可以
    url(r'^(?P<category_id>\d+)/(?P<book_id>\d+)/$', detail),
    url(r'^set_cookie/$', set_cookie),
    url(r'^get_cookie/$',get_cookie),
    url(r'^set_session/$',set_session),
    url(r'^get_session/$',get_session),
]