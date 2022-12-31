t = int(input())

# for i in range(1,t+1):
#     print("{:>5}".format("*"*i))

for i in range(1,t+1):
    print(" "*(t-i) + "*"*i)