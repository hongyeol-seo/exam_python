a = "String"
b = ['a','bc','def','ghij','klmnop']
c = ('a','bc','def','ghij','klmnop')
d = {'name' : 'hong','job':'student','age':10}

#문자열합치기 or 사이값으로넣어도되고
a1 = "/".join(a)
b1 = "/".join(b)
c1 = "/".join(c)
d1 = "".join(d)

print(f'a1타입 : {type(a1)}, 결과값 {a1:=^30}')
print(f'b1타입 : {type(b1)}, 결과값 {b1:=^30}')
print(f'c1타입 : {type(c1)}, 결과값 {c1:=^30}')
print(f'd1타입 : {type(d1)}, 결과값 {d1:=^30}')

print(f'위치값 알려주기 {a.find("S")}')
print(f'위치값 알려주기 {a.index("S")}') #리스트도 같은 기능이 있다. 그런데 없으면 오류를 띄움
print(f'값 변경하기 {a.replace("Str", "Int")}')
print(f'값 자르기 {a.split("r")}')

help(str)