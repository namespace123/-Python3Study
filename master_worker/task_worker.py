import time, queue
from multiprocessing.managers import BaseManager

# 从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass

if __name__ == '__main__':

    # 由于是从网络获取Queue，所以注册时只提供名字
    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')
    # 绑定端口 5000， 设置验证码 ‘abc’
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    # 从网络连接
    manager.connect()
    # 获得 Queue 的对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    # 从task队列取任务，并把结果写入result队列
    for i in range(10):
        try:
            n = task.get(timeout=1)
            print('run task %d * %d ...' % (n, n))
            r = '%d * %d = %d' % (n, n, n*n)
            time.sleep(1)
            result.put(r)
        except Exception:
            print('connect fail or task queue is empty.')

    # 处理结果
    print('worker exit.')
