#201 ~ 204
def print_coin():
    print("비트코인")

for i in range(101):
    print_coin()

#215

def print_with_smile(msg):
    print(msg+":D")

print_with_smile("안녕하세요")

#220

def print_max(a,b,c):
    maxInt = a
    if b > a :
        maxInt = b
    if c > b and c > a:
        maxInt = c

#221
def print_reverse(msg):
    print(msg[::-1])

print_reverse("python")

#222

def print_score(arr):
    # sum = 0
    # for i in arr:
    #     sum += i

    # print(sum/len(arr))
    print(sum(arr)/len(arr))
print_score([1,2,3])

#223
def print_even(arr):
    for i in arr:
        if not i%2:
            print(i)

print_even([1, 3, 2, 10, 12, 11, 15])

#224
def print_keys(d):
    for keys in d.keys():
        print(keys)

print_keys({"이름":"김말똥", "나이":30, "성별":0})

#225
def print_value_by_key(a,b):
    print(a[b])

my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

print_value_by_key(my_dict, "10/26")

#226
def print_5xn(a):
    print(a[:5])
    print(a[5:])

print_5xn("아이엠어보이유알어걸")

#227
def printmxn(a,b):
    num = int(len(a)/b)
    for x in range(num+1):
        print(a[x*num:x*num+num])
printmxn("아이엠어보이유알어걸", 3)

#228
def calc_monthly_salary(a):
    print("{}".format(int(a/12)))

calc_monthly_salary(12000000)

#233
def make_list(a):
    arr = list(a)
    return arr
print(make_list("abcd"))

#234
def pickup_even(s):
    print(s[1::2])

pickup_even([3, 4, 5, 6, 7, 8])

#235 ★별표
def convert_int(n):
    arr = n.split(",")
    print(int("".join(arr)))


# def convert_int (string) :
#     return int(string.replace(',', ''))

convert_int("1,234,567")

#236
