# l = list(range(10))
# print(l)
# l[2:5] = [20, 30]
# print(l)
# del l[5:7]
# print(l)
# l[3::2] = [11, 22]
# print(l)
# #错误： l[2:5] = 100
# l[2:5] = [100]
# print(l)
# l[2:3] = [200]
# print(l)

# 引用和可变对象背后的原理和陷阱
# print(['_'] * 3)
# board = [['_'] * 3 for i in range(3)]
# print(board)
# board[1][2] = 'X'
# print(board)
#
# board = [['_'] * 3] * 3
# print(board)
# board[1][2] = 'X'
# print(board)
#
# # 相当于第一种
# board = [['_'] * 3, ['_'] * 3, ['_'] * 3]
# print(board)
# board[1][2] = 'X'
# print(board)
#
# # 同第二种
# row = ['_'] * 3
# board = []
# for i in range(3):
#     board.append(row)
# board[1][2] = 'X'
# print(board)
#
# # 同第一种
# board = []
# for i in range(3):
#     row = ['_'] * 3
#     board.append(row)
# board[1][2] = 'X'
# print(board)

# l = [1, 2, 3]
# print(id(l))
# l *= 2
# print(l)
# print(id(l))
#
# t = (1, 2, 3)
# print(id(t))
# t *= 2
# print(id(t))

# t = (1, 2, [30, 40])
# try:
#     t[2] += [50, 60] #有效果，但是会把报错
# except Exception as e:
#     print(e)
# print(t)
# try:
#     t[2].extend([50, 60]) #有效果，且不会报错
# except Exception as e:
#     print(e)
# print(t)

# from dis import dis
# dis('s[a] += b')

# fruits = ['grape', 'raspberry', 'apple', 'banana']
# print(sorted(fruits, key=len, reverse=False))
# print(fruits)
# fruits.sort()
# print(fruits)

# import bisect
# import sys
#
# HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 26, 29, 30]
# NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]
# ROW_FMT = '{0:<2d} @ {1:<2d}    {2}{0:<2d}'
#
#
# def demo(bisect_fn):
#     for needle in reversed(NEEDLES):
#         position = bisect_fn(HAYSTACK, needle)
#         offset = position * '    |'
#         print(ROW_FMT.format(needle, position, offset))
#
#
# def main(name):
#     if name == 'left':
#         bisect_fn = bisect.bisect_left
#     else:
#         bisect_fn = bisect.bisect
#     print('DEMO:', bisect_fn.__name__)
#     print('haystack ->', '   '.join('%2d' % n for n in HAYSTACK))
#     demo(bisect_fn)
#
#
# if __name__ == '__main__':
#     main(sys.argv[-1])

# import bisect
# HAYSTACK = [1.0, 4, 5, 6, 8, 12, 13, 15, 20, 21, 23, 26, 29, 30]
# index1 = bisect.bisect_left(HAYSTACK, 1)
# index2 = bisect.bisect_right(HAYSTACK, 1)
# print(index1)
# print(index2)
#
# # 计算等级
# def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
#     i = bisect.bisect(breakpoints, score)
#     return grades[i]
#
# l = [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
# print(l)

# import bisect
# import random
# SIZE = 7
# random.seed(1729)
#
# my_list = []
# for i in range(SIZE):
#     new_item = random.randrange(SIZE * 2)
#     bisect.insort(my_list, new_item)
#     print('%2d ->' % new_item, my_list)

# from array import array
# from random import random
# floats = array('d', (random() for i in range(10**7)))
# print(floats[-1])
# fp = open('floats.bin', 'wb')
# floats.tofile(fp)
# fp.close()
#
# floats2 = array('d')
# fp2 = open('floats.bin', 'rb')
# floats2.fromfile(fp2, 10**7)
# fp2.close()
# print(floats2[-1])

import array
numbers = array.array('h', [-2, -1, 0, 1, 2])
memv = memoryview(numbers)
print(len(memv))
print(memv[0])
memv_oct = memv.cast('B')
print(memv_oct.tolist())
print(memv_oct[5])
memv_oct[5] = 4
print(numbers)

# import numpy
# a = numpy.arange(12)
# print(a)
# print(type(a))
# print(a.shape)
# a.shape = 3, 4
# print(a)
# print(a[2])
# print(a[:, 1])
# print(a.transpose())  #行和列交换

# import numpy
# floats = numpy.loadtxt('lalala.txt')
# print(floats[-3:])
# floats *= .5
# print(floats[-3:])
# from time import perf_counter as pc
# t0 = pc()
# floats /= 3
# print(pc() - t0)
# numpy.save('floats-10M', floats)
# floats2 = numpy.load('floats-10M.npy', 'r+')
# floats2 *= 6
# print(floats2[-3:])

# 双向队列
# from collections import deque
# dq = deque(range(10), maxlen=10)
# print(dq)
# dq.rotate(3)
# print(dq)
# dq.rotate(-4)
# print(dq)
# dq.appendleft(-1)
# print(dq)
# dq.extend([11, 22, 33])
# print(dq)
# dq.extendleft([10, 20, 30, 40])
# print(dq)

# l = [28, 14, '28', 5, '9', '1', 0, 6, '23', 19]
# print(sorted(l, key=int))
# print(sorted(l, key=str))