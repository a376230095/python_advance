'''
我们事先了一个telnet客户端的类TelnetClient，调用实例的start()方法
启动客户端与服务器交互，交互完毕后需调用cleanup()方法，关闭已连接的socket
以及将操作历史记录写入文件并关闭

能否让telnetClient实例支持上下文管理协议，从而替代手工调用cleanup()方法
'''
from telnetlib import Telnet
from sys import stdin,stdout
from collections import deque

class TelnetClient():
    def __init__(self,addr,port=23):
        self.addr=addr
        self.port=port
        self.tn=None

    def start(self):
        self.tn=Telnet(self.addr,self.port)
        self.history=deque()



        #user
        t=self.tn.read_until(b"login: ")
        stdout.write(t)
        user=stdin.readline()
        self.tn.write(user)

        #password
        t=self.tn.read_until(b"Password: ")
        if t.startswith(user[:-1]): t= t[len(user) + 1:]
        stdout.write(t)
        self.tn.write(stdin.readline())

        t=self.tn.read_until(b'$ ')
        stdout.write(t)
        while True:
            uinput=stdin.readline()
            if not uinput:
                break
            self.history.append(uinput)
            self.tn.write(uinput)
            t=self.tn.read_until('$ ')
            stdout.write(t[len(uinput)+ 1:])

    def cleanup(self):
        self.tn.close()
        self.tn=None
        with open(self.addr+"_history.txt","w") as f:
            f.writelines(self.history)

client=TelnetClient('192.168.0.1')
print("\nstrat")
client.start()
print("\ncleanup")
client.cleanup()