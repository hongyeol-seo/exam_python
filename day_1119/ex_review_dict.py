#list[], dict{}, tuple(),set(),str,bool
#딕셔너리의 키 : 수정/변경되지 않는 값 "이뮤터블(immutable)" (string, tuple)

# string, 튜플, 

exDict = {"name" : "Yeol","favor" : "bigdata", "hobby" : "bike"}

# 값추가
exDict['location'] = 'Seoul' #key가 없다면, value와 함께추가
exDict['location'] = 'Deagu' #key, value가 있다면 value만 변경
result = exDict["hobby"] #value 반환 #pop으로 인한 key, value 삭제
# result = exDict["hobby","favor"] #요소를 2개 이상 사용할 수 없음
print(f'result : {result}')
# reslut2 = exDict["hobby2"] #반환값이 없다면 에러메시지 KeyError: 'hobby2'
getResult = exDict.get('hobby','없다면 이 메세지를 출력하세요') #
getResult = exDict.get('hobby','defalut 값은 None Object') #

#2개의 키가 동시에 존재하는 경우, 첫 번째 key 무시 "hobby" : "bike" 삭제 
exDict = {"name" : "Yeol","favor" : "bigdata", "hobby" : "bike", "hobby" : "read"}

# 업데이트
exDict.update(name='hongyeol') #key가 있으면 value 갱신
exDict.update(name2='hongyeol') #key가 없다면 value와 함께 생성
exDict.update({'update':'result'}) #dict자료형으로 할당가능


#값출력
popResult = exDict.pop("hobby",'KeyError 대신 msg') #value값을 반환한다. 없다면 KeyError
print(f'pop 반환값 => str : {popResult,type(popResult)}')
print(f'pop 이후 {exDict}')
popitemResult = exDict.popitem() #lIFO방식으로 tuple출력
print(f'popitem 반환값 => tuple : {popitemResult,type(popitemResult)}')
boolReslut = 'name' in exDict #해당키가 있는지 없는지 반환! True vs False

#값복사
exDict = {"name" : "Yeol","favor" : "bigdata", "hobby" : "bike"}
exDict2 = exDict.copy() #복사
# print(exDict[:]) #list[:]

#딕셔너리 메소드
exDict.keys() #dict_keys 객체를 리턴해준다. 본래 리스트로 반환해주었으나, 메모리를 적게 소요하기위해서
exDict.values() #dict_value 객체를 리턴해준다.  
exDict.items() #key와 value가 담겨있는 dict_items 객체를 리턴해준다.

#iterate하기 때문에 for에서도 사용가능하다.
for x in exDict.keys():
    print(x,end=",")

for x in exDict.values():
    print(x,end=',')

#삭제
del exDict["favor" ] #[key] 와 value 함께 삭제
exDict.clear() #key, value 지움

# exSet = set()
# print(f'출력값 : {exSet}, 타입 : {type(exSet)}')


# print(list(iter(exDict))) #? 
# print(list(iter('korea')))

