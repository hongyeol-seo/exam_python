# # 더하기
# # 빼기
# # 나누기
# #

# # 0으로는 나눌 수 없습니다.

# class operCal:

#     def __init__(self):
#         pass

#     def add(self):
#         print("더하기입니다.")


# class Cal():

#     def __init__(self):
#         super().__init__()
#         # self.add()

#     def add(x,y):
#         print(f'기존값{x}')
#         print(f'후행값{y}')
#         print(x+y)
#         return x+y

#     switch = 1
#     total = []
#     oper = ""

#     while switch:

#         if len(total) >= 1:
#             # 계산값출력
#             num1 = int(input("데이터를 입력해주세요.").strip())
#             if oper == "+":
#                 total = add(sum(total),num1)
                
#                 pass
#             elif oper == "-":
#                 pass
#             elif oper == "*":
#                 pass
#             elif oper == "-":
#                 pass
#             elif oper == "=":
#                 print(f"종료 : {sum(total)}")
#                 break

#         else:
#             # 입력받고
#             num1 = int(input("데이터를 입력해주세요.").strip())
#             oper = input("연산자를 입력해주세요.").strip()
#             total.append(num1)


    
#     # def __init__(self, *data):
#     #     self.nums = []
#     #     for i in data:
#     #         if i == int(i):
#     #             self.nums.append(int(i))
#     #         else :
#     #             self.nums.append(i)
#     # def add(self):
#     #     '''더하기'''

#     #     return sum(self.nums)

#     # # def mid(self):
#     # #     sum = 0 #(3,,4,5)

#     # #     for i in self.nums:
#     # #         sum -= i

#     # #     return sum

#     # def mul(self):
#     #     sum = 1
#     #     for i in self.nums:
#     #         sum *= i

#     #     return round(sum,2)

#     # def div(self):
#     #     # 나누기
#     #     sum = 1

#     #     for i in self.nums:
#     #         if i == 0:
#     #             print('0으로는 나눌 수 없습니다.')
#     #             break


#     #         sum /= i
#     #     return round(sum,2)
# c1 = Cal()
# print(c1)
