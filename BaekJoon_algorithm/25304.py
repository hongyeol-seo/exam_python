x = int(input()) #금액
c = int(input()) #갯수
sum = 0
for i in range(c):
    a, b = map(int, input().split())
    sum += (a*b)

if x == sum :
    print("Yes")
else:
    print("No")