# 1. 3, 6, 9 게임을 파이썬으로 구현해 보세요.

n = int(input("숫자 입력 : ").strip())

for i in range(1,n+1):
    count = 0
    for j in str(i):
        if j == "3" or "6" == j or "9"==j:
            count += 1

    if count >= 1 :
        print("X"*count, end="\t")

    else :
        print(i,end="\t")

# 2. 고무 공을 100 미터 높이에서 떨어뜨리는데, 이 공은 땅에 닿을 때마다 원래 높이의 3/5 만큼 튀어오릅니다. 공이 열 번 튈 동안, 그때마다 공의 높이를 계산후 출력하세요.

for i in range(1,11):
    x = 100 #cm
    y = float(3/5)
    print("{}번째 높이 : {:.2f}m".format(i,x*(y**i)))

height = 100
jump = 3/5
i = 1

while i <= 10:
    height = height*jump
    print('{}번째 높이 : {:.2f}m'.format(i,height))
    i += 1

# 3. 산책을 하는 도중 심부름을 하게 되었습니다. 현재 가지고 있는 금액과 심부름으로 구매한 
#   제품가격을 입력 받으세요. 그리고 아래 2가지 결과를 출력해 주세요.
	# 3-1) ex) 거스름돈은 xxxx 원입니다.
	# 3-2) ex) 거스름돈으로 오천원 지폐는[    ]장, 천원 지폐는 [   ]장을 받았습니다.
#가지고 있는 금액 

#7600

remain =7600

오천원 = 0
천원 = 0

if remain / 5000 > 0 :
    오천원 = remain // 5000

elif remain / 1000 > 0 :
    천원 = remain // 1000

print("오천원 {오천원}")


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

second = 123456000

sec = 24 * 60 * 60 * 1000 #하루
si = 60*60 * 1000#시간
bun = 60 * 1000#분

#입력한 초를 일수로구한다.
day = second//sec #소숫점 이하는 버리는 1일
#입력한 초를 일수를 빼고 시수를 구한다.
second%=sec #37056
hours = second//si
second%=si
minutes = int(second//bun)
second%=bun
print("{}일, {}시, {}분, {}초".format(day, hours,minutes,second))


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


# 6. 1과 자기 자신만을 약수로 가지는 수를 소수(prime number)라 한다.입력받은 숫자 범위에서 소수만 출력하는 코드를 작성하세요.

n = int(input("정수를 입력해주세요 : "))

answer = []
for i in range(2, n+1) :
    count = 0
    for j in range(2, i+1):
        if(i%j==0):
            count += 1

    if count == 1 :
        answer.append(i)

print(answer)

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
# 피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 
# 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.
# 이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.
# n=17일때 까지 피보나치 수를 써보면 다음과 같다.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib(5)

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
print(str.swapcase())

# str = list(str)
# print(str)

# for i in range(len(str)) :
#     if str[i].islower() :
#         print(str[i])
#         str[i] = str[i].upper()

#     else :
#         str[i] = str[i].lower()

# reult = "".join(s for s in str)

# print(reult)

# 15. 아래 데이터를 저장 후 키에 따른 정렬 결과를 출력해 주세요.

arr = {"마징가":[187.5,91],"베트맨":[174.9,102.3],"홍길동":[192,72],'가가멜':[167.2,89.3]}

# arrkeys = list(arr.keys())

# a = (arr[arrkeys[0]][0],arr[arrkeys[1]][0],arr[arrkeys[2]][0],arr[arrkeys[0]][0])

# b= sorted(a)
# print(b)

arr.items()

print(sorted(arr.items(),key=lambda x : x[1]))

# 16. 1 이상의 자연수 n을 받았을 때 해당 수의 약수들을 구하는 함수를 구현하세요. 약수들은 리스트 형태로 숫자 크기 순서대로 출력합니다.

n = 100
divisors = []

for i in range(1, n+1):
    if n % i == 0 :
        divisors.append(i)

divisors.sort(reverse=True)

print(divisors)

# 17. 문자열에 대한 압축 알고리즘을 함수로 구현하세요.
#     컴퓨터에서 쓰이는 간단한 압축 알고리즘으로 Run-Length Encodig(RLE)방법은 예를 들
#     면 다음과 같다. “aaaaabbbccccccddddddddd” 문자열에서 반복되는 문자의 패턴을 찾
#     아 “a5b3c6d9”으로 표현한다. 문자열을 입력 받았을 때 RLE방법으로 구현된 값을 
#     반환하는 함수를 구현하세요.

# 문자열 `str`에 대해 실행 길이 인코딩(RLE) 데이터 압축 알고리즘 수행
# def encode(s):
 
#     encoding = "" #는 출력 문자열을 저장합니다.
 
#     i = 0
#     while i < len(s):
#         # 인덱스 `i`의 문자 발생 횟수
#         count = 1
 
#         while i + 1 < len(s) and s[i] == s[i + 1]:
#             count = count + 1
#             i = i + 1
 
#         # 결과에 현재 문자 및 해당 개수 추가
#         encoding += str(count) + s[i]
#         i = i + 1
 
#     return encoding
 
# if __name__ == '__main__':
 
#     s = 'ABBCCCD'
#     print(encode(s))

# 18. 문자열을 입력하면 UTF-8로 인코딩된 값을 출력된 함수를 구현해 주세요.
#     예) “가나다” => 0b10101100000000000b10110000100110000b1011001011100100

str = '가나다'
str = str.encode('utf-8')
print(str)

# 19. 양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 한다. 
#     어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램을 작성하시오.

#     [ 입력 ]
#     첫째 줄에 N의 진짜 약수의 개수가 주어진다. 
#     이 개수는 50보다 작거나 같은 자연수다. 
#     둘째 줄에는 N의 진짜 약수가 주어진다. 
#     1,000,000보다 작거나 같고, 2보다 크거나 
#     같은 자연수이고, 중복되지 않는다.

#     [ 출력 ]
#     첫째 줄에 N을 출력한다
    
#     (예 :  약수 개수 입력 :  2
#           약수 입력 : 2 3
#           결 과 :  6  )

x = int(input())
a = list(map(int, input().split()))
a.sort()
print(a[0]*a[-1])

# arr = list(map(int, input().split()))
# print(max(arr) * min(arr))
# 진짜 약수 중 최댓값과 최솟값을 곱하면 N을 구할 수 있다

# 그렇게 어렵지 않았던 문제이다. 진짜 약수들이 주어지면 그 약수들을 정렬하고, 맨 처음 진짜 약수와 맨 마지막 진짜 약수를 곱하면 N을 구할 수 있다.


# 20. 주사위 2개를 던졌을 때, 모두 짝수 또는 모두 홀수인 경우를 판별하는 프로그램을 
#     구현하세요. 그리고 승부여부, 동일여부도 출력하세요.

number = int(input("수를 입력하세요: "))

#입력받은 수에 2를 나눈 나머지가 1이면 홀수!
if number%2 == 1:
    print(number, "홀수 입니다.")
else:
    print(number, "짝수 입니다.")

# 21. 여러 단위의 동전들이 주어져 있을때 거스름돈을 가장 적은 수의 동전을 교환해주는 
#     코드를 작성하세요.
#     각 단위의 동전은 무한정 쓸 수 있다.
#     [ 입력설명 ]
#     첫 번째 줄에는 동전의 종류개수 N(1<=N<=12)이 주어진다. 
#     두 번째 줄에는 N개의 동전의 종류가 주어진다.
#     세 번째 줄에는 거슬러 줄 금액 M(1<=M<=500)이 주어진다.
#     각 동전의 종류는 100원을 넘지 않는다.
#     [ 출력설명 ]
#     첫 번째 줄에 거슬러 줄 동전의 최소개수를 출력한다.
#     ------- 예시 -------
#     ▣ 입력예제 1
# 	   	동전 종류 개수 : 3 
# 	    	동전 	  종류 : 1 2 5
# 	    	거스럼    금액 : 15
#     ▣ 출력예제 1
#     		거스럼 동전 개수 : 3
#     		설명 : 5 5 5 동전 3개로 거슬러 줄 수 있다.