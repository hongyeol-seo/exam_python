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