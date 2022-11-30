#리스트(배열) 원소의 합 구하기

def sum (n, S):
    result = 0
    for i in range(n):
        result = result + S[i]
    return result

S = [-1, 10, 7, 11, 5, 13, 8]
sum = sum(len(S), S)
print('sum =', sum)