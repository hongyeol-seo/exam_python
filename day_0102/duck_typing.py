#자바의 인터페이스

class P:
    def fly(self):
        print("상속 받은 친구")

class Parrot(P):
    pass

class A :
    def fly(self):
        print("Airplane flying")

    def swim(self):
        pass

class Airplane(A):
    pass

def lift_off(entity):
    entity.fly()

parrot = Parrot()
airplane = Airplane()

lift_off(parrot) # prints `Parrot flying`
lift_off(airplane) # prints `Airplane flying`
