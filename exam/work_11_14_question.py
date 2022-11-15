# ⑬ 1~10000범위에서 3의 배수만으로 구성된 리스트를 생성하세요. 
print(list(range(1,10000, 3))) #변수명으로 list 금지! #'list' object is not callable

# list = []
# for i in range(10000) :
#     if i%3 == 0 :
#         list.append(i)
#         # continue
# print(list)

threeNums=list(range(3,10001, 3))
print(f'3의배수 리스트 : {threeNums}') #'threeNums' is not defined