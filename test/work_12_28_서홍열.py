# 1. 계산기 프로그램을 클래스 기반으로 만들기
class Cal:
    def __init__(self, *data):
        self.nums = []
        for i in data:
            if i == int(i):
                self.nums.append(int(i))
            else :
                self.nums.append(i)
    def add(self):
        '''더하기'''

        return sum(self.nums)

    def mid(self):
        sum = 0 #(3,,4,5)
    
        for i in self.nums:
            sum -= i

        return sum

    def mul(self):
        sum = 1
        for i in self.nums:
            sum *= i
        
        return round(sum,2)

    def div(self):
        sum = 1
        for i in self.nums:
            sum /= i
        
        return round(sum,2)

cal1 = Cal(1,2,3,4)
cal2 = Cal(1.1,2.7,3,4)
cal3 = Cal(5,5.0)



print(f'+ 값 :',cal1.add())
print(f'- 값 :',cal1.mid())
print(f'* 값 :',cal1.mul())
print(f'/ 값 :',cal1.div())
print(f'--------------------------')
print(f'+ 값 :',cal2.add())
print(f'- 값 :',cal2.mid())
print(f'* 값 :',cal2.mul())
print(f'/ 값 :',cal2.div())
print(f'--------------------------')
print(f'+ 값 :',cal3.add())
print(f'- 값 :',cal3.mid())
print(f'* 값 :',cal3.mul())
print(f'/ 값 :',cal3.div())


# 2. 함수구현 
    #2-1 구구단 2-9단 출력 반복문 출력 1개
    
def gugudan(x,y):
    
    switch = 1
    strX = x
    endY = y
    n = 1

    while n != 10:
        
        if switch : 
            print(f'---{strX}---단',end="   ")
            if strX != endY:
                strX += 1
            else :
                strX = x
                switch = 0
                print()

        elif not switch:
            print(f"{strX} * {n} = {strX*n:02}",end="  ")
            if strX != endY:
                strX += 1
            else : 
                strX = x
                n += 1
                print()

gugudan(2,8)


#2-2 리스트 컨프리핸션

#첫번째방법
j = 5 #입력값
gugudan = [[j , i , j*i ] for i in range(1,10)]
for i in gugudan:
    print(f'{i[0]} * {i[1]} = {i[2]}', end="\n" if i[1] % 5 == 0  else "  ")
    

#두번째방법
dan = 5 
[print(dan, "*", n , "=", dan*n, end="\n" if n == 5 else "   ") for n in range(1,10)]

#2-3 별자리, 띠

def info(year,month,day,gender):

    star = ["",19,18,20,19,20,21,22,22,23,22,22,24]
    locStar = ["염소자리","물병자리","물고기자리","양자리","황소자리","쌍둥이자리","게자리","사자자리","처녀자리","천징자리","전갈자리","궁수자리","염소자리"]

    if star[int(month)] > int(day) :
        print(locStar[int(month)-1])

    else :
        print(locStar[int(month)])

    ganji = ["원숭이","닭","개","돼지","쥐","소","호랑이","토끼","용","뱀","말","양"]

    if int(gender) == 1 or int(gender) == 2:
        year = "19" + year
        print(ganji[int(year)%12])
        print(year)
    else :
        year = "20" + year
        print(ganji[int(year)%12])


data = "920413-1234578"
year,month,day,gender = data[0:2],data[2:4],data[4:6],data[7]
info(year,month,day,gender)