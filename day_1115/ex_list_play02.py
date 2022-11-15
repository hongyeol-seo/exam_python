# list 자료형 가지고 놀기
# [실습] 3과목 점수를 입력받고 합계, 평균 계산하여 출력
# 과목별 점수 입력 받기 -> input
# input 세번 

list = []
subject = ["국어","영어","수학"]

#데이터가 있는지 없는지를 봐야한다.

for i in range(len(subject)) :
    list.append(int(input("{}과목 점수를 입력해주세요".format(subject[i])).strip()))

print('\"합계\" : {}, 평균 : {}'.format(sum(list),sum(list)/len(list)))

