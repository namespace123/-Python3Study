# L1 = ['1', '2', '3']
# L2 = [x for x in L1]
# print(L2)

# def add(a, b, f):
#     return f(a) + f(b)
#
#
# print(add(-5, 6, abs))

# def f(x):
#     return x * x
#
#
# r = map(f, [1, 3, 6, 9])
# print(list(r))

# print(list(map(str, [1, 4, 8, 4, 5])))

# print(bool())
# print(bool(0))
# print(bool(1))
# print(bool("1"))
# print(bool("0"))
# print(bool(""))

# s = "abcc"
# x = "c"
# print(s.count(x))

# symbols = "$%&^*7"
# codes = []
# for symbol in symbols:
#     codes.append(ord(symbol))
#
# print(codes)
#
# symbols = "$%&^*7"
# codes = [ord(symbol) for symbol in symbols]
# print(codes)

# colors = ['white', 'black']
# sizes = ['S', 'M', 'L']
# shirts = [(color, size) for color in colors for size in sizes]
# print(shirts)

# symbols = "$%&^*7"
# print(tuple(ord(symbol) for symbol in symbols))
#
# import array
# print(array.array('I', (ord(symbol) for symbol in symbols)))

# lax_coor = (33.9425, -118.408056)
# lon, lat = lax_coor
# print(lon)
# print(lat)
# city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
# print(city)
# traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
# for passport in sorted(traveler_ids):
#     print('%s/%s' % passport)
#
# for country, _ in traveler_ids:
#     print(country)

# t = (20, 8)
# print(divmod(*t))

# import os
# _, filename = os.path.split('/home/sophia/lalala/hehehe/111.bcp')
# print(filename)

# a, b, *rest = range(0, 5)
# print(a, b, rest)
#
# a, *rest, b = range(0, 5)
# print(a, rest, b)

# metro_areas = [
#     ('Tokyo', 'JP', 36.933, (35.68, 139.69)),
#     ('Delhi NCR', 'IN', 21.935, (28.61, 77.20)),
#     ('Mexico City', 'MX', 20.142, (19.43, -99.13)),
#     ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
#     ('Sao Paulo', 'BR', 19.649, (-23.54, -46.63))
# ]
#
# print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
# fmt = '{:15} | {:9.4f} | {:9.4f}'
# for name, cc, pop, (lat, lon) in metro_areas:
#     if (lon <= 0):
#         print(fmt.format(name, lon, lat))

# from collections import namedtuple
#
# City = namedtuple('City', 'name country population coordinates')
# tokyo = City('Tokyo', 'JP', 36.933, (35.68, 139.69))
# print(tokyo)
# print(tokyo.population)
# print(tokyo.coordinates)
# print(tokyo[1])
# print(City._fields)  #查看字段名
#
# LatLong = namedtuple('LatLong', 'lat long')
# delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.61, 77.20))
# delhi = City._make(delhi_data)
# print(delhi)
# print(delhi._asdict())
# for key, value in delhi._asdict().items():
#     print(key + ':' + str(value))

# a = [1, 2, 3]
# b = ['mac', 'python']
# c = 'linux'
#
# a.append(b)
# a.append(c)
# print(a)
# a = [1, 2, 3]
# a.extend(b)
# print(a.extend(c))
# a = [1, 2, 3]
# a.__iadd__(b)
# print(a.__iadd__(c))

# import copy
#
# a = [1, 2, 3, 4, ['a', 'b']]
# print('原     a= ', a)
#
# b = a  # 直接复制，对象的引用，相当于别名
# c = copy.copy(a)  # 浅拷贝，只拷贝了父对象，不会拷贝对象的内部的子对象
# d = a.copy()  # 浅拷贝，只拷贝了父对象，不会拷贝对象的内部的子对象
# e = copy.deepcopy(a)  # 深拷贝，完全拷贝了父对象及其子对象
#
# a.append(5)
# a[4].append('c')
#
# print('后     a= ', a)
# print('赋 值  b= ', b)
# print('浅拷贝 c= ', c)
# print('浅拷贝 d= ', d)
# print('深拷贝 e= ', e)
