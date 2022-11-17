# 딕셔너리 데이터 타입 
# -형식 : {키:값, 키:값, 키:값}
# -인덱스 없음
# -키 값으로 value를 찾는다. 


nums1 = {} #딕셔너리
nums2 = {'name':'HONG',33:True,'jumsu':[4,5,6]} #딕셔너리

print('nums1 타입 {0}, 길기 : {1}'.format(type(nums1),len(nums1)))
print('nums2 타입 {}, 길기 : {}'.format(type(nums2),len(nums2)))

nums3 = {('name','phone'):['kim','010-8585-8748'],1:12} #리스트의 수정이 가능하기 때문에 가능함 / 문자열도 수정?안되기때문에 가능
print('nums3 타입 {}, 길기 : {}'.format(type(nums3),len(nums3)))
nums4 = {"datas": {'kor' :10, 'math':20}}
nums4 = {"datas": {'kor' :10}}

# test = "hello"
# test[1] = "i" # 'str' object does not support item assignment #수정 안됨
# print(test)

# dict 타입의 데이터 원소 읽기
# 변수명[키]로 데이터를 가져온다.

print(nums2['name'],type(nums2['name'])) 
print(nums2[33],type(nums2[33])) #키를 주면 값을 찾을 수 있다.
print(nums2['jumsu'], type(nums2['jumsu'])) #키를 주면 값을 찾을 수 있다.
# 존재하지 않는 키는 '키 에러' 


print(nums4['datas'],type(nums4['datas'])) #/?? 틀렸는데???

values = nums2['jumsu']
print(values[1])
print(nums2['jumsu'][1])

# print(nums4['datas']['math']) #math 점수를 빼기! 

#------------------------------------------
#새로운 데이터 추가!
#------------------------------------------
nums2['age'] = 12  #age라는 키 값 복사
print(nums2)

nums2['job'] = 'student' 
print(nums2)

# ------------------------------------------
# 값 수정 / 변경 / 업데이트
nums2['age'] = 100  
print(nums2)
# ------------------------------------------

#값 삭제
del nums2['name']
print(nums2)

print(nums2.pop('age')) #? 가지고 있는것

del nums4 #객체가 사라짐! 그렇다면 사라짐!