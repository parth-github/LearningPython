
'''
def f1():
	print('Something')

x = f1
x() # calling x actually calls f1
'''
###########
def f2():
    def f1():
        print('Something')
    return f1

# x = f1() # nested function: f1 can't called directly
#x() # calling x actually calls f1

##### how to call nested function outside its scope
def f2(f):
    def f1():
        print('This is before function call')
        f()
        print('This is after function call')
    return f1
'''
same as 
f3 = f2(f3)
'''
@f2 

def f3():
    print('this is f3')

f3()


