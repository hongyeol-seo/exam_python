# List 전용의 함수들은 => 메소드라고한다.
# List 객체 생성
nums = [1,2,3,4,5,6,7,8,9,10]

#List 전용메서드 
# (1) 리스트 바꾸기 #reverse 어떤 것은 결과물이 있고, 어떤 것은 없다.
# 리스트 데이터의 요소 순서를 반대로 해서 저장
nums.reverse()

# (2) 리스트 요소/인덱스 반환하는 메서드
# 리스트에는 index는 없다. 없으면 Error

# nIdx= nums.index(0) #에러나는걸
# print(nIdx)

#오류가 나지 않도록 하려면 / 먼저 요소가 있는지 여부를 판단한 다음에!
print(nums)
if 3 in nums: #숫자는 3으로 그냥 때려야한다.
    print("포함")
    
else :
    print("불포함")

#요소삭제 

nums.remove(7) #제일 첫번째 값만 발견해서 삭제

#리스트에서 요소/ 원소를 꺼내는 메서드
#일단 이 데이터를 
#list.pop() 제일 마지막 요소 꺼내기
#list.pop(index) 지정된 인덱스의 요소 꺼내기

pickNums = nums.pop()
print(f'pick : {pickNums}')

pickNums = nums.pop(1)
print(f'pick : {pickNums}')

#test 
fruits = ['', 'banana', 'cherry']
if 'banana' in fruits:
    print('포함')
else:
    print('미포함')

# (3) 리스트의 요소/원소 삭제하는 명령어 
# del 삭제하고 싶은 요소
del nums[-1] #특정 인덱스 값을 지우는 것
print(f'nums -> {nums}')

#(4) 리스트 모든 요소/원소 삭제하는 메서드 
nums.clear() #비우기
print(f'nums : {nums}')
 
#(5) 리스트에 요소/원소 추가하는 메서드 / append
# 인덱스가 없는 경우에는 index[0] = 추가하는 것 할 수없다.

nums.insert(-1,11) #insert
print()

# nums.insert(len(nums),11) #append를 사용해서 마지막에 넣는방법이랑 / insert를 통해서 넣는 법  
# 가장 많은 자료형이,  

# (7) 리스트 요소/원소 정렬하는 메소드
# list.sort()오름차순 정렬 (ascending) 기본값
# list.sort()내림차순 정렬 (decending)

nums = [1,2,3,4,5,6,7,8,9,10]

nums.sort(reverse=1) #내림차순을 하고 싶다면 파라미터를 봐야한다. #True 내림차순 1 
print(f'nums : {nums}')

# (8) 리스트 확장시켜주는 메서드 
# List.extend()
nums.append(11)
nums.extend('pig') #인서랑 append의 차이점 #대괄호를 해서 넣어야하고
print(nums) #iterable 데이터 타입 str이 각각 index를 가지고 있기 때문에 

#index라는 메서드는 반환값이 에러 메시지를 띄우기 때문에 그 전에 있는지 여부를 파악해야한다.