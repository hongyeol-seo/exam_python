#115

num = int(input("정수를 입력해주세요. : "))

num1 = (num-20)

if num1 < 0 :
    print(0)

elif num1 > 255 :
    print(255)

#116
time = input(" 현재시간: ").strip()
newtime = int(time[-2:])

if newtime == 00 :
    print("정각입니다.")

else :
    print("정각이 아닙니다.")

#117
fruit = ["사과", "포도", "홍시"]
# msg = input("좋아하는 과일은? : ")

if "사과" in fruit :
    print("정답입니다.")

else :
    print("오답입니다.")

#119
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}

msg = "봄"
if msg in fruit.keys() :
    print("정답입니다.")

else:
    print("오답입니다.")

# fruit.get(msg,"오답입니다.")