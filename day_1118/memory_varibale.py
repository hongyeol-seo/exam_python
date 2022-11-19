# 메모리와 변수
# - 메모리 : 데이터를 저장하는 공간
# - 변 수  : 데이터가 저장된 메모리 주소를 가지고 있음
# => 참조하고 있음
# => 주소로 메모시를 찾아가서 데이터를 읽기/변경

age = 20

# 언패킹 (묶어서 따로따로 저장하는 방법, 풀어놓았던 애들은 풀어서)
name, age = ('마징가',12) #튜플 / 
print(name, age) 

kor, eng = {98, 99} #묶여있는 애들을 한 곳에만 저장하는 것이 아니라, 풀어서 저장한다.
# kor, eng = {98, 99, 100,81} #묶여있는 애들을 한 곳에만 저장하는 것이 아니라, 풀어서 저장한다. 
# too many values to unpack (expected 2) 언패킹을 하기에는 변수가 많다.
# kor, eng = ([98, 99], [100,81]) 이것도 안딘다.

data1='원더우먼','히어로'
data2=('원더우먼','히어로') #튜플 타입
print(data2)
print(data1, type(data1)) #이것도 튜플!

#변수와 복사
year = 2022

#.copy() 카피본을 만들 수가 있다.


year = 2022
data = year
year = 2023

nums=[1,2,3]
back = nums
print('nums[0] : ',nums[0], 'back[0] :' , back[0])
print('id(nums)',id(nums),'id(back)',id(back))

nums[0] = 11

print('nums[0] : ',nums[0], 'back[0] :' , back[0])
print('id(nums)',id(nums),'id(back)',id(back))

#리스트의 값이 변경되어도, 참조하는 주소값은 변하지 않는다. 왜냐하면 리스트안에는변경된 주소만 있을뿐이다.
#1000번지의 주소를 nums도 보고 있고, 11을 넣는다고해서, 1000번지의 주소가 바뀌지는 않는다.
#파이썬 튜터 , 바구니의 내용을 바꾼다고해서 바구니가 바꾸지 않는다.
