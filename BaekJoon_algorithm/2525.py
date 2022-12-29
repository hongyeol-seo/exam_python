A, B = input().split()
A = int(A)
B = int(B)
C = int(input())

D = (B + C) // 60
E = (B+C)

if D :
    if (A+B) >= 24:
        print(0, E%60)
        
    else :
        print("1")
        print(A + D, E%60)


else:
    print("0")
    print(A,B+C)


# H, M = map(int, input().split())
# timer = int(input()) 

# H += timer // 60
# M += timer % 60

# if M >= 60:
#     H += 1
#     M -= 60
# if H >= 24:
#     H -= 24

# print(H,M)