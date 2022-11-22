n = 100
divisors = []

for i in range(1, n+1):
    if n % i == 0 :
        divisors.append(i)

divisors.sort(reverse=True)

print(divisors)
