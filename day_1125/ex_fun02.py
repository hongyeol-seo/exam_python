#range오브젝트??
#함수는 클래스입니다.

def addTwo(a,b):
    return a+b

#함수의 타입
# <class 'function'> <class 'builtin_function_or_method'>
print(type(addTwo),type(len))
myfunc = addTwo

print(myfunc(3,4),addTwo(3,4)) #함수처럼 동작시킨다.
print(id(myfunc),id(addTwo))

#함수! 오브젝트!
