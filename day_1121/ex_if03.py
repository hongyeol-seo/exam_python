# 입력 받은 숫자가 3의 배수면, 3의 배수라고하고
# 아니면 아닙니다. 3의 배수가 아닙니다.

# print(list(range(3,100,3)))


#Hello 단어가 있고, 사용자가 입력한 알파벳이 단어에 포함되어있는지?


# "H" in "Hello"

#[실습] 점수를 입력받고 학점 A-F에서 해당점수의 학점을 출력해주세요.

score = int(input("점수를 입력해주세요 : ").strip())

if score :

    if score >= 90 :
        print("A학점")

    elif score >= 80 :
        print("B학점")

    elif score >= 70:
        print("C학점")

    elif score >= 60 :
        print("D학점")

    else :
        print("F학점")

else :
    print("점수를 다시 입력해주세요")


#[실습] 

member = ["마징가","홍길동","베트맨","세종대왕","나"]
isMember = False

name = '베트맨'

if name in member :
    isMember = True

else :
    isMember = False

print(f'{name}는 멤버 : {isMember}')

#실습 
#사용자로부터 숫자를 입력받고 존재하지 않은 숫자면 추가해주시고,
#존재하는 숫자라면 "이미 존재합니다"라고 출력해주세요.


nums = [1,2,3,4,5,6,7]
num = input("숫자를 입력해주쇼 : ").strip()

if num.isdecimal():
    num = int(num)

    if num in nums :
        print(f"{num}는 이미 존재합니다.")

    else :
        nums.append(num)

else :
    print(f'{num}는 숫자가 아닙니다.')
print(nums)


# 존재하지 않으면 숫자를 추가해주세요.
# 단 가장 작은 값보다 크고, 가장 큰 값보다 작은 경우에만 추가해주세요