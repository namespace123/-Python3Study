# name = input()
# print(name)

# # 高阶函数
# def add(a, b, f):
#     return f(a, 2) + f(b, 2)
# print(add(1, 2, pow))

# def f(x):
#     return x * x
# print(list(map(f, [1, 2, 3, 4])))
# print(list(map(str, [1, 2, 3, 4])))

# 递归运算
# from functools import reduce
# def add(a, b):
#     return a + b
# print(reduce(add, [1, 2, 3, 4, 5, 6]))
# def add2(a, b):
#     return 10 * a + b
# print(reduce(add2, [1, 2, 3, 4, 5, 6]))
#
# def char2num(s):
#     return {'0': 0,'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
#
# def str2int(s):
#     return reduce(lambda x, y: x * 10 + y, map(char2num, s))
# print(str2int('123'))

# def normalize(name):
#     return str(name[0]).upper() + str(name[1:]).lower()
# L1 = ['adam', 'sophia', 'LISA']
# L2 = list(map(normalize, L1))
# print(L2)

# from functools import reduce
# def sum(list):
#     return reduce(lambda x, y: x + y, list)
# def prod(list):
#     return reduce(lambda x, y: x * y, list)
# l = [1, 2, 3, 4]
# print('求和：', sum(l))
# print('求积：', prod(l))

# from functools import reduce
# def str2float(s):
#     a = s.split('.')[0]
#     b = (s.split('.')[1])
#     b = b[0: b.rindex('0')]
#     c = a + b
#     aa = reduce(lambda x, y: 10 * x + y, list(map(int, c)))
#     return float(aa) / pow(10, len(b))
# print('123.456 = ', str2float('123.405060'))

# def is_odd(n):
#     return n % 2 == 1
# l = [1, 2, 3, 4, 5, 6, 7]
# print(list(filter(is_odd, l)))
#
# def not_empty(n):
#     return n and str(n).strip()
# l = ['111123', 2, '  ', 4, '', None]
# print(l)
# print(list(filter(not_empty, l)))

# def foo(num):
#     print("starting...")
#     while num < 10:
#         num = num + 1
#         yield num
# for n in foo(0):
#     print(n)

# 生成素数
# def _odd_iter():
#     n = 1
#     while True:
#         n = n + 2
#         yield n
#
#
# def _not_divisible(n):
#     return lambda x: x % n > 0
#
#
# def primes():
#     yield 2
#     it = _odd_iter()
#     while True:
#         n = next(it)
#         yield n
#         it = filter(_not_divisible(n), it)
#
#
# for n in primes():
#     if n < 100:
#         print(n)
#     else:
#         break

# 过滤出回数
# def is_palindrome(n):
#     if list(reversed(str(n))) == list(str(n)):
#         return True
#     else:
#         return False
#
# print(list(filter(is_palindrome, range(11, 500))))

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# def by_name(t):
#     return t[0].lower()
# def by_score(t):
#     return t[1]
# print(sorted(L, key=by_name))
# print(sorted(L, key=by_score, reverse=True))

# def lazy_sum(*args):
#     def sum():
#         ax = 0
#         for n in args:
#             ax = ax + n
#         return ax
#     return sum
# f = lazy_sum(1, 3, 5, 7, 9)
# print(f)
# print(f())

# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#             return i * i
#         fs.append(f)
#     return fs
# f1, f2, f3 = count()
# print(f1())
# print(f2())
# print(f3())

# def count():
#     def f(j):
#         def g():
#             return j * j
#         return g
#     fs = []
#     for i in range(1, 4):
#         fs.append(f(i))
#     return fs
# f1, f2, f3 = count()
# print(f1())
# print(f2())
# print(f3())

# 匿名函数
# print(list(map(lambda x: x * x, (1, 2, 3))))
# def f(x):
#     return x * x
# f = lambda x: x * x
# print(f)

# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
# @log
# def now():
#     print('2019-03-13')
# print(now())

# def fun(a, **l):
#     print(a)
#     print(l)
# fun(1, c=1, b=2)

# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('%s %s(): ' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator
#
# @log('execute')
# def now():
#     print('2019-03-14')
# print(now())
# # 此处 now的__name__变成了wrapper
# print(now.__name__)

# # 不带参
# import functools
# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper

# 带参
# import functools
# def log(text):
#     def decarator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s(): ' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decarator
# @log('execute')
# def now():
#     print('2019-03-14')
# print(now())
# # 此处 now的__name__变成了wrapper
# print(now.__name__)

# 同时支持传参或者不传参的装饰器
# import functools
# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             if isinstance(text, str):
#                 print("begin call: %s %s" % (text, func.__name__))
#                 func(*args, **kwargs)
#                 print("end call: %s %s" % (text, func.__name__))
#             else:
#                 print("begin call: %s" % (func.__name__))
#                 func(*args, **kwargs)
#                 print("end call: %s" % (func.__name__))
#             return
#         return wrapper
#     if callable(text):
#         return decorator(text)
#     else:
#         return decorator
#
# @log
# def f():
#     print("action1")
# @log('execute')
# def f2():
#     print("action2")
# print(f())
# print(f2())

# 偏函数
# import functools
# int2 = functools.partial(int, base=2)
# print(int2('1000000'))
# print(int2('1000000', base=10))
# kw = {'base': 2}
# print(int('10010', **kw))
# max2 = functools.partial(max, 10)
# # 相当于args = (10, 5, 6, 7) 将10作为最左边的参数
# print(max2(5, 6, 7))

# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# ' a test module '
# __author__ = 'Sophia'
# import sys
# def test():
#     args = sys.argv
#     if len(args) == 1:
#         print("hello world, %s" % args[0])
#     elif len(args) == 2:
#         print('hello, %s' % args[1])
#     else:
#         print('too many le')
# if __name__ == '__main__':
#     test()

# 非公开函数
# def _private_1(name):
#     return 'Hello, %s' % name
# def _private_2(name):
#     return 'Hi, %s' % name
# def greeting(name):
#     if len(name) > 3:
#         return _private_1(name)
#     else:
#         return _private_2(name)
# print(greeting("sophia"))
# print(greeting("wrd"))

# 图像处理 - 生成缩略图
# from PIL import Image
# im = Image.open('C:\\Users\\xk\\Desktop\\桌面\\1.jpg')
# print(im.format, im.size, im.mode)
# im.thumbnail((200, 100))
# im.save('thumb.jpg', 'JPEG')

# # 模块搜索路径
# import sys
# print(sys.path)
# # 运行时修改，运行后失效，永久有效可设置环境变量PATHONPATH
# sys.path.append('lalala')

# class Student(object):
#     pass
# bart = Student()
# print(bart)

# class Student(object):
#
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def print_score(self):
#         print('%s %s' % (self.name, self.score))
#
# bart = Student('Bart Simpson', 59)
# lisa = Student('Lisa', 87)
# bart.print_score()
# lisa.print_score()
# print(bart)
# print(lisa)
# bart.name = 'sophia'
# bart.print_score()
# lisa.age = 8
# print(lisa.age)

# class Student(object):
#
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
#
#     def print_score(self):
#         print('%s: %s' % (self.__name, self.__score))
#
#     def get_name(self):
#         return self.__name
#
#     def get_score(self):
#         return self.__score
#
# bart = Student('Bart', 98)
# # 加了__的变量不可以直接访问了
# # print(bart.__name)
# bart.print_score()
# bart.age = 8
# print(bart.age)
# bart.__name = 'sophia'
# bart.print_score()
# # 这里的 bart.__name 并不是对象里的那个name值
# print(bart.__name)
# print(bart.get_name())

# 继承(这里的 Animal 是 Dog 和 Cat 类的父类)
# class Animal(object):
#     def run(self):
#         print('Animal is running ...')
#
#
# class Dog(Animal):
#     def run(self):
#         print('Dog is running ...')
#
#     def eat(self):
#         print('Eating meat ...')
#
#
# class Cat(Animal):
#     pass
#
#
# dog = Dog()
# dog.run()
# cat = Cat()
# cat.run()
#
# # 多态
# a = list()
# b = Animal()
# c = Dog()
# print(isinstance(a, list))
# print(isinstance(b, Animal))
# print(isinstance(b, Dog))
# print(isinstance(c, Dog))
# print(isinstance(c, Animal))
#
# def run_twice(animal):
#     animal.run()
#     animal.run()
#
# # 多态的好处展露无遗
# run_twice(Animal())
# run_twice(Dog())

# print(type(123))
# print(type('str'))
# print(type(None))
# print(type(abs))
# print(type(123) == type(456))
# print(type(123) == int)
# print(type('abc') == type(123))
#
# import types
# def fn():
#     pass
#
# print(type(fn) == types.FunctionType)
# print(type(abs) == types.BuiltinFunctionType)
# print(type(lambda x: x) == types.LambdaType)
# print(type(x for x in range(10)) == types.GeneratorType)

# print(isinstance('a', str))
# print(isinstance(123, int))
# print(isinstance(b'a', bytes))
# # 同时判断是不是属于其中一个
# print(isinstance([1, 2, 3], (list, tuple)))
# print(isinstance((1, 2, 3), (list, tuple)))

# print(dir('ABC'))

# class MyObject(object):
#     def __init__(self):
#         self.x = 9
#
#     def power(self):
#         return self.x * self.x
# obj = MyObject()
# print(hasattr(obj, 'x'))
# print(hasattr(obj, 'y'))
# obj.y = 'lalala'
# print(hasattr(obj, 'y'))
# print(getattr(obj, 'x'))
# setattr(obj, 'z', 10)
# print(getattr(obj, 'z'))
# # print(getattr(obj, 'a'))
# print(hasattr(obj, 'power'))
# print(getattr(obj, 'power'))
# fn = getattr(obj, 'power')
# obj.x = 10
# print(fn())

# class Student(object):
#     name = 'Student'
# s = Student()
# print(s.name)
# print(Student.name)
# s.name = 'Sophia'
# print(s.name)
# print(Student.name)
# del s.name
# print(s.name)

# python可以动态绑定属性
# class Student(object):
#     pass
# s = Student()
# s.name = 'Sophia'
# print(s.name)
# # 绑定方法
# def set_age(self, age):
#     self.age = age
#
# from types import MethodType
# s.set_age = MethodType(set_age, s)
# s.set_age(25)
# print(s.age)
#
# def set_score(self, score):
#     self.score = score
#
# Student.set_score = MethodType(set_score, Student)
# s.set_score(100)
# print(s.score)

# __slots__ 来限制动态添加的属性，但是对继承的子类不起作用，只对当前类起作用
# 如果子类也定义了__slots__,则默认允许定义的属性是自身的slots加上父类的slots
# class Student(object):
#     __slots__ = ('name', 'age')
#
# s = Student()
# s.name = 'Sophia'
# s.age = 25
# # s.score  = 99
#
# class GraduateStudent(Student):
#     __slots__ = ('name')
# g = GraduateStudent
# g.age = 9999

# class Student(object):
#
#     def get_score(self):
#         return self.score
#
#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('Score must be integer!')
#         if value < 0 or value > 100:
#             raise ValueError('Score must between 0 - 100!')
#         self.score = value
#
# s = Student()
# s.set_score(60)
# print(s.get_score())
# # s.set_score(9999)

# class Student(object):
#     # 定义 getter
#     @property
#     def score(self):
#         return self._score
#
#     # 定义 setter
#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('Score must be integer!')
#         if value < 0 or value > 100:
#             raise ValueError('Score must between 0 - 100!')
#         self._score = value
#
#     # 可以只定义 getter 方法
#     @property
#     def total_score(self):
#         return self._score * 3
#
#
# s = Student()
# s.score = 60  # 实际就是 s.set_score(60)
# print(s.score)  # 实际就是 s.get_score()
# # s.score = 900

# class Screen(object):
#     @property
#     def width(self):
#         return self._width
#     @property
#     def height(self):
#         return self._height
#     @width.setter
#     def width(self, width):
#         self._width = width
#     @height.setter
#     def height(self, height):
#         self._height = height
#     @property
#     def resolution(self):
#         return self._height * self._width
#
# s = Screen()
# s.width = 1024
# s.height = 768
# print(s.resolution)
# # assert 断言
# assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution

# class Animal(object):
#     pass
#
#
# class Mammal(Animal):
#     pass
#
#
# class Bird(Animal):
#     pass
#
#
# class RunnableMixIn(object):
#     def run(self):
#         print("I am running ...")
#
#
# class FlyableMixIn(object):
#     def fly(self):
#         print('I am flying ...')
#
#
# class Dog(Mammal, RunnableMixIn):
#     pass
#
#
# # 蝙蝠
# class Bat(Mammal, FlyableMixIn):
#     pass
#
#
# # 鹦鹉
# class Parrot(Bird, FlyableMixIn):
#     pass
#
#
# # 鸵鸟
# class Ostrich(Bird, RunnableMixIn):
#     pass

# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return 'Student object (name: %s) ' % self.name
#     __repr__ = __str__
#
# s = Student('Sophia')
# print(s)

# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b
#         if self.a > 100:
#             raise StopIteration()
#         return self.a
#
#     def __getitem__(self, n):
#         if isinstance(n, int):
#             a, b = 1, 1
#             for x in range(n):
#                 a, b = b, a + b
#             return a
#         if isinstance(n, slice):
#             start = n.start
#             stop = n.stop
#             if start is None:
#                 start = 0
#             a, b = 1, 1
#             L = []
#             for x in range(stop):
#                 if x >= start:
#                     L.append(a)
#                 a, b = b, a + b
#             return L
#
#
# # for n in Fib():
# #     print(n)
#
# f = Fib()
# print(f[7])
# print(f[1:10])
# print(f[:10])

# class Student(object):
#     def __init__(self):
#         self.name = 'Sophia'
#     def __getattr__(self, attr):
#         if attr == 'score':
#             return 99
#         elif attr == 'age':
#             return lambda :25
#         else:
#             # return "不存在"
#             raise AttributeError("%s is not exist" % attr)
#
# s = Student()
# print(s.name)
# print(s.score)
# print(s.age())
# print(s.address)

# class Chain(object):
#     def __init__(self, path=''):
#         self._path = path
#
#     def __getattr__(self, path):
#         return Chain('%s/%s' % (self._path, path))
#
#     def __str__(self):
#         return self._path
#
#     __repr__ = __str__
#
#
# print(Chain().status.user.timeline.list)

# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __call__(self):
#         print('My name is %s.' % self.name)
#
# s = Student('Sophia')
# s()
# # 判断一个对象是否可调用
# print(callable(s))
# print(callable(max))
# print(callable([1, 2, 3]))
# print(callable(None))
# print(callable('str'))
# print(max(1, 2, 3))
# print(callable(str))

# from enum import Enum
# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#
# for name, member in Month.__members__.items():
#     # value 默认从 1 开始
#     print(name, "->", member, ',', member.value)

# from enum import Enum, unique
# # unique装饰器保证没有重复值
# @unique
# class Weekday(Enum):
#     Sun = 0
#     Mon = 1
#     Tue = 2
#     Thu = 4
#     Fri = 5
#     Sat = 6
#
# print(Weekday.Mon)
# print(Weekday['Tue'])
# print(Weekday.Tue.value)
# print(Weekday(1))
# for name, member in Weekday.__members__.items():
#     print(name, "->", member, ",", member.value)

# from hello import Hello
# h = Hello()
# h.hello()
# # class的类型是type
# print(type(Hello))
# print(type(h))

# def fn(self, name='world'):
#     print('hello,', name)
#
# # 运用type动态创建类
# Hello = type('Hello', (object,), dict(hello=fn))
# h = Hello()
# h.hello()
# print(type(Hello))
# print(type(h))

# class ListMetaclass(type):
#     def __new__(cls, name, bases, attrs):
#         attrs['add'] = lambda self, value: self.append(value)
#         return type.__new__(cls, name, bases, attrs)
#
# class MyList(list, metaclass=ListMetaclass):
#     pass
#
# L = MyList()
# L.add(1)
# print(L)


# ORM 框架
# class ModelMetaclass(type):
#     def __new__(cls, name, bases, attrs):
#         if name == 'Model':
#             return type.__new__(cls, name, bases, attrs)
#         print('Found model: %s' % name)
#         mappings = dict()
#         for k, v in attrs.items():
#             if isinstance(v, Field):
#                 print('Found mapping: %s ==> %s' % (k, v))
#                 mappings[k] = v
#         for k in mappings.keys():
#             attrs.pop(k)
#         attrs['__mappings__'] = mappings
#         attrs['__table__'] = name
#         return type.__new__(cls, name, bases, attrs)
#
# class Model(dict, metaclass=ModelMetaclass):
#     def __init__(self, **kw):
#         super(Model, self).__init__(**kw)
#
#     def __getattr__(self, key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(r"'Model' object has no attribute '%s'" % key)
#
#     def __setattr__(self, key, value):
#         self[key] = value
#
#     def save(self):
#         fields = []
#         params = []
#         args = []
#         for k, v in self.__mappings__.items():
#             fields.append(v.name)
#             params.append('?')
#             args.append(getattr(self, k, None))
#         sql = 'insert into %s (%s) values (%s)' % (self.__table__, ",".join(fields), ','.join(params))
#         print('SQL: %s' % sql)
#         print('ARGS: %s' % str(args))
#
# class Field(object):
#     def __init__(self, name, column_type):
#         self.name = name
#         self.column_type = column_type
#
#     def __str__(self):
#         return '<%s:%s>' % (self.__class__.__name__, self.name)
#
# class StringField(Field):
#     def __init__(self, name):
#         super(StringField, self).__init__(name, 'varchar(100)')
#
# class IntegerField(Field):
#     def __init__(self, name):
#         # super(IntegerField, self).__init__(name, 'bigint')
#         Field.__init__(self, name, 'bigint')
#
# class User(Model):
#     # 定义类的属性到列的映射
#     id = IntegerField('id')
#     name = StringField('username')
#     email = StringField('email')
#     password = StringField('password')
#
# # 创建一个实例
# u = User(id=12345, name='Sophia', email='test@qq.com', password='my-pwd')
# # 保存到数据库
# u.save()

# 所有的错误类型都继承自 BaseException
# try:
#     print('try ...')
#     # r = 10 / 0
#     # r = 10 / int('a')
#     r = 10 / 5
#     print('result: ', r)
# except ZeroDivisionError as e:
#     print('except: ', e)
# except ValueError as e:
#     print('ValueError: ', e)
# except UnicodeError as e:  # 这里UnicodeError是ValueError的子类，放在ValueError的后面是无效的
#     print('Unicode: ', e)
# else:
#     print('no Error!')
# finally:
#     print('finally ...')
# print('END')

# import logging
#
# def foo(s):
#     return 10 / int(s)
#
# def bar(s):
#     return foo(s) * 2
#
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)
#
# main()
# print('END')

# class FooError(ValueError):
#     pass
# def foo(s):
#     n = int(s)
#     if n == 0:
#         raise FooError('invalid value: %s' % s)
#     return 10 / n
# foo('0')

# def foo(s):
#     n = int(s)
#     if n == 0:
#         raise ValueError('invalid value: %s' % s)
#     return 10 / n
#
# def bar():
#     try:
#         foo('0')
#     except ValueError as e:
#         # 如果不知道如何处理，就继续往上抛
#         print('ValueError!')
#         raise
#
#     try:
#         10 / 0
#     # 还可以把一种类型的错误转换成另一种类型错误抛出
#     except ZeroDivisionError:
#         raise ValueError('input error!')
#
# bar()

# import logging
# import pdb
# logging.basicConfig(level=logging.DEBUG)
# def foo(s):
#     n = int(s)
#     logging.debug("参数不能为0")
#     logging.info("参数不能为0")
#     pdb.set_trace()
#     logging.warning("参数不能为0")
#     logging.error("参数不能为0")
#     # assert可以用 -0 来关闭：python3 -0 err.py
#     assert n != 0, 'n is zero!'
#     return 10 / n
# def main():
#     foo('0')
# main()


# class Dict(dict):
#     def __getattr__(self, key):
#         try:
#          return self[key]
#         except KeyError:
#             raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
#     def __setattr__(self, key, value):
#         self[key] = value
#
# # d = Dict(a=1, b=2)
# # print(d['a'])
# # print(d.a)
#
# # 测试单元
# import unittest
# class TestDict(unittest.TestCase):
#
#     # 每个函数开始前都要执行的操作放在这里，简化代码
#     def setUp(self):
#         print("setUp ...")
#
#     # 每个函数结束时都要执行的操作放在这里，简化代码
#     def tearDown(self):
#         print("tearDown ...")
#
#     def test_init(self):
#         d = Dict(a=1, b='test')
#         self.assertEqual(d.a, 1)
#         self.assertEqual(d.b, 'test')
#         self.assertTrue(isinstance(d, dict))
#
#     def test_key(self):
#         d = Dict()
#         d['key'] = 'value'
#         self.assertEqual(d.key, 'value')
#
#     def test_attr(self):
#         d = Dict()
#         d.key = 'value'
#         self.assertTrue('key' in d)
#         self.assertEqual(d['key'], 'value')
#
#     def test_keyerror(self):
#         d = Dict()
#         with self.assertRaises(KeyError):
#             value = d['empty']
#
#     def test_attrerror(self):
#         d = Dict()
#         with self.assertRaises(AttributeError):
#             value = d.empty
#
# unittest.main()

# import re
# m = re.search('(?<=abc)def', 'abcdef')
# print(m.group(0))

# def fact(n):
#
#     '''
#     >>> fact(1)
#     0
#     >>> fact(0)
#     0
#     '''
#     if n % 2 == 0:
#         return 1
#     else:
#         return 0
#
# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()

# -*- coding: UTF-8 -*-

# try:
#     f = open('C:\\Users\\wenfeng\\Desktop\\111.txt', 'r', encoding='UTF-8')
#     print(f.read())
# finally:
#     if f:
#         f.close()
#
# # 与上面的内容等价
# with open('C:\\Users\\wenfeng\\Desktop\\111.txt', 'r', encoding='UTF-8') as f:
#     # print(f.read())
#     # print(f.read(10))
#     l = f.readlines()
#     # print(l)
#     # print(f.readline())
#     for line in f.readlines():
#         print(line.strip())
#
# f = open('C:\\Users\\wenfeng\\Desktop\\111.txt', 'r', encoding='UTF-8', errors='ignore')

# with open('C:\\Users\\wenfeng\\Desktop\\111.txt', 'w', encoding='UTF-8') as f:
#     f.write('Hello, world!')

# from io import StringIO
# f = StringIO()
# print(f.write('hello'))
# print(f.write(' '))
# f.write('world!')
# print(f.getvalue())

# from io import StringIO
# f = StringIO('Hello!\nHi!\nGoodbye!')
# while True:
#     s = f.readline()
#     if s == '':
#         break
#     print(s.strip())

# from io import BytesIO
# f = BytesIO()
# f.write('中文'.encode('utf-8'))
# print(f.getvalue())

# from io import BytesIO
# f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
# print(f.read())

# import os
# print(os.name)
# # 查看系统详细信息，windows不提供此功能
# # print(os.uname())
# # 查看环境变量
# print(os.environ)
# print(os.environ.get('classPath'))
# print(os.environ.get('x', 'default'))

# import os
# print(os.path.abspath("."))
# print(os.path.join(".", "test"))
# print(os.mkdir('test'))
# os.rmdir('test')
# print(os.path.split('/home/sophia/111.txt'))
# print(os.path.split('/home/sophia/111.txt')[0])
# # 获取扩展名
# print(os.path.splitext('/home/sophia/111.txt')[1])
# # os.rename('lalala.txt', 'hehehe.txt')
# os.remove('hehehe.txt')

# 创建文件
# with open('hehehe', 'w') as f:
#     f.write('hello\nworld')

# # 复制文件内容1
# with open('hehehe', 'r') as f:
#     with open('lalala', 'w') as f2:
#         for line in f.readlines():
#             f2.write(line)
#
# # 复制文件内容2
# import shutil
# shutil.copy('lalala', 'xixixi')

# import os
# print([x for x in os.listdir('.') if os.path.isdir(x)])
# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

# import os
# os.mkdir("test")
# with open('test/111.py', 'w'):
#     pass

# 递归遍历所有子文件，并打印相对路径
# import os
# def searchDir(refer_dir, dir):
#     for x in os.listdir(dir):
#         path = os.path.join(dir, x)
#         if os.path.isfile(path):
#             print(os.path.join(refer_dir, x))
#         else:
#             searchDir(os.path.join(refer_dir, x), path)
#
# searchDir("", os.path.abspath("."))

# 考虑到兼容问题，只用pickle保存不重要的数据，不能成功pickle也没有关系
# 序列化，即pickling
# import pickle
# d = dict(name='Bob', age=20, score=88)
# print(pickle.dumps(d))
# with open('dump.txt', 'wb') as f:
#     pickle.dump(d, f)
# # 反序列化
# with open('dump.txt', 'rb') as f:
#     d = pickle.load(f)
#
# print(d)

# import json
# d = dict(name='Bob', age=20, score=88)
# # json.dumps 返回的是一个标准的json字符串
# json_str = json.dumps(d)
# print(json_str)
# # 反序列化
# print(json.loads(json_str))

# 自定义类的序列化
# import json
#
# class Student(object):
#     def __init__(self, name, age, score):
#         self.name = name
#         self.age = age
#         self.score = score
#
# def student2dict(std):
#     return {
#         'name': std.name,
#         'age': std.age,
#         'score': std.score
#     }
#
# s = Student('Bob', 20, 88)
# print(json.dumps(s, default=student2dict))
# # 简化版，无需写序列化方法
# json_str = json.dumps(s, default=lambda obj: obj.__dict__)
#
# def dict2student(d):
#     return Student(d['name'], d['age'], d['score'])
# print(json.loads(json_str, object_hook=dict2student))

# 请在linux或者Mac下执行以下代码
# import os
# print('Process (%s) start ...' % os.getpid())
# pid = os.fork()
# # 子进程永远返回0，父进程返回子进程id
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I(%s) just created a child process (%s).' % (os.getpid(), pid))

# multiprocessing 弥补了windows没有fork的问题
# from multiprocessing import Process
# import os
# def run_proc(name):
#     print('Run child process %s (%s) ...' % (name, os.getpid()))
#
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test', ))
#     print('Child process will start.')
#     p.start()
#     p.join() # join 等待子进程结束后再继续往下运行，通常用于进程间的同步
#     print('Child process end.')

# 进程池批量创建子进程
# from multiprocessing import Pool
# import os, time, random
#
# def long_time_task(name):
#     print('Run task %s (%s) ...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     # 此处设置4 表示一次性只能允许同时运行4个进程，所以第五个进程最后才开始执行
#     # pool 默认大小是cpu核数
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i, ))
#     print('Waiting for all subprocesses done ...')
#     p.close()
#     # 等所有子进程执行完，join之前必须调用close，close之后不能再添加子进程
#     p.join()
#     print('All subprocesses done.')

# import subprocess
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code: ', r)

# import subprocess
# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE,
#                      stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('UTF-8'))
# print('Exit code: ', p.returncode)

# 进程间通信
# from multiprocessing import Process, Queue
# import os, time, random
# # 写数据进程执行的代码
# def write(q):
#     print('Process to write: %s' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('Put %s to queue ...' % value)
#         q.put(value)
#         time.sleep(random.random())
# # 读数据进程执行的代码
# def read(q):
#     print('Process to read: %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)
#
# if __name__=='__main__':
#     # 父进程创建 Queue，并传给各个子进程
#     q = Queue()
#     pw = Process(target=write, args=(q, ))
#     pr = Process(target=read, args=(q, ))
#     # 启动子进程pw，写入
#     pw.start()
#     # 启动子进程pr，读取
#     pr.start()
#     # 等待 pw 结束
#     pw.join()
#     # pr进程里是死循环，无法等待其结束， 只能强行终止
#     pr.terminate()

# 多线程(给线程命名仅用于打印，无其他意义)
# import time, threading
# def loop():
#     print('thread %s is running ...' % threading.current_thread().name)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('thread %s' % threading.current_thread().name, n)
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)
#
# print('thread %s is running ...' % threading.current_thread().name)
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('thread %s ended.' % threading.current_thread().name)

# import time, threading
# from multiprocessing import Pool
# balance = 0
# def change_it(n):
#     global balance
#     balance = balance + n
#     balance = balance - n
# def run_thread(n):
#     for j in range(100000):
#         change_it(n)
# if __name__ == '__main__':
#     p = Pool(4)
#     for i in range(64):
#         p.apply_async(run_thread, args=(i, ))
#     p.close()
#     p.join()
#     print(balance)
#
# balance = 0
# lock = threading.Lock()
# def run_thread(n):
#     for i in range(100000):
#         # 先获取锁
#         lock.acquire()
#         try:
#             # 放心地改
#             change_it(n)
#         finally:
#             # 改完一定要释放锁
#             lock.release()

# python 一个死循环程序
# import threading, multiprocessing
#
# def loop():
#     s = 0
#     while True:
#         s = s ^ 1
#
# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=loop())
#     t.start()

# ThreadLocal，在不使用全局变量的情况下，使每个函数都可以获得属于自己的对象
# 创建ThreadLocal对象
# local_school = threading.local()
# # def process_student():
# #     # 获取当前线程关联的student
# #     std = local_school.student
# #     print('Hello,', std, "in", threading.current_thread().name)
# #
# # def process_thread(name):
# #     # 绑定ThreadLocal的student
# #     local_school.student = name
# #     process_student()
# #
# # t1 = threading.Thread(target=process_thread, args=('Alice', ), name='Thread-A')
# # t2 = threading.Thread(target=process_thread, args=('Bob', ), name='Thread-B')
# # t1.start()
# # t2.start()
# # t1.join()
# # t2.join()

# 正则表达式
# import re
#
# s = r'ABC\-001'  # r表示不使用转义
# print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
# print(re.match('^\d{3}\\-\d{3,8}$', '010-12345'))
# print(re.match(r'^\d{3}\-\d{3,8}$', '01012345'))
# print(re.match(r'^\d{3}-\d{3,8}$', '010-12345'))
#
# # 切分字符串(拯救不规范)
# print('a b   c'.split(' '))
# print(re.split(r'\s+', 'a b    c'))
# print(re.split(r'[\s\,]+', 'a,b, c   d'))
# print(re.split(r'[\s\,\;]+', 'a,b;; c   d'))
#
# # 提取子串（分组）加括号表示定义组，然后以如下方式获取
# m = re.match(r'^(\d{3})-(\d{3,8})$', '010-123456')
# print(m)
# # group(0) 永远是原始字符串
# print(m.group(0))
# print(m.group(1))
# print(m.group(2))

# import re
#
# t = '19:05:30'
# m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
# print(m.group())
# print(m.group(0))
# print(m.groups())
# # 正则表达式默认贪婪匹配
# print(re.match(r'^(\d+)(0*)$', '102300').groups())
# # +后面加？就可以变为非贪婪匹配
# print(re.match(r'^(\d+?)(0*)$', '102300').groups())
#
# # 当某个正则表达式使用次数比较多，可以预编译好
# re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# # 使用
# print(re_telephone.match('010-12345').groups())
# print(re_telephone.match('010-8086').groups())

# 验证email
# import re
# re_email = re.compile(r'^<?(\w*\s*\w*)>?\s*([0-9a-zA-Z]+[.]?[0-9a-zA-Z]+)@([\w]+)[.]?([\w]+)$')
# print(re_email.match('2319175156@qq.com'))
# print(re_email.match('sophia@gmail.com'))
# print(re_email.match('bill.gates@microsoft.com'))
# print(re_email.match('<Tom Paris> tom@voyager.org'))
# print(re_email.match('<Tom Paris> tom@voyager.org').groups())
# print(re_email.match('<Tom Paris> tom@voyager.org').group(1))

# 常用内建设模块
# datetime是一个模块，它里面有一个datetime类
# from datetime import datetime
# now = datetime.now()
# print(now)
# print(type(now))
#
# # 获取指定时间和日期
# from datetime import datetime
# dt = datetime(2015, 4, 19, 12, 20)
# print(dt)
#
# # datetime 转换为 timestamp
# from datetime import datetime
# dt = datetime(2015, 4, 19, 12, 20)
# # timestamp是浮点数，单位是s，小数位部分表示ms
# print(dt.timestamp())
#
# # timestamp 转换为 datetime(默认与本地时间做转换)
# from datetime import datetime
# t = 1429417200.0
# print(datetime.fromtimestamp(t))
# # timestamp 转换为 UTC标准时区的时间
# print(datetime.utcfromtimestamp(t))
#
# # str 转 datetime
# cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
# print(cday)
#
# # datetime 转 str
# now = datetime.now()
# print(now.strftime('%a, %b %d %H:%M'))

# datetime加减
# from datetime import datetime, timedelta
# now = datetime.now()
# print(now)
# print(now + timedelta(hours=10))
# print(now - timedelta(minutes=12))
# print(now - timedelta(days=12))

# 本地时间转UTC时间
# from datetime import datetime, timedelta, timezone
# tz_utc_8 = timezone(timedelta(hours=8))
# now = datetime.now()
# print(now)
# dt = now.replace(tzinfo=tz_utc_8)
# print(dt)

# 时区转换
# 拿到UTC时间并强制设置时区为UTC+0:00
# utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
# print(utc_dt)
# bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
# print(bj_dt)
# tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
# print(tokyo_dt)
# tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
# print(tokyo_dt2)

# 练习
# import re
# from datetime import datetime, timezone, timedelta
# def to_timestamp(dt_str, tz_str):
#     dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
#     tz_r = re.match(r'UTC([+|-]?)(\d{1,2}):00$', tz_str)
#     if tz_r.group(1) == '-':
#         tz = timezone(timedelta(hours=-int(tz_r.group(2))))
#     else:
#         tz = timezone(timedelta(hours=int(tz_r.group(2))))
#     dt = dt.replace(tzinfo=tz)  # 默认为None，无法判断时区，现在强制设置时区
#     print(dt)
#     return dt.timestamp()
#
# t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
# assert t1 == 1433121030.0, t1
# t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
# assert t2 == 1433121030.0, t2
# print('pass')

# collections
# namedtuple('名称', [属性 list])
# from collections import namedtuple
# Point = namedtuple('Point', ['x', 'y'])
# p = Point(1, 2)
# print(p.x, p.y)
# print(isinstance(p, Point))
# Circle = namedtuple('Circle', ['x', 'y', 'r'])

# deque
# list 是线性存储，便于存储和访问，但插入、删除元素慢
# deque 是为了高效实现插入和删除操作的双向列表， 适用于队列和栈：
# from collections import deque
# q = deque(['a', 'b', 'c'])
# print(q)
# q.append('x')
# print(q)
# q.appendleft('y')
# print(q)
# q.pop()
# print(q)
# q.popleft()
# print(q)

# defaultdict
# 使用dict，如果key不存在就会抛出KeyError，如果希望key不存在时返回一个默认值们就是用defaultdict
# 除开这一点，defaultdict 与 dict 完全一样
# from collections import defaultdict
# dd = defaultdict(lambda : 'N/A')
# dd['key1'] = 'abc'
# print(dd['key1'])
# print(dd['key2'])

# OrderedDict
# dict是乱序的，OrderDict是有序的，按插入顺序排序
# from collections import OrderedDict
# d = dict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
# print(d)
# od = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
# print(od)
# od = OrderedDict()
# od['z'] = 1
# od['y'] = 2
# od['x'] = 3
# print(list(od.keys()))

# 利用 OrderedDict 实现先进先出队列
# from collections import OrderedDict
# class LastUpdatedOrderdDict(OrderedDict):
#     def __init__(self, capacity):
#         # super().__init__()
#         self._capacity = capacity
#
#     def __setitem__(self, key, value):
#         containsKey = 1 if key in self else 0
#         if len(self) - containsKey >= self._capacity:
#             last = self.popitem(last=False)
#             print('remove: ', last)
#         if containsKey:
#             del self[key]
#             print('set:', (key, value))
#         else:
#             print('add:', (key, value))
#         OrderedDict.__setitem__(self, key, value)
#
# luod = LastUpdatedOrderdDict(3)
# luod['x'] = 1
# print(luod)
# luod['y'] = 1
# print(luod)
# luod['z'] = 1
# print(luod)
# luod['a'] = 1
# print(luod)
# luod['y'] = 1
# print(luod)

# Counter 计数器
# from collections import Counter
# c = Counter()
# for ch in 'programming':
#     c[ch] = c[ch] + 1
# print(c)

# # base64编码
# import base64
# print(base64.b64encode(b'binary\x00string'))
# print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))# 316
# # url safe 方式是将字符 + / 分别变成 - _ 以适应浏览器需要
# print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
# print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
# print(base64.urlsafe_b64decode('abcd--__'))
# 写一个能处理掉 = 号的base64解码函数
# import base64
# def safe_base64_decode(s):
#     s2 = s.decode(encoding='utf-8')
#     n = len(s2) % 4
#     if n != 0:
#         for i in range(4-n):
#             s2 = s2 + '='
#         s = s2.encode(encoding='utf-8')
#     return base64.b64decode(s)
#
# assert b'abcd' == safe_base64_decode(b'YWJjZA=='), 'error'
# assert b'abcd' == safe_base64_decode(b'YWJjZA'), 'error'
# print('Pass')

# # 把32位无符号整数变成字节
# n = 10240099
# b1 = (n & 0xff000000) >> 24
# b2 = (n & 0xff0000) >> 16
# b3 = (n & 0xff00) >> 8
# b4 = n & 0xff
# bs = bytes([b1, b2, b3, b4])
# print(bs)
#
# # 把32位无符号整数变成字节(改良版)
# import struct
# # >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数
# print(struct.pack('>I', 10240099))
# # >IH 将后面的bytes依次变为 I: 4字节无符号整数 和 H: 2字节无符号整数
# print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))

# import struct
# s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
# print(struct.unpack('<ccIIIIIIHH', s))

# 编写程序判断一个图片是否是位图文件，如果是，打印出图片大小和颜色数
# import struct
# import base64
#
#
# def img2byte(filename):
#     with open(filename, 'rb') as f:
#         res = base64.b64encode(f.read(30))
#
#     return res
#
#
# def is_bm(bytes_data):
#     bytes_data = base64.b64decode(bytes_data)
#     info = struct.unpack('<ccIIIIIIHH', bytes_data)
#     this_type = bytes.decode(info[0] + info[1])
#     if type == 'BM':
#         print("该文件是位图文件")
#         print('该图片大小是 %d*%d, 颜色数是 %d' % (info[-4], info[-3], info[-1]))
#
#     else:
#         print("该文件不是位图文件")
#
# is_bm(img2byte('C:\\Users\\xk\\Desktop\\111.bmp'))

# 摘要算法 hashlib，生成唯一摘要，比如用于保存用户登录密码等
# MD5生成结果是固定的 128 bit 字节
# 通常用一个32位的16进制字符串表示
# import hashlib
# md5 = hashlib.md5()
# md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
# print(md5.hexdigest())
# md5 = hashlib.md5()
# md5.update('how to use'.encode('utf-8'))
# md5.update(' md5 in python hashlib?'.encode('utf-8'))
# print(md5.hexdigest())

# shal的结果是 160 bit 字节，通常用一个40位的16进制字符串表示
# 比SHA1更安全的算法有SHA256、SHA512，但是生成的更慢，长度更长
# import hashlib
# sha1 = hashlib.sha1()
# sha1.update('how to use sha1 in '.encode('utf-8'))
# sha1.update('python hashlib?'.encode('utf-8'))
# print(sha1.hexdigest())

# import hashlib
# def get_md5(str):
#     md5 = hashlib.md5()
#     md5.update(str.encode('utf-8'))
#     return md5.hexdigest()
# # print(get_md5('123456'))
# # print(get_md5('888888'))
# # print(get_md5('password'))
# db = {
#     'sophia': 'e10adc3949ba59abbe56e057f20f883e',
#     'bob': '21218cca77804d2ba1922c33e0151105',
#     'alice': '5f4dcc3b5aa765d61d8327deb882cf99'
# }
# def login(user, password):
#     if db.get(user) == None:
#         print("用户不存在")
#     else:
#         if get_md5(password) == db.get(user):
#             print("用户登录成功")
#         else:
#             print("用户密码输入错误")
# login('lalala', '123456')
# login('sophia', '888888')
# login('sophia', '123456')
#
# # 加盐过程, 可以加个用户名作为salt的一部分，再禁止重复用户名，以确保不同用户密码的MD5值永远不同
# def get_md5_salt(str):
#     md5 = hashlib.md5()
#     str = str + 'the_salt'
#     md5.update(str.encode('utf-8'))
#     return md5.hexdigest()

# import itertools
# import time
# 一个从2开始的无限循环器
# natuals = itertools.count(2)
# for n in natuals:
#     print(n)
#     time.sleep(1)

# 无限循环打印ABC三个字母
# cs = itertools.cycle('ABC')
# for c in cs:
#     time.sleep(1)
#     print(c)

# 无限循环同一个元素，也可以限定循环次数
# ns = itertools.repeat('A', 3)
# for n in ns:
#     time.sleep(1)
#     print(n)

# 截取部分
# natuals = itertools.count(1)
# ns = itertools.takewhile(lambda x: x <= 10, natuals)
# print(list(ns))

# 叠加迭代，结果为A B C X Y Z
# for c in itertools.chain('ABC', 'XYZ'):
#     print(c)

# 把相邻的重复元素跳出来分组打印
# for key, group in itertools.groupby('AAABBBCCAAA'):
#     print(key, list(group))

# 分组时忽略大小写
# for key, group in itertools.groupby('AaaABBbcAAa', lambda c: c.upper()):
#     print(key, list(group))

# 采用SAX方式解析XML
# from xml.parsers.expat import ParserCreate
#
# class DefaultSaxHandler(object):
#     def start_element(selfself, name, attrs):
#         print('sax: start_element: %s, attrs: %s' % (name, str(attrs)))
#
#     def end_element(self, name):
#         print('sax: end_element: %s' % name)
#
#     def char_data(self, text):
#         print('sax: char_data: %s' % text)
#
# xml = r'''<?xml version="1.0"?>
# <ol>
#     <li><a href="/python">Python</a></li>
#     <li><a href="/ruby">Ruby</a></li>
# </ol>
# '''
#
# handler = DefaultSaxHandler()
# parser = ParserCreate()
# parser.StartElementHandler = handler.start_element
# parser.EndElementHandler = handler.end_element
# parser.CharacterDataHandler = handler.char_data
# parser.Parse(xml)

# 生成 XML
# L = []
# L.append(r'<?xml version="1.0"?>')
# L.append(r'<root>')
# L.append(r'some & data')
# L.append(r'</root>')
# print(''.join(L))

# 解析雅虎天气
# from xml.parsers.expat import ParserCreate
#
# data = r'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
# <rss version="2.0" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
#     <channel>
#         <title>Yahoo! Weather - Beijing, CN</title>
#         <lastBuildDate>Wed, 27 May 2015 11:00 am CST</lastBuildDate>
#         <yweather:location city="Beijing" region="" country="China"/>
#         <yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
#         <yweather:wind chill="28" direction="180" speed="14.48" />
#         <yweather:atmosphere humidity="53" visibility="2.61" pressure="1006.1" rising="0" />
#         <yweather:astronomy sunrise="4:51 am" sunset="7:32 pm"/>
#         <item>
#             <geo:lat>39.91</geo:lat>
#             <geo:long>116.39</geo:long>
#             <pubDate>Wed, 27 May 2015 11:00 am CST</pubDate>
#             <yweather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" />
#             <yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
#             <yweather:forecast day="Thu" date="28 May 2015" low="21" high="34" text="Sunny" code="32" />
#             <yweather:forecast day="Fri" date="29 May 2015" low="18" high="25" text="AM Showers" code="39" />
#             <yweather:forecast day="Sat" date="30 May 2015" low="18" high="32" text="Sunny" code="32" />
#             <yweather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" />
#         </item>
#     </channel>
# </rss>
# '''
#
# weather_dict = {}  # 定义天气字典
# which_day = 0  # 哪一天
#
# class WeatherSaxHandler(object):
#     def start_element(self, name, attrs):
#
#         global weather_dict, which_day
#
#         if name == "yweather:location":
#             weather_dict['city'] = attrs['city']
#             weather_dict['country'] = attrs['country']
#
#         if name == 'yweather:forecast':
#             which_day += 1
#             if which_day == 1:
#                 weather_dict['today'] = {'text': attrs['text'], 'low': int(attrs['low']), 'high': int(attrs['high'])}
#             elif which_day == 2:
#                 weather_dict['tomorrow'] = {'text': attrs['text'], 'low': int(attrs['low']), 'high': int(attrs['high'])}
#
#     def end_element(self, name):
#         pass
#
#     def char_data(self, text):
#         pass
#
# def parse_weather(xml):
#     handler = WeatherSaxHandler()
#     parser = ParserCreate()
#     parser.StartElementHandler = handler.start_element
#     parser.EndElementHandler = handler.end_element
#     parser.CharacterDataHandler = handler.char_data
#     parser.Parse(xml)
#     return weather_dict
#
# weather = parse_weather(data)
# assert weather['city'] == 'Beijing', weather['city']
# assert weather['country'] == 'China', weather['country']
# assert weather['today']['text'] == 'Partly Cloudy', weather['today']['text']
# assert weather['today']['low'] == 20, weather['today']['low']
# assert weather['today']['high'] == 33, weather['today']['high']
# assert weather['tomorrow']['text'] == 'Sunny', weather['tomorrow']['text']
# assert weather['tomorrow']['low'] == 21, weather['tomorrow']['low']
# assert weather['tomorrow']['high'] == 34, weather['tomorrow']['high']
# print('Weather:', str(weather))

# from html.parser import HTMLParser
#
# class MyHTMLParser(HTMLParser):
#
#     def handle_starttag(self, tag, attrs):
#         print('<%s>' % tag)
#
#     def handle_endtag(self, tag):
#         print('</%s>' % tag)
#
#     def handle_startendtag(self, tag, attrs):
#         print('<%s/>' % tag)
#
#     def handle_data(self, data):
#         print(data)
#
#     def handle_comment(self, data):
#         print('<!--', data, '-->')
#
#     def handle_entityref(self, name):
#         print('&%s;' % name)
#
#     def handle_charref(self, name):
#         print('&#%s;' % name)
#
# parser = MyHTMLParser()
# parser.feed('''
# <html>
#     <head>
#     </head>
#     <body>
#     <!-- test html parser -->
#         <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...&#9660;<br>END</p>
#     </body>
# </html>
# ''')

# from urllib import request
#
# with request.urlopen('http://api.douban.com/v2/book/2129650') as f:
#     data = f.read()
#     print('Status: ', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s %s' % (k, v))
#     print('Data: ', data.decode('utf-8'))

# 模拟iphone移动端发送get请求，返回移动端网页内容
# from urllib import request
#
# req = request.Request('http://www.douban.com/')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     print('Status:', f.status, f.reason)
#     # for k, v in f.getheaders():
#     #     print('%s: %s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))

# 模拟post请求登录weibo
# from urllib import request, parse
#
# print('Login to weibo.cn ...')
# email = input('Email: ')
# passwd = input('Password: ')
# login_data = parse.urlencode(
#     [
#         ('username', email),
#         ('password', passwd),
#         ('entry', 'mweibo'),
#         ('client_id', ''),
#         ('savestate', '1'),
#         ('ec', ''),
#         ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
#     ]
# )
# req = request.Request('https://passport.weibo.cn/sso/login')
# req.add_header('Origin', 'https://passport.weibo.cn')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
#
# with request.urlopen(req, data=login_data.encode('utf-8')) as f:
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', f.read().decode('utf-8'))

# 将网页返回值转用json解析
# from urllib import request
# import json
#
# def fetch_data(url):
#
#     req = request.Request(url)
#     with request.urlopen(req) as f:
#         return json.loads(f.read().decode('utf-8'))
#
# # 测试
# URL = 'http://m.maoyan.com/ajax/movieOnInfoList?token='
# data = fetch_data(URL)
# print(data)
# assert data['stid']== '576591972453269000'
# print('ok')

# from PIL import Image, ImageDraw, ImageFont, ImageFilter
# import random
# # 随机字母:
# def rndChar():
#  return chr(random.randint(65, 90))
# # 随机颜色 1:
# def rndColor():
#     return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
#
# # 240 x 60:
# width = 60 * 4
# height = 60
# image = Image.new('RGB', (width, height), (255, 255, 255))
# # 创建 Font 对象:
# font = ImageFont.truetype('C:\\Windows\\Fonts\\Arial.ttf', 36)
# # 创建 Draw 对象:
# draw = ImageDraw.Draw(image)
# # 填充每个像素:
# for x in range(width):
#     for y in range(height):
#         draw.point((x, y), fill=rndColor())
# # 输出文字:
# for t in range(4):
#     draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor())
# # 模糊:
# image = image.filter(ImageFilter.BLUR)
# image.save('code.jpg', 'jpeg')
























