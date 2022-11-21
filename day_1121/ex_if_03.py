#조건부 표현식

# 참인경우 if 조건문 else 거짓인경우
# print("odd number") if value%2 else print("even number")
# kind="Odd Number" if value%2 else "Even Number"
# num = 10
# print(1 if num > 0 else 0) #3항 연산자

num = 10

print("홀수") if (num % 2) else print("짝수")
#앞이면 1 뒤에는 0 

print(num % 2)

# [양수, 음수, 0을 식별해서 조건문을 조건부 표현식으로]


# print("1")if 5>10 else (print("2")if 10>5 else print(3))

n = 0
print("양수") if n > 0 else print("0") if n==0 else(print("음수")) #괄호를 적게되면 가독성이 떨어진다.

#함수 -> 클래스 ->
#아주 문법에 유하다. 배워야할 사람잆장에서는 배울게 많다.
