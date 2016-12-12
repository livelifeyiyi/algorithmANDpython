#-*- coding: utf-8 -*-

#生成器，只能读取一次
mygenerator = (x*x for x in range(3))
for i in mygenerator :
	print(i)
for i in mygenerator :
	print(i)
print "*"*20


def createGenerator():
	mylist = range(3)
	for i in mylist:
		yield i*i
mygenerator = createGenerator()
print mygenerator
print mygenerator.next()
print mygenerator.next()
# or use:
for i in mygenerator:
	print i
print "*"*20

#使用generator的next方法执行yield里的代码
def yield_fun():
	a = 3
	b = 2
	yield a
	c = 4
	yield b
generator = yield_fun()
print generator.next()
print generator.next()
print "*"*20

#yield除了把资料传给呼叫者外，还可以从呼叫者接受资料
def yield_fun():
	a = 3
	b = 2
	b = yield a
	yield b
generator = yield_fun()
print generator.next()
print generator.send(8)