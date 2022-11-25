# count = 5

# while count > 0 :
#     print("Hello")
#     # count-=1

#다운카운팅방식 --------------
#업카운팅방식 ----------------

# 반복중단하기 break
# 반복중 조건에 해당하는 경우 즉시 반복을 중단!
# break 가장 가까이에 있는 반복문만 중단시킨다.
# 1~30 사이의 숫자 중에서 3의 배수이면서 5의 배수인 숫자가 나오면 중단하세요.

for i in range(1,31):
    if i%3 == 0 :

        if i%5 == 0 :
            print(f'3과 5의 배수 {i}', end="\t")
            break
        else:
            print(i, end="\t")

num = 1 
while num <=30:
    if num%15 == 0:
        break
    # if not num%15: break
    print(num)
    num+=1

isBreak = False #내부 반복문이 중단되었는지 정보를 담는 변수

for num in range(1,11):
    if isBreak:
        break
    print(f"----{num}")
    for data in ["A","B","C","D","E"]:
        #C인 경우 반복을 중단
        if data == "C":
            isBreak = True
            break
        print(data)

#사용자로부터 데이터를 입력 받아서 리스트에 저장! 종료시는 소문자 q나 대문자 Q입력시 종료할 것입니다.
#이런경우는 게속 운영되어야한다.

datas = []
while True :
    data = input("저장하고 싶은 데이터 입력(종료 : Q/q) : ").strip()
    if data in ["Q","q"] :
        print("프로그램을 종료합니다.")
        break

    else :
        datas.append(datas)

# --------------------------------------------------------
# 반복문에 실행을 위로 올려주는 기능?
# 반복문에서 코드 실행을 스킵하고, 다음으로 진행하도록하는 키워드
# --------------------------------------------------------

#1부터 30까지 숫자를 출력하는데 3의 배수는 출력하지말고, 나머지 숫자만 출력해주세요.

num = 0 
while num <= 30 :
    if num%3 == 0:
        print("")    
    else : print(num)

for n in range(1,31):
    if n%3 :
        print(n)

num = 0 
while num <= 30 :
    num += 1 
    if not num%3:
        # print()
        continue #위로올라간다.
    print(num)

for n in range(1,31):
    if not n%3 :
        print(n)

