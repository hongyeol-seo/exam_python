a,b,c = map(int, input().split())

if a==b==c:
    print((a * 1000)+10000)
elif a in (b,c):
    print((a*100)+1000)
elif b in (a,c):
    print((b*100)+1000)
else :
    print(max([a,b,c])*100)
    

# a, b, c = map(int, input().split())

# if a == b == c:
#     print(10000+a*1000)
# elif a == b:
#     print(1000+a*100)
# elif a == c:
#     print(1000+a*100)
# elif b == c:
#     print(1000+b*100)
# else:
#     print(100 * max(a,b,c))