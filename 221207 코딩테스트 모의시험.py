# 1
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
