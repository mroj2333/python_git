from django.shortcuts import render, redirect, reverse
from django.http import HttpRequest,HttpResponse
from book.models import BookInfo,PeopleInfo

# Create your views here.
"""
视图
1.就是python函数
2.函数的第一个参数就是请求 和请求相关的 它是HttpRequest的实例对象
3.我们必须要返回一个响应 响应是HttpResponse的实例对象/子实例对象
"""

def index(request):
    books = BookInfo.objects.all()
    peoples = PeopleInfo.objects.all()
    # request, template_name, context=None
    # 参数1：当前的请求
    # 参数2：模板文件
    # 参数3： context 传递参数

    context = {
        'books':books,
        'peoples':peoples
    }


    # 需求1：登陆成功之后跳转到首页
    # return redirect('/home/')

    # 通过在urls里面给路由起的name别名找到路由
    # path = reverse('index')
    # 如果我们设置了namespace 这个时候就需要通过namespace:name 来获取路由
    # path = reverse('book:name')
    # return redirect(path)

    # 需求2：注册成功之后跳转到首页
    # 同需求1


    return render(request,'index.html',context)


def detail(request,book_id, category_id):
    # print(category_id, book_id)

    #######################GET 查询字符串####################################
    """
    https://www.baidu.com/s?wd=itcast&rsv_spt=1&rsv_iqid=0xdfc98e87000601a4&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=&tn=baiduhome_pg&ch=&rsv_enter=1&rsv_dl=ib&rsv_btype=i&inputT=2216
    以?作为分割
    ?前边 是路由
    ?后边 是查询字符串
    ?key=value&key=value&key=value&...

    我们在登陆的时间会输入用户名和密码 理论上 用户名和密码都应该以POST方式进行传递
    只是为了让大家好理解，接下来我们用get方式传递用户名和密码
    """

    # http://127.0.0.1:8000/2/200/?user=itcast&password=fhsdjk
    # query_params = request.GET
    #
    # print(query_params)
    # < QueryDict: {'password': ['fhsdjk'], 'user': ['itcast']} >

    # http://127.0.0.1:8000/2/200/?user=itcast&password=fhsdjk&user=itheima
    # <QueryDict: {'password': ['fhsdjk'], 'user': ['itcast', 'itheima']}>
    # QueryDict以普通的字典的形式来获取 一键多值的时间只能获取一个值
    # 我们想获取一键多值的话需要使用QueryDict的list方法
    # user = query_params.getlist('user')

    # user = query_params['user']
    # password = query_params.get('password')
    # print(user,password)
    # itcast fhsdjk





#######################POST 表单数据####################################
    # data = request.POST
    # print(data)
    # <QueryDict: {'username': ['itcast'], 'password': ['123']}>



    #######################POST json数据####################################
    """
    # JSON是双引号
    {
        "name":"itcast",
        "password":"123",
    }
    """
    # body = request.body
    # print(body)
    # b'{\n    "username":"itcast",\n    "password":"123"\n}'
    # body_str = body.decode() # JSON形式的字符串
    # print(body_str)
    """
    {
    "username":"itcast",
    "password":"123"
    }
    得到的是一个字符串
    json.dumps 将字典转换为JSON形式的字符串
    json.loads 将JSON形式的字符串转换为字典
    使用前要通过import导入json库 json是python标准库
    """



    #######################请求头####################################

    # print(request.META) request.META 返回的数据为字典类型
    """
    {
      'wsgi.multithread': True,
      'PYCHARM_DISPLAY_PORT': '63342',
      'RUN_MAIN': 'true',
      'LC_TELEPHONE': 'zh_CN.UTF-8',
      'PAPERSIZE': 'a4',
      'PATH_INFO': '/2/200/',
      'LC_NUMERIC': 'zh_CN.UTF-8',
      'XMODIFIERS': '@im=fcitx',
      'LC_IDENTIFICATION': 'zh_CN.UTF-8',
      'PWD': '/home/python/Desktop/study/bookmanager',
      'PYCHARM_HOSTED': '1',
      'QT4_IM_MODULE': 'fcitx',
      'UPSTART_JOB': 'unity7',
      'LC_ADDRESS': 'zh_CN.UTF-8',
      'JOB': 'unity-settings-daemon',
      'wsgi.file_wrapper': <class 'wsgiref.util.FileWrapper'>,
      'HTTP_ACCEPT_ENCODING': 'gzip, deflate, sdch',
      'XDG_SEAT': 'seat0',
      'COMPIZ_BIN_PATH': '/usr/bin/',
      'DBUS_SESSION_BUS_ADDRESS': 'unix:abstract=/tmp/dbus-F4apFGWMi9',
      'XDG_DATA_DIRS': '/usr/share/ubuntu:/usr/share/gnome:/usr/local/share/:/usr/share/:/var/lib/snapd/desktop',
      'CONTENT_LENGTH': '',
      'DISPLAY': ':0',
      'GTK2_MODULES': 'overlay-scrollbar',
      'QUERY_STRING': '',
      'LANGUAGE': 'zh_CN:en_US:en',
      'XDG_SESSION_TYPE': 'x11',
      'SERVER_NAME': 'localhost',
      'wsgi.multiprocess': False,
      'PYTHONUNBUFFERED': '1',
      'SCRIPT_NAME': '',
      'GNOME_KEYRING_PID': '',
      'DJANGO_SETTINGS_MODULE': 'bookmanager.settings',
      'IM_CONFIG_PHASE': '1',
      'REQUEST_METHOD': 'GET',
      'XAUTHORITY': '/home/python/.Xauthority',
      'wsgi.version': (1, 0),
      'CLUTTER_IM_MODULE': 'xim',
      'LC_NAME': 'zh_CN.UTF-8',
      'SHLVL': '0',
      'PYTHONPATH': '/home/python/Desktop/study/bookmanager:/opt/pycharm-2016.3.1/plugins/python/helpers/pycharm_matplotlib_backend:/opt/pycharm-2016.3.1/plugins/python/helpers/pycharm_display',
      'PATH': '/home/python/.virtualenvs/bookmanager/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin',
      'XDG_CURRENT_DESKTOP': 'Unity',
      'wsgi.run_once': False,
      'GDMSESSION': 'ubuntu',
      'LOGNAME': 'python',
      'SERVER_SOFTWARE': 'WSGIServer/0.2',
      'QT_LINUX_ACCESSIBILITY_ALWAYS_ON': '1',
      'MANDATORY_PATH': '/usr/share/gconf/ubuntu.mandatory.path',
      'GATEWAY_INTERFACE': 'CGI/1.1',
      'wsgi.input': <_io.BufferedReader name=6>,
      'TZ': 'Asia/Shanghai',
      'UPSTART_SESSION': 'unix:abstract=/com/ubuntu/upstart-session/1000/6818',
      'VIRTUAL_ENV': '/home/python/.virtualenvs/bookmanager',
      'PYTHONIOENCODING': 'UTF-8',
      'OLDPWD': '/opt/pycharm-2016.3.1/bin',
      'SESSION': 'ubuntu',
      'USER': 'python',
      'XDG_CONFIG_DIRS': '/etc/xdg/xdg-ubuntu:/usr/share/upstart/xdg:/etc/xdg',
      'XDG_SESSION_ID': 'c2',
      'HTTP_HOST': '127.0.0.1:8000',
      'HTTP_ACCEPT_LANGUAGE': 'zh-CN,zh;q=0.8',
      'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
      'HTTP_USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
      'LC_PAPER': 'zh_CN.UTF-8',
      'CONTENT_TYPE': 'text/plain',
      'REMOTE_ADDR': '127.0.0.1',
      'DESKTOP_SESSION': 'ubuntu',
      'DEFAULTS_PATH': '/usr/share/gconf/ubuntu.default.path',
      'XDG_VTNR': '7',
      'PS1': '(bookmanager) ',
      'GNOME_KEYRING_CONTROL': '',
      'LC_TIME': 'zh_CN.UTF-8',
      'SHELL': '/bin/bash',
      'HTTP_CONNECTION': 'keep-alive',
      'GTK_IM_MODULE': 'fcitx',
      'GIO_LAUNCHED_DESKTOP_FILE_PID': '15793',
      'INSTANCE': '',
      'GTK_MODULES': 'gail:atk-bridge:unity-gtk-module',
      'XDG_SESSION_DESKTOP': 'ubuntu',
      'LANG': 'zh_CN.UTF-8',
      'REMOTE_HOST': '',
      'LC_MEASUREMENT': 'zh_CN.UTF-8',
      'SESSIONTYPE': 'gnome-session',
      'XDG_RUNTIME_DIR': '/run/user/1000',
      'XDG_SESSION_PATH': '/org/freedesktop/DisplayManager/Session0',
      'QT_IM_MODULE': 'fcitx',
      'COMPIZ_CONFIG_PROFILE': 'ubuntu',
      'wsgi.errors': <_io.TextIOWrapper name='<stderr>' mode='w' encoding='UTF-8'>,
      'SSH_AUTH_SOCK': '/run/user/1000/keyring/ssh',
      'UPSTART_INSTANCE': '', 'HOME': '/home/python',
      'XDG_GREETER_DATA_DIR': '/var/lib/lightdm-data/python',
      'SERVER_PROTOCOL': 'HTTP/1.1',
      'wsgi.url_scheme': 'http',
      'QT_QPA_PLATFORMTHEME': 'appmenu-qt5',
      'XDG_SEAT_PATH': '/org/freedesktop/DisplayManager/Seat0',
      'SERVER_PORT': '8000',
      'HTTP_COOKIE': 'sessionid=syiojsuh9cet038d9flkh6l36v2cl23e; csrftoken=PhOfTEDrLAQzodU5xywK2e3jilhWE9eByif9k7smPxH9zwymUwxztBBQOx7yNqwJ',
      'GNOME_DESKTOP_SESSION_ID': 'this-is-deprecated',
      'LC_MONETARY': 'zh_CN.UTF-8',
      'GPG_AGENT_INFO': '/home/python/.gnupg/S.gpg-agent:0:1',
      'GIO_LAUNCHED_DESKTOP_FILE': '/usr/share/applications/jetbrains-pycharm.desktop',
      'HTTP_UPGRADE_INSECURE_REQUESTS': '1',
      'GDM_LANG': 'zh_CN',
      'QT_ACCESSIBILITY': '1',
      'UPSTART_EVENTS': 'xsession started'
    }
    """
    # print(request.META["CONTENT_TYPE"])
    # text/plain

    return HttpResponse('detail')

#######################Cookies####################################
"""
保存在客户端的数据叫做 cookie
cookie是保存在客户端的
cookie是基于域名(IP)的
    0.概念
    1.流程(原理)
        第一次请求过程
            1.我们的浏览器第一次请求服务器的时候，不会携带任何cookie信息
            2.服务器接收到请求以后，没有接收到cookie信息
            3.服务器设置一个cookie信息，cookie信息设置在相应的响应中
            4.浏览器接收到这个响应之后，会发现响应中有Cookie信息，name=itcast 浏览器会将cookie信息保存在浏览器中
        第二次及其之后的请求过程
            5.浏览器第二次及其之后的请求都会携带cookie信息
            6.服务器接收到请求之后，会发现携带的cookie信息 name=itcast 这样服务器就认识是谁的请求了
    2.看效果
    3.从http协议角度深入掌握Cookie的流程(原理)

"""
def set_cookie(request):
    # 1.先判断有没有cookie信息
    #   先假设没有

    # 2.获取用户名
    username = request.GET.get('username')
    # 3.因为我们讲舍没有cookie信息，我们服务器就要设置cookie信息
    response = HttpResponse('set_cookie')
    response.set_cookie('username',username)
    return response

def get_cookie(request):
    # 1.服务器可以接收(查看)cookie信息 cookie信息就是一个字典
    cookies = request.COOKIES
    username = cookies.get('username')
    # 2.得到用户信息就可以继续其他的业务逻辑了
    return HttpResponse('get_cookie')



#######################Cookies####################################

"""
    问题1：我换了浏览器，还能获取到session信息吗？ 不可以
    问题2：我不换浏览器，删除sessionid，则获取不到session信息
    问题3：再去执行 set_session的时候，会重新生成sessionid
    
保存在服务器的数据叫做 session
    session需要依赖于cookie
    
    如果浏览器禁用了cookie，则session不能实现
    
    0.概念
    1.流程
        第一次请求：
            ① 我们第一次请求的时候可以携带一些信息(用户名/密码) cookie中没有任何信息
            ② 当我们的服务器接收到这个请求之后，进行用户名和密码的验证，验证没有问题可以设置session信息
            ③ 在设置session信息的同事，服务器会在响应头中设置一个 sessionid的cookie信息
            ④ 客户端(浏览器)在接收到响应之后，会将cookie信息保存起来(保存sessionid的信息)
            
        第二次及其之后的请求：
            ⑤ 第二次及其之后的请求都会携带sessionid信息
            ⑥ 当服务器接收到请求之后，会获取到sessionid信息，然后进行验证，验证成功，则可以获取session信息(session信息保存在服务器端)
    2.效果
      第一次请求：
        ① 第一次请求，在请求头中没有携带任何cookie信息
        ② 我们在设置session的时候，session会做量将是
            第一件：将数据保存在数据库中
            第二件：设置一个cookie信息，这个cookie信息是以sessionid为key value为xxx
            cookie肯定会以响应的形式在响应头中出现
            
      第二次及其之后的请求：
        ③ 都会携带cookie信息，特别是sessionid 
    3.从原理(http)角度

"""

def set_session(request):
    # 1.cookie中没有任何信息
    print(request.COOKIES)
    # 2.对用户名和密码进行验证 假设认为用户名和密码正确
    user_id = 666
    # 3.设置session信息
    # request.session 理解为字典
    # 设置session的时候其实做了两件事
        # 1.将数据保存在数据库中
        # 2.设置一个cookie信息，这个cookie信息是以sessionid为key
    request.session['user_id'] = user_id

    # 4.返回响应
    return HttpResponse('set_session')


def get_session(request):
    # 1.请求会携带sessionid信息
    print(request.COOKIES)

    # 2.会获取到sessionid信息，然后进行验证 验证成功就可以获取session信息
    # request.session 字典
    user_id = request.session['user_id']
    user_id = request.session.get('user_id')

    # 3.返回响应
    return HttpResponse('get_session')