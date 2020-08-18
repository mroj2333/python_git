"""
Django settings for bookmanager project.

Generated by 'django-admin startproject' using Django 1.11.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# __file__ 表示文件的名字
# settings.py

# os.path.abspath(__file__)  abspath是据对路径
# /home/python/Desktop/study/bookmanager/bookmanager/settings.py

# os.path.dirname(os.path.abspath(__file__))
# /home/python/Desktop/study/bookmanager/bookmanager

# os.path.dirname(os.path.dirname(os.path.abspath(__file__))
# /home/python/Desktop/study/bookmanager


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h2=u_&yr0wj62p#8jm@_7g=-0owxg-zww*4q%aa34n5f%1m7ay'

# SECURITY WARNING: don't run with debug turned on in production!
# 开发者进行调试用的
DEBUG = True
# 当我们部署上线的时间要设置为False
# DEBUG = False
# ALLOWED_HOSTS 允许以哪个主机的形式访问后端
#　默认是127.0.0.1
# 如果你改变了允许的方式，需要将运行的ip/域名加进列表
# 默认的127需要自己添加才可以再次访问 python manage.py runserver 0:8000
# 安全机制 只能以罗列的来访问
ALLOWED_HOSTS = ['192.168.201.129',
                 '127.0.0.1',
                 ]


# Application definition
# 安装/注册 子应用
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 把创建的子应用添加进来
    # 子应用名.apps.子应用名Config
    'book.apps.BookConfig',
    'login.apps.LoginConfig',
    'pay.apps.PayConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ROOT_URLCONF 是我们工程url的配置入口
# 默认是 工程名.urls
# 可以修改，但是我们默认不修改
ROOT_URLCONF = 'bookmanager.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # DIRS 设置模板路径
        'DIRS': [os.path.join(BASE_DIR, 'template'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bookmanager.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# sqlite 主要是一个嵌入式的关系型数据库
# 主要是在移动端使用 sqlite属于小型的关系型数据库

# 中型的数据库：mysql(已经被甲骨文收购) sqlserver
# 大型的数据库：oracle DB2
DATABASES = {
    'default': {
        # ENGINE 引擎
        # 'ENGINE': 'django.db.backends.sqlite3',

        # MYSQL 'django.db.backends.mysql'
        'ENGINE': 'django.db.backends.mysql',
        'HOST' : '127.0.0.1',
        'PORT' : '3306',
        'USER' : 'root',
        'PASSWORD' : 'mysql',
        # 要使用的数据库的名称
        'NAME': 'book_42_01',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-Hans'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# django是如何区分动态资源和静态资源的呢？
# 就是通过STATIC_URL
# 我们在访问静态资源http://ip:port/ + STATIC_URL + 文件名
# django就会认识我们再访问静态资源，这时候会去静态文件夹(STATICFILES_DIRS)进行匹配
STATIC_URL = '/static/'

# 告知系统静态文件存放在哪里
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]