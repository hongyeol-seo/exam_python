# for n in range(0, 81):
#     num, dan =(n//9)+1, (n%9)+2
#     if num != 10 and dan != 10:
#         print(f'{dan:^3}*{num:^3}= {dan*num:02}', end='\n' if dan==9 else '  ')

# [print (f'{(n%9)+2:^3}*{(n//9)+1:^3}= {((n%9)+2)*((n//9)+1):02}', end='\n' if ((n%9)+2)==9 else '  ') for n in range(81)  if ((n%9)+2)!=10 and ((n//9)+1)!=0]
        
# star={'a':range(100, 200), 'b':range(201, 301)}

# print(star.values())

# for st in star.values():
#     print(st, 101 in st)

# -  1월 20일 ~  2월 18일 : 물병자리    	 2월 19일 ~  3월 20일 : 물고기자리
#    3월 21일 ~  4월 19일 : 양자리		    4월 20일 ~  5월 20일 : 황소자리
#    5월 21일 ~  6월 21일 : 쌍둥이자리	    6월 22일 ~  7월 22일 : 게자리
#    7월 23일 ~  8월 22일 : 사자자리		 8월 23일 ~  9월 23일 : 처녀자리
#    9월 24일 ~ 10월 22일 : 천칭자리		10월 23일 ~ 11월 22일 : 전갈자리
#   11월 23일 ~ 12월 24일 : 궁수자리		12월 25일 ~  1월 19일 : 염소자리
  
stars={ range(120, 219):'물병자리', range(219,321):'물고기자리', range(321, 419):'양자리',
        range(420, 521):'황소자리', range(521,622):'쌍둥이자리', range(622, 723):'게자리',
        range(723, 823):'사자자리', range(823,924):'처녀자리', range(924, 1023):'천칭자리',
        range(1023, 1123):'전갈자리', range(1123,1225):'궁수자리'}
  
def getMyStar(birth):
    my_star='염소자리'
    for key, value in stars.items():
        if birth in key: 
            my_star = value
            break
    return my_star

print('1225 => ', getMyStar(1225))
print('101 => ', getMyStar(101))
print('119 => ', getMyStar(119))    
print('623 => ', getMyStar(623))
print('123 => ', getMyStar(123))    
