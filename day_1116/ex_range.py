# -------------------------------------------
# range() #내장함수
# 정수의 범위를 만들어주는 함수
# -------------------------------------------
# 1~50 숫자로 구성된 리스트 객체를 생성하세요.
# 함수 사용법 range(시작번호, 끝번호, 간격) / 시작번호 이상 끝번호 미만 / 
# range() 함수 이해하기
nums = list(range(10))
# nums = (range(10),)
print(f'nums : {nums}')
print(f'타입 : {type(nums)}')

#리스트로 형변환을 하면 가능하다. set가능함 / 튜플은 안되나?

#1 부터 10까지 저장하는 리스트를 만들고 싶습니다
print(list(range(1,11)),type(list(range(1,11))))
print(set(range(1,11)),type(set(range(1,11))))
print((range(1,11),), type((range(1,11),))) 

#1~10 사이 숫자중에서 3의 배수로 리스트를 구성하고 싶다.

print(list(range(3,11,3)))

# 1 ~ 1000으로 구성된 리스트
print(list(range(1,1000)))
