# 변수명 = (값1, 값2, 값3)
# - 여러가지 종류의 여러개의 데이터를 저장하는 타입
# - 저장 후 수정/삭제/추가 안됨
# - 저장된 데이터/요소 읽기만 가능 => Read Only 
# 형태
# (데이터1, 데이터2...)
# 데이터,
# (데이터,)
# 데이터, 데이터

empty = () #빈것만들었지만 아무것도 할 수 없다.
# 가변 동적할당
nums1 = (1,2,3)
nums2 = 1,2,3
nums3 = (1,)
nums4 = 1,
nums5 = (1)
nums6 =  1 

print(f'empty 타입 : {type(empty)}')
print(f'num1 타입 : {type(nums1)}')
print(f'num2 타입 : {type(nums2)}')
print(f'num3 타입 : {type(nums3)}')
print(f'num4 타입 : {type(nums4)}')
print(f'num5 타입 : {type(nums5)}')
print(f'num6 타입 : {type(nums6)}')

# 함수 반환값에서 튜플 바뀌면 안되니까! / 데이터를 받을때 / 힙에 저장한다. 객체이기때문에 다 힙에 저장한다. 사라지면 안되잖아!

# 인덱싱

# 슬라이싱 

nums = tuple(range(10))
print(nums[1])

#값 변경 x
#요소 삭제 x

nums.count(4)

#형 변환 시켜서 값 변환한다.
#변경 못하는 걸 '상수'라고 한다. #시퀀스데이터타입(=이터러블) : 순서가 있는 데이터 타입!

# str를 list로 형변환 

world = 'Hello'
newList = list(world) #extend랑 비슷하네
print(str(newList)) #list를 str로 바꾸면 고대로 나옴!
