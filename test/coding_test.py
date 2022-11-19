# 1. 3, 6, 9 게임을 파이썬으로 구현해 보세요.

msg = int(input("숫자를 입력하세요 : "))

for num in range(1,msg+1):
    
    count = 0

    for x in str(num) :
        
        if ("3" in x) or ("6" in x) or ("9" in x) :
            count += 1

    if (count > 0) :
        print("x" * count, end=" ")
    
    else :
        print(num, end=" ")

# 2. 고무 공을 100 미터 높이에서 떨어뜨리는데, 이 공은 땅에 닿을 때마다 원래 높이의 3/5 
#    만큼 튀어오릅니다. 공이 열 번 튈 동안, 그때마다 공의 높이를 계산후 출력하세요.

for i in range(1,11):
    x = 10000 #cm
    y = float(3/5)
    print("{}번째 높이 : {:.2f}cm".format(i,x*(y**i)))


# 3. 산책을 하는 도중 심부름을 하게 되었습니다. 현재 가지고 있는 금액과 심부름으로 구매한 
#   제품가격을 입력 받으세요. 그리고 아래 2가지 결과를 출력해 주세요.

#가지고 있는 금액 
remain = 1600

if (remain // 5000) :
    result = remain - 5000*(remain // 5000)
    if(result // 1000) :
        result2 = result//1000
    print(f"5천원 {remain // 5000}, 1천원{result//1000}")

elif (remain // 1000) :
        result2 = remain//1000    
        print(f"1천원 {result2}")
 
else :
    print(remain)

# 4. 밀리세컨드는 1초를 1000으로 나눈 시간으로 밀리세컨드(ms)를 입력 받아서 시-분-초를
#    변환하여 출력하는 코드를 작성하세요.


# 5. 월(Month)을 입력 받아 해당 월(Month)의 계절을 출력하는 코드를 작성하세요.
#    단, 월(Month)에 해당하지 않는 숫자 입력 시 “잘못된 데이터입니다” 출력요망
spring = [3,4,5]
summer = [6,7,8]
autumn = [9,10,11]
winter = [12,1,2]

season = input("월을 입력해주세요.").strip()

if season.isdecimal() :
    
    if int(season) in spring :
        print("봄입니다.")
    elif int(season) in summer :
        print("여름입니다")
    elif int(season) in autumn :
        print("가을입니다.")
    else :
        print("겨울입니다.")

else :
    print("잘못된 데이터 입력입니다.")  


# 6. 1과 자시자신만을 약수로 가지는 수를 소수(prime number)라 한다.
#    입력받은 숫자 범위에서 소수만 출력하는 코드를 작성하세요.


# 7. 아래 그림처럼 *을 출력하는 코드를 작성하세요.

for i in range(1,6) :
    print("{:>5}".format("*"*i))

# 8. 숫자와 콤마로만 이루어진 문자열 S가 주어진다. 이때, S에 포함되어있는 자연수의 합을 
#   구하는 프로그램을 작성하시오.
#   ( 예 :  123,42,98,18 입력  )

s = '123,42,98,18'
arr = s.split(',')

for i in range(len(arr)):
    arr[i] = int(arr[i])

print(sum(arr))

# 9. 입력된 영단어가 팰린드롬이면 1, 아니면 0을 출력하는 프로그램을 작성하세요.
#    *팰린드롬: 거꾸로 읽어도 제대로 읽는 것과 같은 문장이나 낱말, 숫자, 문자열.
#    ( 예 :  level, noon => 1,  run, apple =>0 )

msg = 'level'

if msg == msg[::-1] :
    print(1)

else :
    print(0)

# 10. *(애스터리스크)로 아래 출력 결과와 동일한 Tree(트리)를 만드시오.

for i in range(11) :
    print("{:^21}".format("*"*(2*i)+"*"))

print("{:^21}".format("***"))
print("{:^21}".format("***"))
print("{:^21}".format("***"))

# 11. 피보나치 수열을 구현하세요.
#     피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 
#     1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.
#     이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.
#     n=17일때 까지 피보나치 수를 써보면 다음과 같다.
#     0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
#     n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

# 12.  3개의 정수를 입력 받아서 가장 큰수, 가장 작은 수를 출력하는 함수를 구현하세요.

arr = []
count = 0
for i in range(3) :
    num = input("정수를 입력해주세요 : ").strip()

    if num.isdigit():
        arr.append(int(num))
        count += 1 

    else :
        print("정수가 아닙니다.")
        break

if count == 3 :
    print(f"가장 큰 수 {max(arr)}, 가장 작은 수{min(arr)}")

# 13. 문자열 리스트를 입력 받아서 오름차순 결과 가장 낮은 문자열과 가장 높은 문자열을 
#     출력하는 함수를 구현하세요.

strArr = ["apple","ace","april"]

strArr.sort(reverse=False)
print(max(strArr),min(strArr))

# 14. 입력된 문자열에서 대문자는 소문자로, 소문자는 대문자로 변환하여 결과를 반환하는 
#     함수를 구현하세요.
#     (예: ‘GooD’  ==> ‘gOOd“)

str = "aPPle"
str = list(str)
print(str)

for i in range(len(str)) :
    if str[i].islower() :
        print(str[i])
        str[i] = str[i].upper()

    else :
        str[i] = str[i].lower()

reult = "".join(s for s in str)

print(reult)