
# i = 5 
# temp = [[i, j, i*j] for j in range(1,10)]
# for i in temp:
#     print("{} * {} = {}".format(i[0],i[1],i[2]),end="\t")

msg = "921010-3234567"

headNum, EndNum = msg.split("-")

year = headNum[:2]
month = headNum[:4]
day = headNum[:6]
month = int(month)
day = int(day)

if int(year) > 22 :
    newYear = "19"+year

else :
    newYear = "20"+year

tail = int(newYear)%12
# newtail

if tail == 0:
    newtail = "원숭이"
elif tail == 1:
    newtail = "닭"
elif tail == 2:
    newtail = "개"
elif tail == 3:
    newtail = "돼지"
elif tail == 4:
    newtail = "쥐"
elif tail == 5:
    newtail = "소"
elif tail == 6:
    newtail = "호랑이"
elif tail == 7:
    newtail = "토끼"
elif tail == 8:
    newtail = "용"
elif tail == 9:
    newtail = "뱀"
elif tail == 10:
    newtail = "말"
else:
    newtail = "양"
    
if (month == 1 and day <= 20) :
    star = "물병자리"
elif month == 2 and day <= 18 :
    star = "물병자리"
elif month == 2 and day <=28:
    star = "물고기자리"
elif month == 3 and day <=20:
    star = "물고기자리"
elif month == 3 and day <=21 :
    start = "양자리"
elif month == 4 and day <=19 :
    start = "양자리"
elif month == 4 and day <=31 :
    start = "양자리"
elif month == 5 and day <=21 :
    start = "쌍둥이자리"
elif month == 5 and day <=21 :
    start = "쌍둥이자리"

    

#두자리가 00이면 20붙이고 00이 아니면 
#22 보다 크면 