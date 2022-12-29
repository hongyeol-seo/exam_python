# -------------------------------------
# 상속
# -------------------------------------

# -------------------------------------
# 선생님을 나타내는 데이터 타입 =>
# 속성 / 필드
    #과목
    #나이
    #이름
    #학교(소속)
    #경력
    #담임여부
# 메서드
    #가르친다.
    #퇴근한다.
    #등수를 메긴다.
    #공부한다.
    #담임지도를한다.
    #생활기록부를 작성한다.
    #학부모상담을한다.
# -------------------------------------

# -------------------------------------
# 학생을 나타내는 데이터 타입 =>
# 속성/필드
    #이름
    #학교
    #학년
    #반
    #성적/등수
    #듣는수업수
# 메서드
    #공부한다.
    #학교에온다/간다
    #시험을본다
    #수업시간에존다
    #시험성적을보고좌절한다
    #소풍을간다
    #야자를한다.
# -------------------------------------

class man :

    def __init__(self, name):
        self.name = name

    def sleep(self):
        print(f'{self.name}는 ★개꿀잠★을 잔다')


class human(man) :
    
    def __init__(self,name,age,school):
        super().__init__(name)
        self.age = age
        self.school = school 

    def goToschool(self):
        print(f"{self.name}는 {self.school}에 간다")

    def study(self):
        print(f'{self.name}는 {self.name}은 공부를 한다')        

class teacher(human):
    
    def __init__(self, name, age, school,subject):
        super().__init__(name, age,school)
        self.subject = subject

    def teaching(self):
        print(f'{self.school} 학생을 가르친다')

    def hit(self):
        print(f'{self.school} 학생을 때린다.')


class student(human) :

    def __init__(self, name, age,school,grade,ban):
        super().__init__(name, age,school)
        self.grade = grade
        self.ban = ban
    
    def test(self):
        print(f"{self.name}은 {self.school} 시험을 본다.")

    def hit(self):
        print(f"{self.name}은 학교 폭력을 자행한다.")

t1 = teacher("홍길동",30,"대구고","수학")
s1 = student("임꺽정",20,"대구중","3학년","1반")

t1.goToschool()
t1.study()
t1.sleep()
t1.hit()

print("-----------------------")

s1.goToschool()
s1.study()
s1.test()
s1.sleep()
s1.hit()


# class test1 :

#     def __init__(self, age, name="홍열"):
#         self.name = name
#         self.age = age

#     def sleep(self):
#         print(f'{self.name}는 꿀잠을 잔다')

# class test2(test1):
    
#     def __init__(self,name):
#         super().__init__(name)

#     def showinfo(self):
#         print(f'{self.name}')
        
# tt2 = test1(30)
# tt2.sleep()
# # tt2.showinfo() 


class t1 :
    def __init__(self,x=7):
         self.x = x

class t2(t1):

    def __init__(self, x=7):
        super().__init__(x)

    # def __init__(self):
    #     super().__init__()

    def show(self):
        print(f"{self.x}")

tt2 = t2()
tt2.show() 


# -----------------------------
# 매개변수 => 값, 가변값, 키=값 가변, 디폴트값
# ----------------------------

def cal(num1,num2,op="-"):
    if op=="+":
        return num1+num2
    elif op == "-":
        return num1-num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1/num2 if num2 > 0 else '0으로 나눌 수 없습니다.'

print(cal(10,2,"*"))
print(cal(10,2))

#질문
# car1이 났다. 한번만 if하자 하고 바로 튀어나간다 .


def cal2(num1,num2,op="-"):
    if op=="+":
        return num1+num2
    if op == "-":
        return num1-num2
    if op == "*":
        return num1 * num2
    if op == "/":
        return num1/num2 if num2 > 0 else '0으로 나눌 수 없습니다.'

print(cal(10,2,"*"))
print(cal(10,2))