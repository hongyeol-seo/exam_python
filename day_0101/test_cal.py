# 사칙연산클래스
# 입력값받기


class Cal:

    a = "테스트 메시지"
    Cal_History = "cal_History.txt"
    f = open(Cal_History, mode="a", encoding="utf-8")

    def add(self, a, b):
        # Cal.f.write("입력")
        # Cal.f.close()
        # print(self.a)
        self.f.write("더하기입력")
        print("더하기 메소드")
        self.f.close()
        print(f'{a} + {b} = {a+b}')
        return a+b

    def sub(a, b):
        print(f'{a} - {b} = {a-b}')
        return a-b

    def mul(a, b):
        print(f'{a} * {b} = {a*b}')
        return a*b

    def div(a, b):
        print(f'{a} / {b} = {a/b}')
        return a/b

    def start(self):
        
        a = 0
        while True:

            Cal_History = "cal_History.txt"
            f = open(Cal_History, mode="a", encoding="utf-8")

            if not a:
                a = int(input("처음 숫자입력 : ").strip())  # 숫자입력

            x = input(f"연산자 입력:").strip()
            b = int(input("숫자입력 : ").strip())  # 숫자입력

            if x == "+":
                f.write(f'{a} + {b} = {a+b}\n')
                f.close()
                a = self.add(a, b)

            elif x == "-":
                f.write(f'{a} - {b} = {a-b}\n')
                f.close()
                a = sum(a, b)

            elif x == "*":
                f.write(f'{a} * {b} = {a*b}\n')
                f.close()
                a = self.mul(a, b)

            elif x == "/":
                if b == 0:
                    print("0으로 나눌 수 없습니다.")
                    continue
                else:
                    f.write(f'{a} / {b} = {a//b}\n')
                    f.close()
                    a = div(a, b)

            elif x == "=":
                f.write(f'= {a}\n')
                f.close()
                print("계산기를 종료합니다.")
                break

    def __init__(self, name):
        self.name = name
        print(f"{self.name}의 계산기를 시작합니다.")
        self.start()

c1 = Cal("홍열")
