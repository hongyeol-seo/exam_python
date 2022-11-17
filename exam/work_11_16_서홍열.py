# 1. 아래 데이터를 jumsu라는 변수명으로 저장해 주세요. 그리고 총합, 평균을 출력하세요.

jumsu  = []
jumsu.append(98)
jumsu.append(71)
jumsu.append(90)
jumsu.append(82)
jumsu.append(88)
print(f'총합 : {sum(jumsu)}, 평균 : {(sum(jumsu)/len(jumsu)):.2f}')

# 2. {"김연아":"피겨스케이팅", "류현진":"야구", "박지성":"축구", "귀도":"파이썬"} 데이터에서 키만 출력, 값만 출력, 키와 값을 함께 출력해 주세요.

strDict = {"김연아":"피겨스케이팅", "류현진":"야구", "박지성":"축구", "귀도":"파이썬"}
print(f' 값만 출력 : {strDict.keys()}')
print(f' 키와 갑출력 : {strDict.values()}')
print(f' 키와 갑출력 : {strDict.items()}')

# 3. 3명의 사용자의 이름, 전화번호를 입력 받은 후 persons 변수명에 저장하세요.

person = {}
nameList = []
numList = []
for i in range(3) :
    nameList.append(input("이름을 입력해주세요. : ").strip())
    numList.append(input("번호를 입력해주세요. ex) 010-8583-8748 : ").strip())

person['이름'] = nameList
person['전화번호'] = numList

print(person)
print(person.keys())

# 4. foods={‘한식’:’불고기‘, ’중식‘:’자장면‘, ’일식‘:’스시‘} 데이터에서 한식과 일식 값 출력

foods={'한식':'불고기', '중식':'자장면', '일식':'스시'}
print('한식 값 : %s'%(foods['한식']))
print('일식 값 : %s'%(foods['일식']))

# 5 foods={‘한식’:’불고기‘, ’중식‘:’자장면‘, ’일식‘:’스시‘} 데이터에 사용자로부터 좋아하는
# 한식, 중식, 분식 입력받아서 데이터를 저장해 주세요.

favor = foods[input("좋아하는 음식을 종류를 입력해주세요. ex) 한식, 중식, 스시 중에서")]
print(favor)

# 6 { "류현진":"야구", "김연아":"피겨스케이팅", "박지성":"축구", "귀도":"파이썬"} 데이터에 손홍민선수에 대한 데이터를 추가 후, 정렬해 주세요.

sportPerson = { "류현진":"야구", "김연아":"피겨스케이팅", "박지성":"축구", "귀도":"파이썬"}
sportPerson['손흥민'] = '축구'
print(sorted(sportPerson,reverse=True)) #내림차순 

# 7 빈 데이터를 저장하는 코드를 리스트, 튜플, 딕셔너리, 집합, 문자열 등 각 데이터 타입에 따라 작성하세요.

exList = []
exTuple = ()
exDicit = {}
exSet = set()
exStr = ''

#8 아래 데이터를 student라는 변수명으로 저장하세요. 과목별 최고점수, 최저점수 출력하세요.

student = {'이름' : ['베트맨','마징가','슈퍼맨','슈렉','피오나'],'국어' : 
[90,82,77,94,78],'수학':[89,71,100,82,99],'윤리':[98,80,92,93,90],'국사':[99,91,90,71,83]}

print('국어최고 점수 : {}, 국어최저 점수 : {}'.format(max(student['국어']),min(student['국어'])))
print('수학최고 점수 : {}, 수학최저 점수 : {}'.format(max(student['수학']),min(student['수학'])))
print('윤리최고 점수 : {}, 윤리최저 점수 : {}'.format(max(student['윤리']),min(student['윤리'])))
print('국사최고 점수 : {}, 국사최저 점수 : {}'.format(max(student['국사']),min(student['국사'])))

#9 “Good Luck” 대한 알파벳 하나 하나에 대한 대문자를 요소로 하는 리스트 생성후 정렬해 주세요.

msg = "Good Luck"
msgList = []
msgList.extend(msg.upper())
msgList.sort(reverse=True)
msgList.remove(" ") #공백삭제
print(msgList)

# 10 1~50범위에서 2의 배수, 5의 배수, 7의 배수로 구성된 데이터를 저장하세요.
# 그리고 데이터에서 값들을 하나의 리스트로 합쳐주세요.

twoDiv = list(range(2,51,2))
fiveDiv = list(range(5,51,5))
sevenDiv = list(range(7,51,7))
result = twoDiv + fiveDiv + sevenDiv
result.sort(reverse=False)
print(result)