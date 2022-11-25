# --------------------------
# 내가 만드는 함수들
# --------------------------
# 2개 숫자를 덧셈후 반환하는 기능
# 2개 숫자, 곱셈, 나눗셈!

def twoPlus(num1, num2):
    return(num1+num2)
def twoMinus(num1, num2):
    return(num1-num2)
def twoMulti(num1, num2):
    return(num1*num2)
def twodiv(num1, num2):
    return(num1/num2)

print("{} + {} = {}".format(100,50,twoPlus(100,50)))
print("{} - {} = {}".format(100,50,twoMinus(100,50)))
print("{} * {} = {}".format(100,50,twoMulti(100,50)))
print("{} / {} = {}".format(100,50,twodiv(100,50)))

# 나의 계산기 프로그램!
# 1. 입력
# 2. 덧ㅅ
# 3. 뺄샘
# 4. 곱셈
# 5. 나눗셈
# 6. 종료

isCheck = False

def printMenu():
    print("""
        ---------------
        나의 계산기 프로그램!
        ---------------
        1. 입력
        2. 덧셈
        3. 뺄샘
        4. 곱셈
        5. 나눗셈
        6. 종료
        ---------------
        """)

while True :
    #메뉴띄우는함수

    printMenu()
    

    choice = input("메뉴 선택(1~6 : ").strip()
    if choice == "6":
        print("나의 계산기를 종료합니다.")
        break

    elif choice == "1":
        num1,num2 = input("숫자 2개 입력 ex(1,7): ").strip().split(",")
        num1 = int(num1)
        num2 = int(num2)
        print(f'num1 : {num1}, num2 : {num2}')
        isCheck = True
        continue

    elif choice == "2":
        if isCheck :
            #더하기
            print(f'{num1} + {num2} = {twoPlus(num1,num2)}')
            continue

        else :
            print("입력한 데이터가 없습니다.")


    elif choice == "3":
        if isCheck :
        #빼기
            print(f'{num1} - {num2} = {twoMinus(num1,num2)}')
            continue
        else :
            print("입력한 데이터가 없습니다.")

    elif choice == "4":
        if isCheck :
        #곱하기
            print(f'{num1} * {num2} = {twoMulti(num1,num2)}')
            continue
        else :
            print("입력한 데이터가 없습니다.")


    elif choice == "5":
        if isCheck :
        #나누기
            print(f'{num1} / {num2} = {twodiv(num1,num2)}')
            continue
        else :
            print("입력한 데이터가 없습니다.")