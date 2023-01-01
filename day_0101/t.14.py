# while True :
#     x = int(input())
#     if x in range(1,20):
#         print("있다")
#     else :
#         print("없다")


class test001:
    a = 5

    def show(self):
        print("show메서드")
        print(self.a)

    def info():
        print("클래스 메소드")

    def __init__(self) -> None:
        print("시작")
        test001.info()
        self.show()


t1 = test001()
# t1.show()


