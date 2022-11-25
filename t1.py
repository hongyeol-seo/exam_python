# count = 0
# arr = list(range(100))

# #홀수만 찍어서 출력해라! 

# for idx in range(len(arr)):
#     print(f'for문 {idx}번째')
#     if not arr[idx] % 2:
#         continue
#     else :
#         print(arr[idx])



# def add(a, b=0,c=0):
#     print(a,b,c)
#     print("걸과 : ", a+b+c)

    
# add(3,5,7)


def saveInfo(**infos):
    print(type(infos),len(infos),infos)

#키워드 파라미터 함수 호출 방법 
#함수명(변수명 = 값, ...., 변수명 )
saveInfo(name="Hong")
saveInfo()
saveInfo(age=12, phone='010-222-1111',job='학생',loc="대구") #데이터의 의미와 값을, 같이 준다.

