# for n in nums:
bigNums = range(10001)
bigNums = range(1,10001)

print(type(bigNums),bigNums,bigNums[0],bigNums[-1])
print(bigNums[:3])
#인덱스로 원소 접근이 되니까 for이 들어가는거임
#그래서 괄호가 필요하다면 list로 변환 / 값을 찍으면 / 슬라이싱이랑 인덱스 접근도 되지만...

nums = [11,22,33,44,55,66,77,88,99]
#nums 짝수 인덱스 요소만 출력만 출력해주세요.

for idx in range(0,len(nums)) :
    if idx%2 == 0 :
        print(nums[idx])

    # if not idx%2 : 


for idx in range(0,len(nums),2) :
      print(nums[idx])

    # if not idx%2 : 


for i in range(2,9) :
    
    print(f'{i} 단')
    for j in range(9) :
        print(f'{i} * {j} = {i*j}')
    
    print()

# 숫자문자열으 정수로 형변환하기!
nums = ["1","3","8","10"]

for n in range(len(nums)) :
    nums[n] = int(nums[n])

print(nums)


#딕셔너리
#묶여있던 애들이 풀리는것
data = {"name" : "홍열","지역":"서울"}
a = ((1,2),(3,4),(5,6))

for (key, valeu) in data.items() :
    print(key, valeu)

for (tu,ple) in a :
    print(tu,ple)

#튜플
for i in range(2,10) :
    
    print(f'{i} 단')
    for j in range(1,10) :
        print(f'{i} * {j} = {i*j:2}')
    
    print()


    seven = list(range(0, 101, 7))
# 한 줄에 3줄씩 나오게 해봐라!

# 첫번째 버전
# for num in seven :
#     if num % 35 : #35의 배수 #5개씩 나오는거  #규칙을 찾아야한다.
#        print(num, end=" ")

#     else:
#          print(num, end="\n")

# seven의 인덱스를 하려고한다면

# 두 번째 버전
# for idx in range(len(seven)):
#     if idx % 5 == 4:
#         print(seven[idx], end="\n")

#     else:
#         print(seven[idx], end="\t")

# 적어서보자!
# 0 1 2 3 4
# 5 6 7 8 9 5라는게 관계가 있을때 5로 나누었을때 나머지가 4인애들
# 반복을 쓸 때는 유사하거나, 반복적인 것을 할 때 찾아낸다.
# 값으로 할 수도 있고, 정답을 알 수 있다.

# 최대값 최소값

# 4나 9로 나누었을때 0이면 되나요?

#문제 1부터 500까지 한 줄에 5줄 출력해봐라

#값으로 출력 
for n in range(1,500) :
    if n%5 == 0 :
        print(n, end="\n")
    else : 
        print(n, end="\t")

#값으로 출력 (3줄) 

for n in range(1,500) :
    if n%3 == 0 :
        print(n, end="\n")
    else : 
        print(n, end="\t")

#값으로 출력 6줄
for n in range(1,500) :
    if n%6 == 0 :
        print(n, end="\n")
    else : 
        print(n, end="\t")

#인덱스로 출력! 

seven = list(range(0, 501, 4))

# 3줄

for idx in range(len(seven)) :
    if idx%3 == 2 :
        print(seven[idx],end="\n")
    else :
        print(seven[idx],end="\t")
