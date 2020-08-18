"""bookmanager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin


"""
1.urlpatterns 是固定写法 它的值是 列表
2.我们再浏览器中输入的路径会和 urlpatterns中的每一项进行顺序匹配
    如果匹配成功，则直接引导到相应的模块，后续的匹配结束
    如果匹配不成功(把urlpatterns中的每一项都匹配过了)，则直接返回404
3.urlpatterns中的元素 是url
    url的第一个参数是：正则 r 转义 ^ 严格的开始 $ 严格的结尾
4.我们在浏览器中输入的路由 中 哪些部分参与正则匹配
    http://ip:port/path?key=value
    我们的http://ip:port和 get post 参数不参与正则匹配
5.如果和当前的某一向匹配成功，则引导到子应用中继续匹配
    如果匹配成功，则停止匹配返回相应的视图
    如果匹配不成功，则继续和后边的工程中的url的每一项继续匹配，直到匹配过每一项
6.
"""

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 添加一项，只要不是admin/ 肯定会走这个
    # 我们就都引导到 book子应用

    # 在include的第二个参数中添加一个namespace
    # 这样的话 我们的name就变成为了namespace:name

    # namespace 习惯上使用 子应用 的名字
    url(r'^', include('book.urls',namespace='book')),
    url(r'^pay/', include('pay.urls',namespace='pay'))
]
