# #set형태

# s1 = set({1, 2, 3})
# s2 = set([1, 2, 3])
# s3 = {1, 2, 3}
# print(s1)
# print(s2)
# print(s3)
# print(type(s1))
# print(type(s2))
# print(type(s3))


# foods={'한식':'불고기', '중식':'자장면', '일식':'스시'}
# print('한식 값 : %s'%(foods['한식']))
# print('일식 값 : %s'%(foods['일식']))

# # 5 foods={‘한식’:’불고기‘, ’중식‘:’자장면‘, ’일식‘:’스시‘} 데이터에 사용자로부터 좋아하는
# # 한식, 중식, 분식 입력받아서 데이터를 저장해 주세요.

# food = foods[input("좋아하는 음식을 종류를 입력해주세요. ex) 한식, 중식, 스시 중에서")]
# print(food)

# print(type((0))) #인트
# print(type([0])) #리스트
# print(type({0})) #셋

# nums = {1,4,2,3}
# nums.pop()
# print(nums)
# nums2 = [1,4,2,3]
# nums2.pop(3)
# print(nums2)

# dict = {'a' : '허ㅗㅇ열'}
# print(dict.keys('a'))


# for i in range(len(abcBig)) :
#     print(abcBig[i],abcBig[i].lower())





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