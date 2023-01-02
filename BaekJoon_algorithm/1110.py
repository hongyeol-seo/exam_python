n = int(input("숫자 입력 : ").strip())
strNum = n
count = 0

while True :

    x = n//10 #십의자리
    y = n%10 #일의자리
    sum = x + y 
    z = str(x)+str(y) #합계
    z = int(z)
    if z == strNum :
        print(z)
        print(count)
        break
    count += 1 
    n = y+z
