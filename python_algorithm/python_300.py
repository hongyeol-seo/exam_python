#007
print("naver","kakaotalk","samsung",sep=";")
#009
print("first",end="");print("Second")
#013
s = "hello"
t = "python"
print(s+"!",t)
#021
letters = 'python'
print(letters[0],letters[2])
#021
license_plate = "24가 2210"
print(license_plate[-4:])
#023
string1 = "홀짝홀짝홀짝"
print(string1[::2])
#024
string1 = "PYTHON"
print(string1[::-1])
#025
phone_number = "010-1111-2222"
print(phone_number.replace("-"," "))
#027
url = "http://sharebook.kr"
print(url[-2:])
# url_split = url.split('.')
# print(url_split[-1])
#029 
string1 = 'abcdfe2a354a32a'
print(string1.replace("a","A"))
#030
#replace 메서드를 사용하면 원본은 그대로 둔채로 변경된 새로운 문자열 객체를 리턴해줍니다.
string = 'abcd'
string.replace('b', 'B')
print(string)
#034
# t1 = 'python'
# t2 = 'java'
# print((t1,t2)*4)
t1 = "python"
t2 = "java"
t3 = t1 + ' ' + t2 + ' '
print(t3 * 4)
#035
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print("이름 {} 나이 {}".format(name1,age1))
print("이름 {} 나이 {}".format(name2,age2))

#038
arr =[]
상장주식수 = "5,969,782,550"
arr = 상장주식수.split(",")
arr[0] = int(arr[0])
arr[1] = int(arr[1])
arr[2] = int(arr[2])
arr[3] = int(arr[3])
print(arr)
#039
분기 = "2020/03(E) (IFRS연결)"
분기[:분기.index("(")]
#043
print('hello'.capitalize())

#044 
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))
#045 ★
file_name = "보고서.xlsx"
# string.endswith(value, start, end)
# print(file_name.endswith(("xlsx","xls",1,1)))

str = "this is string example....wow!!!"
print(str.endswith("is", 2, 6))
print(str.endswith("is", 2, 4))

s = '가나다라 마바사아 자차카타 파하'
s.endswith('라',0,4)
s.endswith('다라 ',0,5) #마지막 인덱스 포함

#046
file_name = "2020_보고서.xlsx"
print(file_name.startswith('2020'))

#047 #split() 기본값이 공백
a = "hello world"
a = a.split()
print(a)

#052
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
# movie_rank.append("배트맨")
movie_rank.insert(-1,"배트맨")
print(movie_rank)

#053
movie_rank = ["닥터 스트레인지", "스플릿", "럭키","배트맨"]
movie_rank.insert(1,"슈퍼맨")
print(movie_rank)

#054
# del movie_rank[3]
movie_rank.remove("럭키")
print(movie_rank)

#055
# 여러 값을 삭제할 때는 어떤 값이 먼저 삭제된 후 남은 원소들에 대해서 순서를 새로 고려한 후 삭제해야 합니다.
movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
del movie_rank[-2:]
print(movie_rank)

#061
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

#062
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[0::2])

#065
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0],interest[2])

#066
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']

print(" ".join(interest))

#068
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']

print('\n'.join(interest))

#069
string = "삼성전자/LG전자/Naver"
interest = string.split("/")
print(interest)

#070
data = [2, 4, 3, 1, 5, 10, 9]
# data.sort()
# print(data)
print(sorted(data))

#071
my_variable = ()
print(type(my_variable))

t = ('a', 'b', 'c')
t = ('A', 'b', 'c')
print(t)

#077
interest = ('삼성전자', 'LG전자', 'SK Hynix')
print(list(interest))

#078
interest = ['삼성전자', 'LG전자', 'SK Hynix']
print(tuple(interest))

#079 #튜플 언패킹
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(type(a), b, c)

#080
print(tuple(range(2,99,2)))

#081 #별표현식 
# 기본적으로 데이터 언패킹은 좌변의 변수와 우변 데이터 개수가 같아야 합니다. 하지만 star expression을 사용하면 변수의 개수가 달라도 데이터 언패킹을 할 수 있습니다. 튜플에 저장된 데이터 중에서 앞에 있는 두 개의 데이터만 필요할 경우 나머지 데이터의 언패킹 코드를 작성할 필요가 없습니다.

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

*c, _, _= scores
print(c) 
print(_)

ice = {"메로나": 1000, "폴라포": 1200, "빵빠레": 1800}
ice["죠스바"] = 1200
ice["월드콘"] = 1500
del ice["메로나"]


# ice.update(서홍열="남자",송명희="여자")
# print(ice)

#092
inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}

print(inventory.get("메로나","없으면 없다고말해")[0])
print(inventory.get("메로나","없으면 없다고말해")[1])

#094
inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}

inventory["월드콘"] = [500, 7]
inventory.update(월드콘 = [500,7])
# inventory.update({"서홍열":"남자"})
print(inventory)

#095
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}

arr = list(icecream.keys())

print(arr)

print(sum(list(icecream.values())))

#098
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}

icecream.update(new_product)
print(icecream)

#099
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)


#100
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]

close_table = dict(zip(date, close_price))
print(close_table)