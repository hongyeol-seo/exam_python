#137

for i in [10,20,30]:
    print(i)

#138
for i in [10,20,30]:
    print(i)
    print("------")

#141
리스트 = [100, 200, 300]

for _ in 리스트 :
    print(_+10)

#143
리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for _ in 리스트 :
    print(len(_))

#144
리스트 = ['dog', 'cat', 'parrot']
for i in 리스트 : 
    print(i,len(i))

#145
리스트 = ['dog', 'cat', 'parrot']
for i in 리스트 :
    print(i[0])

#147
리스트 = [1, 2, 3]
for i in 리스트 :
    print(f'3 * {i} = {3*int(i)}')

#148
리스트 = ["가", "나", "다", "라"]
for i in 리스트[1:]:
    print(i)

#149
리스트 = ["가", "나", "다", "라"]
for i in 리스트[0], 리스트[-2]:
    print(i)

#150
리스트 = ["가", "나", "다", "라"]
for i in 리스트[::-1] :
    print(i)

#151
리스트 = [3, -20, -3, 44]
for i in 리스트[1:3] :
    print(i)

#152
리스트 = [3, 100, 23, 44]
for i in 리스트 :
     if i%3 == 0 :
        print(i)

#152
리스트 = [13, 21, 12, 14, 30, 18]
for i in 리스트 :
    if i < 20 and i%3 == 0 :
        print(i)

#153
리스트 = ["I", "study", "python", "language", "!"]
for i in 리스트 :
    if len(i) >= 3 :
        print(i)

#155
리스트 = ["A", "b", "c", "D"]
for i in 리스트 :
    if i.isupper() :
        print(i)

#157
리스트 = ['dog', 'cat', 'parrot']
for i in 리스트 :
    print(i.capitalize())

#158
리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
for i in 리스트 : 
    i = i.split(".")
    print(i[0])

#159
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트 :
    i2 = i.split(".")
    if "h" in i2[1] :
        print(i)

#160
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in 리스트 :
    i2 = i.split(".")
    if "h" in i2[1] or "c" in i2[1]:
        print(i)