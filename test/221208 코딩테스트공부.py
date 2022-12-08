# 20

# def menu():
#     print("="*40)
#     print("1. 입력", end="\t")
#     print("2. 덧셈", end="\t")
#     print("3. 뺄셈")
#     print("4. 곱셈", end="\t")
#     print("5. 나눗셈", end="  ")
#     print("6. 종료")
#     print("="*40)


# datas = False

# while True:
#     menu()

#     num = int(input("메뉴 입력 : "))
#     if datas == 0 and num == 1:
#         n, m = input("숫자 2개 입력 : ").split(",")
#         n = int(n)
#         m = int(m)
#         datas = True
#         continue
#     elif datas and num == 2:
#         print("{} + {} = {}".format(n, m, (n+m)))
#     elif datas and num == 3:
#         print("{} = {} = {}".format(n, m, (n-m)))
#     elif datas and num == 4:
#         print("{} * {} = {}".format(n, m, (n*m)))
#     elif datas and num == 5:
#         print("{} / {} = {}".format(n, m, (n/m)))
#     elif num == 6:
#         print("나의 계산기 프로그램을 종료합니다.")
#         break

#     else:
#         print("입력 데이터를 확인해주세요.")


# 19

# def outString(**datas):

#     for i in datas.keys():
#         if datas[i] != "":
#             print(f'{i} => {datas[i]}')


# while True:

#     name = input("이름 : ")
#     age = input("나이 : ")
#     phone = input("번호 : ")
#     job = input("직업 : ")
#     loc = input("지역 : ")
#     id = input("아이디 : ")

#     outString(dname=name, dage=age, dphone=phone, djob=job, dloc=loc, did=id)

# # 18

# def sixCalu(num1, num2):
#     addValue = num1 + num2
#     midValue = num1 - num2
#     mulValue = num1 * num2
#     divValue = num1 / num2 if num2 > 0 else 0

#     return addValue, midValue, mulValue, divValue


# print(sixCalu(3, 4))

# # 17
# data = 'Merry Christmas HaPPy New YEaR'
# data = [i.lower() if i.isupper() else i.upper() for i in data]
# print("".join(data))

# # 16

# for i in range(1, 17, 2):
#     print("{:^15}".format("*"*i))

# print("{:^15}".format("*"*4))
# print("{:^15}".format("*"*4))
# print("{:^15}".format("Merry Christmas"))
# print("{:^15}".format("2023"))

# 15


# def addData(*datas):
#     if len(datas) > 0:
#         # print(datas, type(datas))
#         arr = list(datas)
#         sum = 0
#         if isinstance(arr[0], str):
#             sum = ""
#             for i in datas:

#                 sum += i
#         else:
#             for i in datas:

#                 sum += i
#         print(sum)

#     else:
#         print("값이 없습니다.")


# addData()
# addData(1, 3, 5)
# addData(True, True, False, False, True)
# addData('A')
# addData('A', 'BC', 'Good')
# addData("2", "9", "3")

# 14


# def countNums(n):
#     if n//10000 > 0:
#         print("만의 자리 {}".format(n // 10000))
#     if n % 10000//1000 > 0:
#         print("천의 자리 {}".format(n % 10000 // 1000))
#     if n % 1000//100 > 0:
#         print("백의 자리 {}".format(n % 1000 // 100))
#     if n % 100//10 > 0:
#         print("십의 자리 {}".format(n % 100 // 10))
#     else:
#         print("일의 자리 {}".format(n % 10))

# countNums(1234)

# 11

# def primeNum(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False

#     return True


# n = 30

# for i in range(2, n+1):
#     if primeNum(i):
#         print(i, end="  ")

# from datetime import datetime

# data = "2000.12.31."

# year, month, day = data[:-1].split(".")
# year = int(year)
# month = int(month)
# day = int(day)

# todayYear = datetime.today().year
# todayMon = datetime.today().month
# today = datetime.today().day

# age = todayYear - year
# koeanAge = age+1

# print(f"당신의 한국 나이는 {koeanAge}")

# if todayMon < month:
#     age -= 1
#     print(f"당신의 외국 나이는 {age}")
# elif todayMon == month and today < day:
#     age -= 1
#     print(f"당신의 외국 나이는 {age}")

# else:
#     print(f"당신의 외국 나이는 {age}")

# 4

# n = 100

# for j in range(n+1):
#     i = str(j)
#     if i[-1] == "2" or i[-1] == "4" or i[-1] == "8":
#         print("#", end=" ")
#     else:
#         print(i, end=" ")

#     if j % 20 == 0:
#         print("")

# 8

def outString(msg):
    arr = set()

    for i in msg:
        if i.isdecimal():
            # print(i)
            arr.add(int(i))

    print(arr)


msg = "Happy New Year 2023"
outString(msg)
msg = '홍길동 010-1111-2222'
outString(msg)
