class a :
    LOC = "부산"

    def __init__(self) -> None:
        pass
    
    def showinfo(self):
        print(f'{self.LOC}에 갑니다.')

class b :
    LOC = "대구"

    def __init__(self) -> None:
        self.__showinfo()

    
    def __showinfo(self):
        print(f'{self.LOC}에 갑니다.')


def doit(self):
    self.showinfo()


a1 = a()
b1 = b()

doit(a1)
# doit(b1)
    