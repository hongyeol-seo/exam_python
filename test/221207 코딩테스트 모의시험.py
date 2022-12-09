# 1
from datetime import datetime
msg = ['Good', 'child', 'Zoo', 'apple', 'Flower', 'zero']


def listSort(data):
    data.sort(reverse=True)
    print(data)
    print(f"가장 높은 문자열 {data[0]}, 가장 낮은 문자열 {data[-1]}")


listSort(msg)

# 2
data = "가나다"


def strEncoding(data):
    print("가나다의 16진수 인코딩 {}{}{}".format(
        hex(ord(data[0])), hex(ord(data[1])), hex(ord(data[2]))))
    print("가나다의 8진수 인코딩 {}{}{}".format(
        oct(ord(data[0])), oct(ord(data[1])), oct(ord(data[2]))))
    print("가나다의 2진수 인코딩 {}{}{}".format(
        bin(ord(data[0])), bin(ord(data[1])), bin(ord(data[2]))))


strEncoding(data)

# 3


def listSum(data):
    data1 = list(data.replace(",", ""))

    for i in range(len(data1)):
        data1[i] = int(data1[i])

    print(f"{data}의 합 : {sum(data1)},가장 큰 수 : {max(data1)}, 가장 작은 수 {min(data1)} ")


data = '123,42,98,18'
listSum(data)

data = '1,234'
listSum(data)

# 4


def strPrint(data):

    for i in range(1, data+1):
        j = str(i)
        if j[-1] == "2" or j[-1] == "4" or j[-1] == "8":
            print("#", end="")
        else:
            print(i, end="")

        if i % 20 == 0:
            print("")


strPrint(int(input("정수 입력 : ")))

# 5


def favorMonth(num):
    month = {
        1: ["Jan.", "Winter"],
        2: ["Fab.", "Wither"],
        3: ["Mar.", "Spring"],
        4: ["Apr.", "Spring"],
        5: ["May", "Spring"],
        6: ["Jun.", "Summer"],
        7: ["Jul.", "Summer"],
        8: ["Aug.", "Summer"],
        9: ["Sep.", "Fall"],
        10: ["OCt.", "Fall"],
        11: ["Nov.", "Fall"],
        12: ["Dec.", "Winter"]}

    if num in list(month.keys()):
        for i in month[num]:
            print(i, end=" ")
    else:
        print("존재하지 않는 월입니다.")


favorMonth(int(input("좋아하는 월 입력 : ")))

# 6


def addWon(n):
    n = n.strip()
    n = n.replace(",", "")
    n, won = n.split(" ")
    print(format(int(n), ","), won)


n = "    1234567, $"
addWon(n)
n = "907, W"
addWon(n)

# 7
# 함수


def div(n):
    arr = []
    for i in range(1, n+1):
        if n % i == 0:
            arr.append(str(i))

    print(f'{n}의 약수 : {" ".join(arr)}')


div(8)

# 8
# 함수


def outString(data):
    s1 = set()
    for i in data:
        if i.isdecimal():
            s1.add(int(i))
    s1 = list(s1)
    for j in s1:
        print(j, end=" ")


msg = "Happy New Year 2023"
outString(msg)
msg = '홍길동 010-1111-2222'
outString(msg)

# 9


def yourAge(data):

    tYear = datetime.today().year
    tMonth = datetime.today().month
    tDay = datetime.today().day

    year, month, day = data[:-1].split(".")
    print(tYear, type(tYear))

    age = tYear - int(year)
    KoeranAge = age + 1

    if tMonth < int(month):
        age -= 1
    elif tMonth == int(month) and tDay < int(day):
        age -= 1

    print(f"한국나이 {KoeranAge}")
    print(f'외국나이 {age}')


n = '2000.12.31.'
yourAge(n)

# 10


def factory(n):
    sum = 1
    if n == 0:
        print(f"{n}! => {n}", end=" ")
    else:
        print(f"{n}! =>", end=" ")
        for i in reversed(range(1, n+1)):
            sum *= i
            if i > 1:
                print(f"{i} * ", end="")
            else:
                print(f"{i} = {sum}")


factory(0)

# 11
# 다시 한 번 더 복습!


def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


# data = int(input("데이터를 입력해주세요. : "))
data = 50

for i in range(data+1):
    if isPrime(i):
        print(i, end=" ")

# 12

data = {"국어": [90, 82, 77, 94, 78], "수학": [89, 71, 100, 82, 99],
        "윤리": [98, 80, 92, 93, 91], "국사": [99, 91, 90, 71, 83]}
keyList = list(data.keys())

print(
    f"{keyList[0]} 최고점수 : {max(data[keyList[0]])}, 최저점수 : {min(data[keyList[0]])}")
print(
    f"{keyList[1]} 최고점수 : {max(data[keyList[1]])}, 최저점수 : {min(data[keyList[1]])}")
print(
    f"{keyList[2]} 최고점수 : {max(data[keyList[2]])}, 최저점수 : {min(data[keyList[2]])}")
print(
    f"{keyList[3]} 최고점수 : {max(data[keyList[3]])}, 최저점수 : {min(data[keyList[3]])}")

# 13
# 함수


def gugudan(n, m):

    strNum = n
    endNum = m
    line = 1
    check = True
    strCheck = True

    while check:
        if strCheck and strNum <= endNum:
            print(f"  --{strNum}단--  ", end="\t")
            strNum += 1
            continue

        elif strCheck and strNum > endNum:
            strNum = n
            strCheck = False
            print("")

        if strNum <= endNum and line < 10:
            print(f"{strNum} * {line} = {strNum*line}", end="\t")
            strNum += 1
            # continue

        if strNum <= endNum and line < 10:
            print(f"{strNum} * {line} = {strNum*line}", end="\t")
            strNum += 1
            # continue
        elif strNum > endNum and line < 10:
            print("")
            strNum = n
            line += 1
            # continue
        else:  # strNum > endNum and line > 10:
            check = False
            # break

# data = input("시작구구단, 종료구구단 : ")
gugudan(3, 7)

# 14

a = 12345

print("만의 자리 %s" % ((a//10000)))
print("천의 자리 %s" % ((a % 10000//1000)))
print("백의 자리 %s" % ((a % 1000//100)))
print("십의 자리 %s" % ((a % 100//10)))
print("일의 자리 %s" % ((a % 10)))

print("만의자리 {}:".format((a//10000) if (a//10000) >= 0 else ""))
print("천의자리 {}:".format(((a % 10000)//1000) if ((a % 10000)//1000) > 0 else ""))
print("백의자리 {}:".format(((a % 1000)//100) if (a % 1000//100) > 0 else ""))
print("십의자리 {}:".format(((a % 100)//10) if (a % 100//10) > 0 else ""))
print("일의자리 {}:".format(((a % 10)) if (a % 10) > 0 else ""))

# 15


def addData(*data):
    if len(data) > 0:
        if isinstance(data[0], str):
            print("앞에 숫자", data[0])
            if data[0].isdecimal():
                sum = 0

            else:
                sum = ""

        else:
            sum = 0

        for i in data:
            if type(i) == str and i.isdecimal():
                sum += int(i)
            else:
                sum += i

        print(sum)

    else:
        print(None)


addData()
addData(1, 3, 5)
# addData(True, True, False, False, True)
# addData('A')
# addData('A', 'BC', 'Good')
# addData("2", "9", "3")

# 16

for i in range(1, 9):
    print("{:^15}".format("*"*((2*i)-1)))

print("{:^15}".format("****"))
print("{:^15}".format("****"))
print("{:^15}".format("Merry Chiristmas"))
print("{:^15}".format("2023"))

# 17

msg = 'Merry Christmas Happy New Year'

newString = [i.upper() if i.islower() else i.lower() for i in msg]

print("".join(newString))

# 18


def fourCalc(num1, num2):
    addValue = num1+num2
    subValue = num1-num2
    mulValue = num1*num2
    divValue = num1/num2 if num2 > 0 else 0
    remain = num1 % num2
    remain2 = num1//num2

    return addValue, subValue, mulValue, divValue, remain, remain2


print('덧셈 값 : {}, \n뺄셈 값 : {}, \n곱셉 값 : {},\n나눗셈 값 {}, \n나머지 값 : {}, \n몫 : {}'.format(fourCalc(4, 3)[
      0], fourCalc(4, 3)[1], fourCalc(4, 3)[2], fourCalc(4, 3)[3], fourCalc(4, 3)[4], fourCalc(4, 3)[5]))

# 19 #복습


def saveInfo(**datas):
    for i in datas.keys():
        if datas.get(i) != "":
            print(f"{i} => {datas[i]}")


id = input("아이디를 입력하세요 : ").strip()
name = input("이름을 입력하세요 : ").strip()
age = input("나이를 입력하세요 : ").strip()
phone = input("번호를 입력하세요 : ").strip()
job = input("직업을 입력하세요.").strip()
loc = input("지역을 입력하세요 : ").strip()

saveInfo(id1=id, name1=name, age1=age, phone1=phone, job1=job, loc1=loc)

# 20


def menu():
    print("="*40)
    print("1. 입력", end="\t")
    print("2. 덧셈", end="\t")
    print("3. 뺄셈", end="\n")
    print("4. 곱셈", end="\t")
    print("5. 나눗셈", end="  ")
    print("6. 종료")
    print("="*40)


isCheck = False
while True:

    menu()
    data = int(input("메뉴 선택(1~6) : "))

    if data == 1:
        if isCheck == 0:
            nums = input("숫자 2개 입력 : ").strip()
            n, m = nums.split(",")
            n = int(n)
            m = int(m)
            isCheck = True
        else:
            print("이미 입력값이 있습니다.")

    elif data == 2 and isCheck:
        print(f"{n} + {m} = {n+m}")

    elif data == 3 and isCheck:
        print(f"{n} + {m} = {n-m}")

    elif data == 4 and isCheck:
        print(f"{n} * {m} = {n*m}")

    elif data == 5 and isCheck:
        print(f"{n} / {m} = {n/m}")

    elif data == 6 and isCheck:
        print("나의 계산기 프로그램을 종료합니다.")
        break

    else:
        print("메뉴 선택 오류")
