from django.shortcuts import render
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
    return render(request,'index.html',context)

"""
类似于 ipython的工具
python manager.py shell
"""


#########################新增数据#########################
""""
# 方式1
# 会把新生成的对象返回给我们
# 需要手动调用save()方法
book=BookInfo(
    name='python',
    pub_date='2000-01-01'
)
book.save()

# 方式2 直接入库
# objects模型的管理类，我们对模型的增删改查都找它

BookInfo.objects.create(
    name='java',
    pub_date='2010-01-01'
)
"""


#########################修改(更新)数据#########################
"""
# 方式1
# 1.查询数据
# select * from bookinfo where id=1;
book = BookInfo.objects.get(id=1)
# 2.直接修改实例的属性
book.readcount = 20
# 3.调用save方法
book.save()

# 方式2 直接更新
# filter()过滤
BookInfo.objects.filter(id=1).update(
    readcount=100,
    commentcount=200
)
"""


#########################删除数据#########################
""""# 方式1
# 1.先查询出数据
book = BookInfo.objects.get(id=5)
# 2.调用删除方法delete()
book.delete()

# 方式2
BookInfo.objects.filter(id=7).delete()
"""

#########################基本查询#########################
"""
# get 得到某一个数据
# all 获取所有
# count 个数

# 返回一个对象 不存在的数据将会产生异常
"book.models.DoesNotExist: BookInfo matching query does not exist."
book = BookInfo.objects.get(id=1)
try:
    book = BookInfo.objects.get(id=100)
except BookInfo.DoesNotExist:
    pass

# all返回一个列表 get得到的是一个单一对象
BookInfo.objects.all()

BookInfo.objects.all().count()
BookInfo.objects.count()
"""


#########################filter\get\exclude查询#########################
"""
select  from bookinfo where 条件语句
相当于where查询
filter ：过滤出多个结果
get ：返回一个结果
exclude ： 排除掉符合条件剩下的结果 相当于not
语法形式：
    以 filter(字段名_运算符=值) 为例

# 查询编号为1的图书
# exact 精确的 准确的 就是等于
BookInfo.objects.get(id__exact=1)
BookInfo.objects.get(id=1)

# get返回的是一个单一对象 filter返回的是一个列表

BookInfo.objects.filter(id=1)


# 查询书名包含'湖'的图书
# contains 就是包含的意思
BookInfo.objects.filter(name__contains='湖')


# 查询书名以'部'结尾的图书
BookInfo.objects.filter(name__endswith='部')


# 查询书名为空的图书
BookInfo.objects.filter(name__isnull=True)


# 查询编号为1或3或5的图书
BookInfo.objects.filter(id__in=[1, 3, 5])


# 查询编号大于3的图书
# gt 大于 great 大
# gte 大于等于 e equal
# lt 小于 less than
# lte 小于等于
BookInfo.objects.filter(id__gt=3)


# 查询书籍id不为3的图书
BookInfo.objects.exclude(id=3)


# 查询1980年发表的图书
BookInfo.objects.filter(pub_date__year=1980)


# 查询1990年1月1日后发表的图书
BookInfo.objects.filter(pub_date__gte='1990-01-01')
# 错误的查询
BookInfo.objects.filter(pub_date__gte='1990.01.01')
"""



#########################F对象#########################
# 两个属性的比较：F对象
"""
F对象的语法形式
filter(字段名__运算符=F('字段名'))
"""
from django.db.models import F
BookInfo.objects.filter(readcount__gte=F('commentcount'))

# 查询阅读量大于评论量两倍的图书
BookInfo.objects.filter(readcount__gte=F('commentcount')*2)


#########################Q对象(了解)#########################
"""
# 需要查询id大于2 并且阅读量大于20的书籍

# 方式1
# filter().filter()
BookInfo.objects.filter(id__gt=2).filter(readcount__gt=20)

# 方式2
# filter(条件, 条件)
BookInfo.objects.filter(id__gt=2, readcount__gt=20)


# 需要查询id大于2 或者阅读量大于20的书籍
from django.db.models import Q

# Q(字段名__运算符=值)
# 或 Q()|Q() ..
# 并且 Q()&Q() ..
# ~notQ()

BookInfo.objects.filter(Q(id=2)|Q(readcount__gt=40))

# 查询书籍id不为3
BookInfo.objects.exclude(id=3)
BookInfo.objects.filter(~Q(id=3))
"""


#########################聚合函数(了解)#########################
"""
# sum,max,min,avg,count
# 聚合函数需要使用 aggregate
# 语法形式是：aggregate(聚合函数('字段'))

# 当前书籍的阅读总量
from django.db.models import Sum,Max,Min,Count,Avg
BookInfo.objects.aggregate(Sum('readcount'))
"""



#########################排序#########################
"""
# order_by 默认升序
BookInfo.objects.all().order_by('readcount')
# 降序
BookInfo.objects.all().order_by('-readcount')
"""



#########################关联查询#########################
"""
# 书籍和人物的关系是一对多
# 书籍 中没有任何关于人物的字段
# 人物 中有关于书籍的字段 book 外键


# 语法形式：
#   通过书籍查询人物信息(已知 主表数据，关联查询从表数据)
#   主表模型.关联模型_set.all() 注：关联模型名称小写

#   通过人物查询书籍信息(已知 从表数据，关联查询主表数据)
#   从表模型.实例对象.外键

# 查询书籍为1的所有人物信息
# 通过书籍查询人物
# 1.查询书籍
book = BookInfo.objects.get(id=1)
# 2.根据书籍查询关联人物信息
book.peopleinfo_set.all()


# 查询人物为1的书籍信息
# 根据人物查询书籍
# 1.查询人物
person = PeopleInfo.objects.get(id=1)
# 2.根据人物查询书籍
# person.book 是一个实例对象
person.book.name
"""

"""
关联过滤查询
语法： 关联模型类名小写__属性名__条件运算符=值
# 查询图书，要求图书人物为“郭靖”

BookInfo.objects.filter(peopleinfo__name='郭靖')

# 查询图书，要求书中人物的描述包含“八”
BookInfo.objects.filter(peopleinfo__description__contains='八')

# 查询书名为“天龙八部”的所有人物
PeopleInfo.objects.filter(book__name='天龙八部')

# 查询图书阅读量大于50的所有人物
PeopleInfo.objects.filter(book__readcount__gt=50)
"""



#########################查询集(QuerySet)#########################
"""
# all() : 返回所有数据
# filter() : 返回满足条件的数据
# exclude() : 返回满足条件之外的数据
# order_by() : 对结果进行排序

# 查询结果集的两大特性：惰性执行、缓存
# 惰性执行：不调用的时间不会执行查询操作
# 缓存：
# 无缓存查询
[book.id for book in BookInfo.objects.all()]

#带缓存的查询
books = BookInfo.objects.all()
[book.id for book in books]


# 切片不支持负数
books = BookInfo.objects.all()[0:2]

# 
"""