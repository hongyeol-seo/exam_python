# 복습하기
year = 2022
data = year
year = 2023

nums=[1,2,3]
back = nums

#얕은 복사!

# --------------------------------------------------------------

print('id(nums)',id(nums),'id(back)',id(back))
print('nums[0] : ',nums[0], 'back[0] :' , back[0])

nums[0] = 7
print('id(nums)',id(nums),'id(back)',id(back))
print('nums[0] : ',nums[0], 'back[0] :' , back[0])

# --------------------------------------------------------------

nums=[['A'],1,2,3]
back = nums
nums_copy = nums.copy()

#얕은 복사! 만약에 내부까지 수정하려면, 모듈을 사용해서 바꾸어야한다.

print('id(nums)',id(nums),'id(nums_copy)',id(nums_copy))
print('nums[0] : ',nums[0], 'nums_copy[0] :' , nums_copy[0])

nums[0][0] = 11
nums_copy[3] = 7

print('id(nums)',id(nums),'id(nums_copy)',id(nums_copy))
print('nums[0] : ',nums[0], 'nums_copy[0] :' , nums_copy[0])

# https://docs.python.org/3/library/copy.html

# 복사와 관련된 내용 
# --------------------------------------------------------------

kor, eng, math, art = [98,99,'A',81]
kor, eng, math, art = 98,99,'A',81

# print(kor)
# 여기는 각각 저장되어있기 때문에 