# 횟수가 정해져있다면 for문
# 횟수가 정해져있지않다면 while문

# while 반복문
# -반복의 횟수가 고정이 아닌경우 사용하는 반복문
# -단순 카운팅용 반복문
# -필수조건] 반복을 중단할 수 있는 코드 필수
# -무한반복문
# -반드시 반복을 종료할 수 있는 코드 또는 업데이트 필수
# while 1:
#     print("1")

# while 반복문 - (1) 반복 카운팅 ----------------------
# 20번 "Hello world"

count = 1 #다운카운팅, 업카운팅

while count <= 20 : 
    print("Hello world")
    count+=1

#for문

for n in range(20) :
    print('Hello world') #카운팅하려고 넣는 n이기 때문에

# break -> for/while 반복문에 반복을 중단시키는 키워드
# 1부터 100까지 숫자를 하나씩 더해서, 덧셈에 결과가 71이 될때까지만 더해주세요.

count = 0
sum = 0

while count <= 100 :
    sum += count
    if sum < 72 : count += 1 #실행되는 구문이 하나밖에 없을때는 옆에 적으면 됩니다.
    else:
        print(sum)
        print(count)
        break

total = 0 
for num in range(1,101):
    total = total+num
    if total>= 71 : break

# continue 계속해서 -> for/while 반복문에서 아래 코드를 실행하지 않고 제일 위의 코드로 돌아갑니다.

# 1부터 20까지 출력하세요. 20에서 2의 배수만 빼고 출력하세요.

num = 0

while num <= 20:
    num = num + 1 #
    if not num%2 : continue
    print(num)

isEnd = False

for n in [1,2,3]:
    if isEnd : break
    for n2 in [11,22,33]:
        if n2 >= 20 :break
        isEnd = True
        print(n2) #그렇지 않다면?

    print(n)


for value in range(50):
    if value%2==0:
        continue

print(f"value : {value}")

#책 예저! 

i = 0
while i < 10:
    i += 1
    if i % 2 ==0:
        continue
        print(i)