

# # dan = input("단을 입력해주세요 : ").strip()
# # if len(dan)>0:
# #     dan=int(dan)
# #     for n in range(1,10):
# #         print(f'{dan} * {n} ={dan*n}',end="\t")

# # #
 
# # for i in range(2,10) :
    
# #     print(f'{i} 단')
# #     for j in range(1,10) :
# #         print(f'{i} * {j} = {i*j:2}',end="\t")
    
# #     print("")
# # #
# i = 0
# while i < 10:
#     i += 1
#     if i % 2 ==0:
#         continue
#     print(i)

number = [1,2,3,4,5]

result = [i*2 for i in number if not i%2]
print(result)
