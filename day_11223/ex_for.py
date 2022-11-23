# 숫자 1부터 50까지 화면에 세로 방향으로 출력

nums = list(range(1,51))

# #한줄에 5개
# for i in range(len(nums)) :
#     if i%5 == 0 :
#         print(i, end="\n")

#     else :
#         print(i, end="\t")

#한줄에 7개
for i in range(1,51) :
    if i%2 == 0:
        print(i, end="\n")
    else:
        print(i, end="\t")


#값으로접근
#인덱스로접근

#한줄에 5개

for i in range(2,10) :
    
    print(f'{i} 단')
    for j in range(1,10) :
        print(f'{i} * {j} = {i*j:2}',end="\n")
    
    print("")