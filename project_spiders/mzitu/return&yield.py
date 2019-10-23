# def func1():
#     for i in range(1, 5):
#         print(i)

# def func2():
#     for i in range(1, 5):
#     	return i

# def func3():
#     for i in range(1, 5):
#         yield i

# func1() 
# print("**************************")
# print (func2())
# print("**************************")
# print (func3())

'''
1.print并不会阻断程序的执行，就不用多说了。
2.func2()方法中的循环执行第一次就被return结束掉了。（后面的2、3、4就不会有返回的机会了）
3.yield你可以通俗的叫它"轮转容器"，可用现实的一种实物来理解：
水车，先yield来装入数据、产出generator object、使用next()来释放；
好比水车转动后，车轮上的水槽装入水，随着轮子转动，被转到下面的水槽就能将水送入水道中流入田里。
'''

# def func3():
#     for i in range(1,5):
#         yield i#装入
 
# gob = func3()#generator 类型
# print (next(gob))#1    释放的第一个装入的数据，（先入先出）
# print (next(gob))#2
# print (next(gob))#3
# print (next(gob))#4
 
# print (next(gob))#报错


# 个人理解，yield在python内部是当作list处理的：
def func3():
    for i in range(1,5):
        yield i
        
yi = []
yi = func3()
print(yi)
for y in yi:
    print (y)

'''
yield 生成器相比 return一次返回所有结果的优势：
（1）反应更迅速
（2）更节省空间
（3）使用更灵活
'''