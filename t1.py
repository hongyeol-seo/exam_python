seven = list(range(0,101,7))
# 첫번째 버전
# for num in seven :
#     if num % 35 : #35의 배수 #5개씩 나오는거  #규칙을 찾아야한다.
#         print(num, end=" ")

#     else:
#          print(num, end="\n")

#seven의 인덱스를 하려고한다면

#두 번째 버전
for idx in range(len(seven)) :
    if idx % 5 ==4:
        print(seven[idx], end="\n")

    else :
        print(seven[idx], end="\t")

# 적어서보자!
# 0 1 2 3 4 
# 5 6 7 8 9 5라는게 관계가 있을때 5로 나누었을때 나머지가 4인애들
# 반복을 쓸 때는 유사하거나, 반복적인 것을 할 때 찾아낸다.
# 값으로 할 수도 있고, 정답을 알 수 있다.

#최대값 최소값

#4나 9로 나누었을때 0이면 되나요?