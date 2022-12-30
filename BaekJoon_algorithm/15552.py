import sys

c = int(sys.stdin.readline().rstrip())
for i in range(c):
    a,b = map(int,(sys.stdin.readline().rstrip().split()))
    print(a+b)
