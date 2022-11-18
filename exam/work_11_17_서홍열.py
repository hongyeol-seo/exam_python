# ➀ 1,5,3,9,1,1,2,8,7,4,2 데이터 중복 제거 후 저장하고 타입, 개수, 데이터 출력하세요.

arr = {1,5,3,9,1,1,2,8,7,4,2}
print(f'타입 : {type(arr)}\n개수 : {len(arr)}\n데이터 출력 : {arr}')
s1 = set([1,2,3])
# ➁ [1,1,5,2,6,9,2]와 [5,9,1,3,4,2,8,7,1,2,5] 데이터를 중복된 값을 제거한 하나의 리스트를 생성해 주세요.  

arr = set([1,1,5,2,6,9,2])
arr2 = set([5,9,1,3,4,2,8,7,1,2,5])

arr3 = arr.intersection(arr2)
print(arr3)

# ➂ ‘Happy Christmas’ 문자열에서 알파벳만 중복을 제거한 데이터로 저장해 주세요.

msg = 'Happy Christmas'
msg = set(msg.replace(" ",""))
print(msg)

# ④ 1부터 6까지의 값을 가진 데이터 num6, 4부터 9까지의 값을 가진 데이터 num9에서 num6에만 존재하는 데이터를 출력하세요. 
# 그리고 num6와 num9에 모두 존재하는 # 데이터를 출력하세요. 그리고 num6와 num9의 모든 데이터를 중복 없이 출력하세요.
num6 = set(range(1,7))
num9 = set(range(4,10))
print('nam6에만 존재하는 데이터 %s' %(num6.difference(num9)))
print('num6|num9 데이터 %s :' %(num6.union(num9)))
print('중복없이 출력 : %s' %(num6.intersection(num9)))

# ⑤ [9, 3, 1, 8, 7, 2, 1, 4, 2, 3, 5, 7] 에서 중복된 데이터 제외한 데이터들 평균 출력
strArr = set([9, 3, 1, 8, 7, 2, 1, 4, 2, 3, 5, 7])
print(strArr)
print("평균출력 %s"%(sum(strArr)/len(strArr)))

# ⑥ 집합 1,2,3 데이터에 [4,5,6,7,8] 데이터를 한꺼번에 추가 해 주세요.

nums = set([1,2,3])
nums.update([4,5,6,7,8])
print(nums)

# ⑦ 데이터 {'name':'pey', 'phone':'0119993323', 'birth': '1118'}에서 메서드를 사용해서 1118과 pey를 출력하세요. 그리고 gender에 대한 값을 출력하세요.
# 조건) 값이 없을 경우 no-data라고 출력하세요.

strDict = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}

print("결과값 1 : %s\n결과값 2 : %s\n결과값 3 : %s"%(strDict.get('name'),strDict.get('birth'),strDict.get('gender',"no-data")))

# ⑧ True, False 2가지 데이터만 저장하는 타입은 (bool)입니다.
# True, False 데이터를 저장하는 변수 2개를 선언한 후 타입을 출력하세요.

a = True
b = False
print(f'a 타입 : {type(a)}, b타입 {type(b)}')

#  ⑨ 아래 데이터를 논리 데이터 타입으로 저장 후 출력하세요.

a = bool('Happy')
b = bool("")
c = bool([12])
d = bool([])
e = bool(("A"))
f = bool(())
g = bool({1:89, 2:12})
h = bool({})
i = bool(1)
j = bool(0)
k = bool(None)
l = bool(set())

abc = [a,b,c,d,e,f,g,h,i,j,k,l]
for i in range(len(abc)) :
    print("%s 의 값 :%s"%(chr(ord('a') + i),abc[i]))