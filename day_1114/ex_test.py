#실습1
nums = [1,3,5,7,9,11,13,15]
#짝수 요소만 출력
print(nums[1::2])
#제일 첫번째, 마지막 요소 제외한 나머지 출력
print(nums[1:-1])
#nums = [1,3,'A',15]가 되도록 값 변경
nums[2:-1] = ['A']
print(f'변경된 값 변경 : {nums}')

#실습2 
bools = [False, True, False, False, True, False,False,True]
#Ture 데이터만 출력 
print(bools[1::3])

#실습3
datas = [[11],2,3,[44,44,[66,77,[88]]],9,10]
# 88 데이터 출력 
print(datas[3][2][2])
# 77, 88 데이터 출력 
print(datas[3][2][1:])
# 9, 10 데이터 출력
print(datas[-2],datas[-1]) 