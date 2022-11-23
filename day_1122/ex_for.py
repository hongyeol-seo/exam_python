# for 반복문 
# 유사하거나 동일한 코드를 줄여서 처리하는 문법

# msg = "Merry Christmas 2022"

# for i in msg :
#     print(i)

# 내장함수 print(재료) <- #매개변수, 파라미터

print(10,20,30,sep="*"); print(10,20,30)#실행을 했을 때, 기본값으로 sep이 공백값으로 잡혀있다. sep / \n 자동으로 줄바꿈이 되어있다.

# 1~1000숫자 중에서 7의 배수로 구성된 데이터
# 한 줄에 10개씩

seven = list(range(7,1000,7))
for num in range(0,len(seven)) :

    if num % 3:
        print(num, end="\t")
    else :
        print(num, end="\n")

    # if num % 10 == 9 :
    #     print(seven[num], end="\n")
    # else :
    #     print(seven[num], end="\t")

#한줄에 2개씩 찍기

# 9/10  num % 2 

# for num in range(len(seven)) :
# print(seven[num:num+7]) #
    
#7의 배수 데이터에 모든 원소 출력 

seven = list(range((0,101,7)))
for num in seven :
    print(num)
    # if num % 3:
    #     print(num, end="\t")
    # else :
    #     print(num, end="\n")

    # if num % 10 == 9 :
    #     print(seven[num], end="\n")
    # else :
    #     print(seven[num], end="\t")

seven = list(range(0,101,7))
for num in seven :
    if num % 35 : #35의 배수 #5개씩 나오는거  #규칙을 찾아야한다.
        print(num, end=" ")

    else:
         print(num, end="\n")

