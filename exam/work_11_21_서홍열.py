# ➀ True, False 2가지 데이터만 저장하는 타입은 ( )입니다. True, False 데이터를 저장하는 변수 2개를 선언한 후타입을 출력하세요.

print('Boolen')
a = True
b = False
print(f'a 타입 : {type(a)}, b타입 {type(b)}')

#  ➁ 아래 데이터를 논리 데이터 타입으로 저장 후 출력하세요.

a = bool('Happy')
b = bool("")
c = bool([12])
d = bool([])
e = bool(("A"))
f = bool(())
g = bool({1:89, 2:12})
h = bool({})
i = bool(1)
j = bool(0)
k = bool(None)
l = bool(set())

abc = [a,b,c,d,e,f,g,h,i,j,k,l]
for i in range(len(abc)) :
    print("%s 의 값 :%s"%(chr(ord('a') + i),abc[i]))

#  ➂ 78점의 학점을 출력하는 코드를 작성하세요

score = 78 

if score >= 90 :
    print("A학점")

elif score >=80 :
    print("B학점")

elif score >= 70 :
    print("C학점")

elif score >= 60 :
    print("D학점")

else :
    print("망한학점")

#  ④ 국어, 영어, 수학, 미술 과목명을 키로 저장하는 데이터가 있습니다.
#  점수는 98, 45, 72, 99입니다, 과목에 대한 점수를 조사하는 경우 존재하는 과목인지
#  검사 후 점수를 출력하도록 코드를 작성해 주세요. (점수 조사 과목은 임의로 선택)

subject = {"국어":98,"영어":45,"수학":72,"미술":99}
sub = input("과목을 입력해주세요 : ").strip()

if sub and sub.isalpha():
    if sub in list(subject.keys()) :
        print(f'{sub}의 점수 : {subject[sub]}')

    else : 
        print("존재하지 않는 과목입니다.")
else: 
    print(f"입력값 형식이 잘못되었습니다. 입력값 : {sub}")

#  ⑤ 데이터를 입력 받고 입력 받은 데이터가 있는지 체크 후 있을 경우와 없는 경우에 따른 코드를 작성해 주세요. 입력된 데이터가 있는 경우 해당 데이터를 5번 반복 출력하세요. 

arr = ["대한민국","월드컵","카타르","손흥민","16강신화"]
arrSub = input("입력값을 입력해주세요. : ").strip()

if arrSub :
    if arrSub in arr :
        print("입력값이 존재합니다.")
        for i in range(6) :
            print(f'{arrSub}')
    
    else :
        print("데이터가 존재하지 않습니다.")

else :
    print(f"입력값 형식이 잘못되었습니다. 입력값 : {arrSub}")


# ⑥ 팔굽혀펴기 시험을 보는데 남자는 10번 이상이면 합격(Pass)이고 여자는 5번 이상을 해야 합격입니다. 합격(Pass)/불합격(Fail)을 출력하는 코드를 작성하세요.

man = 15 
woman = 7

print("합격") if man >= 10 else print("불합격")
print("합격") if woman >= 5 else print("불합격")


#다른 닶
gender, pushup = "F", 9

if gender == "M" :
    if pushup >= 10 :
        result = 'Pass'

    else :
        result = "Fail"

else :
    if pushup >- 5:
        result = 'pass'
    else :
        result = 'fail'

print(f'{gender}의 푸쉬업 {pushup}개 결과는 : {result}')

#  ⑦ 어떤 농장에서는 수박이 10kg이 넘으면 1등급, 그렇지 않고 7kg이 넘으면 2등급, 그렇지 않고 4kg이 넘으면 3등급, 나머지는 4등급을 준다고 합니다. 수학된 수박 무게를 입력 받아서 등급을 기준으로 수박 무게와 등급을 저장하세요.

waterMelon = int(input("수박 무게를 입력해주세요(kg) : "))

if waterMelon >= 10 :
    print(f"{waterMelon}kg은 1등급니다.")
elif waterMelon >= 7 :
    print(f"{waterMelon}kg은 2등급니다.")
elif waterMelon >= 4:
    print(f"{waterMelon}kg은 3등급니다.")
else :
    print(f"{waterMelon}kg은 4등급니다.")

#다른닶 : 딕셔너리에 값 저장!
# watermelonGrade={'1등급':[], '2등급':[], '3등급':[], '4등급':[]}

# ⑧ 입력 받은 나이의 연령대를 출력하세요. ( 영‧유아(0~5세), 아동(6~12세), 청소년(13~18세), 청년(19~29세), 중년(30~49세),장년(50~64세), 노년(65세 이상) )

age = int(input("연령을 입력해주세요 : "))

if age >= 65 :
    print(f"{age}세는 노년입니다.")
elif age >= 50 :
    print(f"{age}세는 장년입니다.")
elif age >= 30 :
    print(f"{age}세는 중년입니다.")
elif age >= 19 :
    print(f"{age}세는 청년입니다.")
elif age >= 13 :
    print(f"{age}세는 청소년입니다.")
elif age >= 6 :
    print(f"{age}세는 아동입니다.")
else :
    print(f"{age}세는 영유아입니다.")

# ⑨ 입력 받은 명문 문자열이 소문자이면 대문자로, 대문자이면 소문자로 출력해주세요.

checkStr = input("문자열을 입력해주세요 : ")

if checkStr.islower() :
    print(checkStr.upper())

else :
    print(checkStr.upper())

# ⑩ 숫자 입력을 요청하고 입력 받은 데이터를 검사한 후 입력 받은 데이터가 숫자인 경우만 '입력 OK', 아닌 경우는 '숫자 데이터가 아닙니다.'라고 출력하세요.

checkNum = input("숫자를 입력해주세요 : ").strip()

if checkNum :

    if checkNum.isdecimal() :
        print("입력 OK")

    else :
        print("숫자데이터가 아닙니다")

else :
    print(f"입력값 형식이 이상합니다. : {checkNum}")