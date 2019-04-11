# 测试单元
import unittest
class TestDict(unittest.TestCase):

    # 每个函数开始前都要执行的操作放在这里，简化代码
    def setUp(self):
        print("setUp ...")

    # 每个函数结束时都要执行的操作放在这里，简化代码
    def tearDown(self):
        print("tearDown ...")

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

unittest.main()