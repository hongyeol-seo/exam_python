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

# 4 [9, 3, 1, 8, 7, 2, 1, 4, 2, 3, 5, 7] 에서 중복된 데이터 제외한 데이터들의 평균 출력하세요.

arr = [9, 3, 1, 8, 7, 2, 1, 4, 2, 3, 5, 7]
print(sum((set(arr))))

# 5 ‘가을 하늘’에 대한 코드값을 출력하고, 다시 코드값에 대한 문자열을 출력하세요.

# 6 { "류현진":"야구", "김연아":"피겨스케이팅", "박지성":"축구", "귀도":"파이썬"} 데이터에 손홍민선수에 대한 데이터를 추가 후, 정렬해 주세요.

# 7 빈 데이터를 저장하는 코드를 리스트, 튜플, 딕셔너리, 집합, 문자열 등 각 데이터 타입에 따라 작성하세요.

# 8 아래 데이터를 student라는 변수명으로 저장하세요. 과목별 최고점수, 최저점수 출력하세요.

# 9 “Good Luck” 대한 알파벳 하나 하나에 대한 대문자를 요소로 하는 리스트 생성 후 정렬해 주세요. 

# 10 1~50범위에서 2의 배수와 5의 배수로 구성된 데이터를 저장한 후 중복된 데이터를 제거해 주세요.