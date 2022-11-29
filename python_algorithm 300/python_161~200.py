#161
for i in range(100):
    print(i)

#162
for i in range(2002,2051,4):
    print(i)

#163
for i in range(0,31,3):
    print(i)

#164
for i in range(1,101):
    print(100-i)

#165
for i in range(10):
    print("0."+str(i))

# for num in range(10) :
#     print(num / 10)

#166
for i in range(1,10,2):
    print(f'3 * {i} = {3*i}')

#167
num = 0
for i in range(0,11):
    num+=i
    if i == 10 :
        print(num)

#168
num = 0 
for i in range(1,11,2):
    num+=i
    if i == 9 :
        print(num)

#170
mul = 1
for i in range(1,11):
    mul *= i

print(mul)

#171
price_list = [32100, 32150, 32000, 32500]

for idx in range(len(price_list)):
    print(price_list[idx])

#173
price_list = [32100, 32150, 32000, 32500]
for idx in range(len(price_list)):
    print(3-idx,price_list[idx])

# for i in range(len(price_list)):
#     print((len(price_list) - 1) - i, price_list[i])

#174
price_list = [32100, 32150, 32000, 32500]

for idx in range(len(price_list)-1):
    print((100+(idx*10)),price_list[idx+1])

# for i in range(1, 4):
#     print(90 + 10 * i, price_list[i])

#175
my_list = ["가", "나", "다", "라"]
for idx in range(1,4):
    print(my_list[idx-1],my_list[(idx)])

#176
my_list = ["가", "나", "다", "라", "마"]

for idx in range((len(my_list)-2)):
    print(my_list[idx],my_list[idx+1],my_list[idx+2])


#177
my_list = ["가", "나", "다", "라"]
for idx in range(1,len(my_list)):
    print(my_list[4-idx],my_list[3-idx])

#178
my_list = [100, 200, 400, 800]
for idx in range(1,len(my_list)):
    print(my_list[idx]-my_list[idx-1])

#179
my_list = [100, 200, 400, 800, 1000, 1300]
for idx in range(len(my_list)-2):
    print((my_list[idx]+my_list[idx+1]+my_list[idx+2])/3)

#180
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility=[]

for idx in range(5):
    volatility.append(high_prices[idx]-low_prices[idx])

print(volatility)

#184

stock = {"10/10":[80,110,70,90],"10/11":[210,230,190,200]}

#186
apart = [ [101, 102], [201, 202], [301, 302] ]

for i in apart:
    for j in i :
        print(str(j)+"호")

#187
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart[::-1]:
    for j in i :
        print(str(j)+"호")

#188
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
    for j in i:
        print(j,"호")
        print("----")

#189
count = 0
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
    count += 1
    for j in i:
        if count == 1 :
            print(j,"호")
            count = 0
        else :
            print(j,"호")
            print("-"*5)

# for row in apart:
#     for col in row:
#         print(col, "호")
#     print("-----")

#190
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart :
    for j in i:
        print(j,"호")

print("-"*5)

#191
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

# for i in data:
#     for j in i :
#         print("{}".format((j*0.014)+j))

for line in data:
    for column in line:
        print('{:.2f}'.format(column * 1.00014))

#192

for line in data:
    for column in line:
        print('{:.2f}'.format(column * 1.00014))
    print("-"*5)

#193
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

arr = []
for line in data:
    for column in line:
        arr.append(column * 1.00014)
print(arr)

#194 ★별표
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

arr = []
for i in data:
    sub = []
    for j in i :
        sub.append(j * 1.00014)
    arr.append(sub)
print(arr)

#195
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for i in ohlc[1:]:
    print(i[-1])    
#196
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for i in ohlc[1:]:
    if i[-1] > 150 :
        print(i[-1])

#197
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for i in ohlc[1:]:
    if i[-1] >= i[0] :
        print(i[-1])

#198
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

volatility = []

for i in ohlc[1:]:
    volatility.append(i[1]-i[2])

print(volatility)
#199

ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for i in ohlc[1:]:
    if i[3] > i[0] :
        print(i[1]-i[2])

#200
arr = []
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]

for i in ohlc[1:]:
    sum.append(i[3]-i[0])

print(sum(arr))