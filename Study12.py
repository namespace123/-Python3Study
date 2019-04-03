# 图形界面
# from tkinter import *
# import tkinter.messagebox as messagebox
#
# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.ceateWidgets()
#
#     def ceateWidgets(self):
#         self.nameInput = Entry(self)
#         self.nameInput.pack()
#         self.alterButton = Button(self, text='hello', command=self.hello)
#         self.alterButton.pack()
#
#     def hello(self):
#         name = self.nameInput.get() or 'world'
#         messagebox.showinfo('Message', 'Hello, %s' % name)
#
# app = Application()
# app.master.title('Hello, World!')
# app.mainloop()

# 网络通信就是两个进程之间的通信
# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('www.sina.com.cn', 80))
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# # 接收数据
# buffer = []
# while True:
#     # 每次最多接收1k字节
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = b''.join(buffer)
# s.close()
# with open('lalala.html', 'wb') as f2:
#     f2.write(data)
#
#
# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))
# # 把接收的数据写入文件
# with open('sina.html', 'wb') as f:
#     f.write(html)

import asyncio

@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用 asyncio.sleep
    r = yield from asyncio.sleep(1)
    print("Hello again!")

# 获取 EventLoop：
loop = asyncio.get_event_loop()
# 执行 coroutine
loop.run_until_complete(hello())
loop.close()















