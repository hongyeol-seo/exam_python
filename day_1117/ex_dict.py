#사람의 정보 저장 /알아서 노필기
#데이터 저장용 변수 선언 / 알아서 노필기
#값을 가져오는 메서드
#dict.get(키)
#존재하는 키라면 값을 반환
#존재하지 않으면 None 반환 any|none 있으면 any를 반환(값)
#왜냐하면 print(dict['없는키'])를 부르면 key 에러나옴

person = {'name' : '서홍열','job':'학생','age':31}
print(person.get('name2', '존재하지 않는 키')) #함수가 들어갈 수도 있네!
# print(person.get('name2', person.clear())) #함수가 들어갈 수도 있네!

print(len(person))
# person.clear()
print(person)
# print(person.pop('name')) pop() 인덱스가 없기 때문에 키를 넣어야한다. 근데 만약 키가 없다면 에러 메시지를 띄우겟다
# print(person)
location = '주소'
person.update({location:"대구"}) #kwargs #키 값 형태로 반환한다. #딕셔너리 딕셔너리로도 넗수 잇따 
person.update(name='홍길동') #없다면 추가 있으면 변경
print(f'뭐지? {person[location]}')
print(person)

# ---------------------------------
# dict.pop(키)
print(f'묶어서 같이 뺀다. {person.popitem()}') #제일 마지막에 들어있는 키와 아이템을 뺀다.
msg = person.popitem()
print(msg) #제일마지막에 있는 뒷부분부터/ 키와 값을 튜플 형식으로 꺼내는 메서드 
print(person)

#del을 사용해서 삭제할 수도 있다!

# s1 = set([1,2,3])
# print(s1)
# s1 = set(1,2,3)

