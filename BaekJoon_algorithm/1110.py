n = int(input("숫자 입력 : ").strip())
strNum = n
count = 0

while True :

    x = strNum//10 #십의자리
    y = strNum%10 #일의자리
    z = (x + y)%10 
    strNum = (z * 10) + y

    count += 1
    if(strNum == n):
        break

print(count)

n = input()
num = n
cnt = 0

while 1 : 
    if len(num) == 1:
        num = "0" + num

    plue = str()