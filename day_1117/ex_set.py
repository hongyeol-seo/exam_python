# 집합자료형 frozenset타입! 
# 파이썬 2.3부터 지원됨
# 중복 x, 순서 x
# 변수명 = set(데이터)
# 원래는 list[] 이렇게 만들어야하는데, 알아서 넣어주겠다.
# 단, set은 set()형식으로 넣어줘야한다.
# numSet1 = {"1", 3, 5, [1,3]} # 수정가능 타입은 사용 불가
# print(type(numSet1)) #리스트 사용할 수 없다!!!!!!
# {"키":"값"}값도 넣을 수 없네
# string 수정 불가능하기때문에 가능함

numSet1 = {"1", 3, 5, (1,3)}
print(f"numSet1 => {type(numSet1)}, {numSet1}")

# 중복제거에 활용이 된다.
# 데이터 타입끼리 데이터 비교시에 활용한다.
# 합집합, 교집합, 차집합 기능을 제공한다.
# set객체생성
# 중복제거!

data1 = set() #비어있는 set #문자가 있는애들이 들어가야한다. / 인덱스가 있는 애드이 들어가야한다.

data2 = {1,3,4,5,6,7,8,9}
data3 = set("hello")

print('데이터 타입 : %s, \"갯수\" %s 모양 : %s' %(type(data1),len(data1),data1))
print('데이터 타입 : %s, \"갯수\" %s 모양 : %s' %(type(data2),len(data2),data2))
print('데이터 타입 : %s, \"갯수\" %s 모양 : %s' %(type(data3),len(data3),data3))

# 1~10 범위에서 2의 배수로구성된 데이터

div2 = set(range(2,11,2)) #
div5 = set(range(5,11,5)) #

# 2개의 데이터에 공통된 데이터를 출력하기

#교집합 & 엔퍼센트

print(list(div5&div5))
print(div2.intersection(div5)) #교집합 함수

#합집합 #2개의 데이터 중에서 모든 데이터/ 단 중복ㄷ제거하고 출력
print(div2|div5)
print(div2.union(div5))

#s1에만 존재하는 데이터를 출력
#s1 - s2
print(div2-div5)
print(list(div2.difference(div5))) #set으로 돌려주네! #리스트로 변경하는법

#문자열

print(3 in [1,3,5])
print("H" in "Hello")
print("A" in {"A":123})
print(123 not in {"A":123}) #키값이 있는지? '키'가 맞다면!