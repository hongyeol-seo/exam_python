H, M = input().split()

H = int(H)
M = int(M) # + 15

if H < 24 and M > 45:
    print(H, M-45)

elif H == 0 and  M < 45 :
    print(23,M+15)

else :
    print(H-1,M+15)
