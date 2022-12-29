# dan = 5 

# [print(dan, "*", n , "=", dan*n, end="\n" if n == 5 else "   ") for n in range(1,10)]

# for num in range(1,10):
#     # print(f'----{dan}단-----',end="   ")

#     for dan in range(2,10):
#             print(f'{dan} * {num} = {dan*num:02}',end="\n" if dan == 9 else "    ")

# [print(f'{dan} * {num} = {dan*num:02}',end="\n" if dan == 9 else "    ") for num in range(1,10) for dan in range(2,10)]

def addDate(*data):
    if len(data) > 0 :
        num = 0
        for i in data:
            num += i
                                                                                                                                                                                                                                                                   
        # else : 
        #     return None
        
        return num

# def addDate(*nums):
#     total = 0
#     for num in nums :
#         total += num

#     return total if len(nums)>0 else None
#     #조건부 표현식

print(addDate())
print(addDate(1,3,5))
print(addDate(True, True, False, False, True))
print(addDate(0.9, 12.4, 4.1))
