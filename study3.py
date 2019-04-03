# a = dict(one=1, two=2, three=3)
# b = {'one': 1, 'two': 2, 'three': 3}
# c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
# d = dict([('two', 2), ('one', 1), ('three', 3)])
# e = dict({'three': 3, 'one': 1, 'two': 2})
# print(a == b == c == d == e)  # True

# DIAL_CODES = [
#     (86, 'China'),
#     (91, 'India'),
#     (1, 'USA'),
#     (62, 'Indonesia'),
#     (81, 'Japan'),
#     (7, 'Russia'),
#     (880, 'Bangladesh')
# ]
# print(DIAL_CODES)
# country_code = {country: code for code, country in DIAL_CODES}
# print(country_code)
# print({code: country.upper() for country, code in country_code.items() if code < 66})

# import sys
# import re
#
# WORD_RE = re.compile(r'\w+')
# index = {}
# with open(sys.argv[1], encoding='utf-8') as fp:
#     for line_to, line in enumerate(fp, 1):
#         for match in WORD_RE.finditer(line):
#             word = match.group()
#             column_no = match.start() + 1
#             location = (line_to, column_no)
#             # 这其实是一种很不好的实现， 这样写只是为了证明论点
#             # occurrences = index.get(word, [])
#             # occurrences.append(location)
#             # index[word] = occurrences
#             # 使用setdefault方法一步到位
#             index.setdefault(word, []).append(location)
# for word in sorted(index, key=str.upper()):
#     print(word, index[word])

# import sys
# import re
# import collections
#
# WORD_RE = re.compile(r'\w+')
# index = collections.defaultdict(list)
# with open(sys.argv[1], encoding='utf-8') as fp:
#     for line_to, line in enumerate(fp, 1):
#         for match in WORD_RE.finditer(line):
#             word = match.group()
#             column_no = match.start() + 1
#             location = (line_to, column_no)
#             index[word].append(location)
# for word in sorted(index, key=str.upper()):
#     print(word, index[word])

# class StrKeyDict(dict):
#     def __missing__(self, key):
#         if isinstance(key, str):
#             raise KeyError(key)
#         return self[str(key)]
#
#     def get(self, key, default=None):
#         try:
#             return self[key]
#         except KeyError:
#             return default
#
#     def __contains__(self, key):
#         return key in self.keys() or str(key) in self.keys()
#
#
# d = StrKeyDict([('2', 'two'), ('4', 'four')])
# print(d['2'])
# print(d[4])
# # print(d[1])
# print(d.get('2'))
# print(d.get(4))
# print(d.get(1, 'N/A'))
# print(2 in d)
# print(1 in d)

# import collections
#
# ct = collections.Counter('abfajhafsdafds')
# print(ct)
# ct.update('aaaaaaaaazzz')
# print(ct)
# print(ct.most_common(2))

# import collections
#
# class StrKeyDict(collections.UserDict):
#     def __missing__(self, key):
#         if isinstance(key, str):
#             raise KeyError(key)
#         return self[str(key)]
#
#     def __contains__(self, key):
#         return str(key) in self.data
#
#     def __setitem__(self, key, item):
#         self.data[str(key)] = item
# d = StrKeyDict([('2', 'two'), ('4', 'four')])
# print(d['2'])
# print(d[4])
# # print(d[1])
# print(d.get('2'))
# print(d.get(4))
# print(d.get(1, 'N/A'))
# print(2 in d)
# print(1 in d)

# from types import MappingProxyType
# d = {1: 'A'}
# d_proxy = MappingProxyType(d)
# print(d_proxy)
# print(d_proxy[1])
# # d_proxy[2] = 'x'
# d[2] = 'B'
# print(d_proxy)
# print(d_proxy[2])
# print(d)

# l = ['spam', 'spam', 'eggs', 'spam']
# print(set(l))
# print(list(set(l)))
#
# a = {'lalala', 'hehehe', 'heiheihei'}
# b = {'xixixi', 'hehehe'}
# print(a | b)
# print(a & b)
# print(a - b)
#
# # 快速计算交集
# found = len(set(a) & set(b))
# print(found)
# found = len(set(a).intersection(set(b)))
# print(found)

# from dis import dis
# print(dis('{1}'))
# print("---------")
# print(dis('set(1)'))

# print(frozenset(range(10)))

# from unicodedata import name
# print({chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')})

print(1 == 1.0)
print(hash(1))
print(hash(1.0))
















































