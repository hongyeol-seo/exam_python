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
