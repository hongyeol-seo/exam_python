# Lsit 자료형
# - 여러가지 종류의 데이터를 담는 자료형
# - 형태 : [데이터1, 데이터2..., 데이터N]
# - 요소 / 원소 : 리스트 안에 들어있는 데이터
# ------------------------------------------
# List 객체생성

emList = []
numLIst = [5,23,0.9,7,-1]
strList = ["A","BCD","한글","123"]
dataList = [12,"a",True, 235]
dataList2 = [1,2,3,['a','b',[]]]

#해당하는 리스트안에
list = [emList,numLIst,strList,dataList,dataList2]

for i in list : 
    print(f'%s 갯수 %s 개:'%(i,len(i)) )

#리스트 안에 요소 값 읽기
print(numLIst[0])
print(numLIst[1])
print(numLIst[:-1])

numLIst[0] = "수정" #리스트는, 딕셔너리 가변 
print(numLIst)

#dataList2 요소출력하기
print(dataList2[0],dataList2[-1])
print(type(dataList2[0]),type(dataList2[-1]))

print(dataList2[0],dataList2[-1][1]) #만약 b를 빼고 싶다면!? 

a = [1,2,['a','b',['life','is']]]

print(a[-1][-1][0])

#요소변경하기
#str 타입은 지원안함

nums = [1,20,3,4,5]
nums[1] =2
print(nums) 
#슬라이싱 

print(nums[1:4:2])
print(nums[0::2]) #0번 요소부터 짝수 인덱스 요소만 출력 -> [시작인덱스 : 끝인덱스+1 : 간격] #if없이 뽑아올 수도 있다.

#1번 요소부 ~ 3번 요소 값을 ''a로 변경
nums[1:3] = ['a','a','a']
nums[1:3] = ['a','a','a','a','a'] #그러면 바뀜 / 만약에 인덱스를 넘친다고 하더라도 그냥 다 넣는다.
print(nums)

nums[:-3] =[0] #앞에 날리고 0으로 대체하기 
print(nums) #만약 범위가 적다면 요소가 있는 부분까지만 바꾼다.

nums[:]=[]
print(nums)

