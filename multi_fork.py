#-*- coding: utf-8 -*-
#!/usr/bin/python

import os

print('当前进程:%s 启动中 ....' % os.getpid())
#Fork a child process. Return 0 in the child and the child’s process id in the parent.
#Only in Linux
pid = os.fork()
if pid == 0:
    print('子进程:%s,父进程是:%s' % (os.getpid(), os.getppid()))
else:
    print('进程:%s 创建了子进程:%s' % (os.getpid(),pid ))