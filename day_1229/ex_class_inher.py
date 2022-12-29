# 자바는 다중상속이 안되는 반면, 파이썬은 다중 상속이 된다. play play play  라ㅓ는 메소드를 가지고 있느 클래스라면 제일 앞에 껏을 상속한다.

class A :

    def __init__(self,aa) -> None:
        self.aa = aa
        print("A_init()")

    def play(self):
        print(f'{self.aa}하면서 놀고 있다')
class B :

    def __init__(self,bb,number):
        print("B_init()")
        self.bb= bb
        self.number= number

    def play(self):
        print(f'{self.bb}신나 신나')

    def run(self):
        print("뛴다")

class C(A,B):
    pass

class D(B,A):
    pass

class E(C):
    pass

c1 = C("영웅")
c1.play()

d1 = D("영웅","123")
d1.play()

d2 = E("GGGG")
print(d2.aa)
print(d2.run())
# print(d2.bb)
