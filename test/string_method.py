a = "String"
b = "apple"
c = ""
# capitalize()	Converts the first character to upper case
print("apple".capitalize()) #string 앞글자만 대문자로

# casefold()	Converts string into lower case
print("APPLE".casefold()) #모든 문자열을 소문자로

# center()	Returns a centered string
"apple".center(30,"*") #가운데 정렬

# count() Returns the number of times a specified value occurs in a string
"apple".count("p") #요소 개수 파악

# encode()	Returns an encoded version of the string
"가".encode(encoding='UTF-8') #인코드로 변환

# endswith()	Returns true if the string ends with the specified value
"apple".endswith("a") #끝자리가 endswith의 요소값인지 아닌지

# expandtabs()	Sets the tab size of the string
"a\tpple".expandtabs(10) #tab사거리

# find()	Searches the string for a specified value and returns the position of where it was found
"apple".find("p") #요소의 인덱스값찾기
# find(찾을 문자, 찾기 시작할 위치, 찾기를 끝맺을 위치)


# format()	Formats specified values in a string
"{}".format("apple") #포멧스트링

# format_map()	Formats specified values in a string

print('Hi, {name}! I feel {feel}.'.format_map({'name':'hongyeol', 'feel':'happy'}))
#인자대신 딕셔너리로 사용

# index()	Searches the string for a specified value and returns the position of where it was found
'apple'.index("l")

# isalnum()	Returns True if all characters in the string are alphanumeric #모든 문자열이 영어, 한글 혹은 숫자로 되어있으면 참 리턴/ 특수기호 X
'apple사과123'.isalnum()

# isalpha()	Returns True if all characters in the string are in the alphabet
'안녕하세요'.isalpha() #모든 문자열이 string으로만 구성되어있으면, 숫자 있으면 안됨

# isascii()	Returns True if all characters in the string are ascii characters
'apple@#$#'.isascii() #아스키문자라면 True

# isdecimal()	Returns True if all characters in the string are decimals
'123'.isdecimal()

#주어진 문자열이 숫자로만 되어있는지 / 숫자러철 생긴애들중에 int형으로 형 변환이 되는 애들 '3²' 안됨

# isdigit()	Returns True if all characters in the string are digits
#숫자로만 이우러어져있는지?
'-123'.isdigit() #'-', 소수점을 뜻하는 '.' 이것들을 숫자가 아닌 문자로 판단을 하기 때문에 실수나 음수를 판단하지 못합니다.

# isidentifier()	Returns True if the string is an identifier
'123o'.isidentifier()
# 유효한 식별자이면 True 반환, 그 외는 False 반환.
# ※ 유효한 식별자 O 경우 : 영문(A~z), 숫자(0~9), _ 로만 구성.
# ※ 유효한 식별자 X 경우 : 숫자로 시작, 공백이나 특수문자 포함

# islower()	Returns True if all characters in the string are lower case
'apple'.islower() #모든 문자열이 소문자인지여부

# isnumeric()	Returns True if all characters in the string are numeric

'123'.isnumeric() #모든 문자열이 숫자인지?
# isprintable()	Returns True if all characters in the string are printable

'korea\njapn'.isprintable() #줄바꿈 문자 x
"\u0014".isprintable() #불가 유니코드

# isspace()	Returns True if all characters in the string are whitespaces

'     '.isspace() #모든 문자열이 공백이라면 true

# istitle()	Returns True if the string follows the rules of a title 
"Hello.World".istitle()
#문자열 안 각 단어의 첫 글자만 대문자이면 True 반환, 그외는 False 반환.

# isupper()	Returns True if all characters in the string are upper case
"APPLE".isupper() #모든 문자열의 대문자여부

# join()	Converts the elements of an iterable into a string
"".join(["H","e","l","l","o"]) #iterable 타입을 합치기

# ljust()	Returns a left justified version of the string
"apple".ljust(10,"/") #문자열을 왼쪽으로 숫자값만큼 정렬 빈칸은, 옵션값으로 채우기

# lower()	Converts a string into lower case
"APPLE".lower()  #문자열소문자로
# lstrip()	Returns a left trim version of the string
'     apple'.lstrip() #왼쪽공백제거
# maketrans()	Returns a translation table to be used in translations
#문자열 일부를 지정 문자로 대체 정의하는 매핑 테이블 생성.

a = "apple"
b = a.maketrans("pp","PP","le")
a.translate(b) #바꾸고싶은문자열, #바꿀문자열, #없앨문자열

# partition()	Returns a tuple where the string is parted into three parts

a = "Hello my name is HongYeol"
a.partition("is") #문자열을 맨 처음 일치문자열 기준으로 쪼개서 3개의 요소를 갖는 Tuple 생성. 

# replace()	Returns a string where a specified value is replaced with a specified value

'apple'.replace("a","b")
# rfind()	Searches the string for a specified value and 
print('안녕하세요. 만나서 반갑습니다.'.rfind("만",3))
print('안녕하세요. 만나서 반갑습니다.'.find("만",3))
#차이가 없나?

# returns the last position of where it was found

# rindex()	Searches the string for a specified value and returns the last position of where it was found

'apple'.rindex(a)

# rjust()	Returns a right justified version of the string
"apple".rjust(20,"*") #문자열을 오른쪽으로 숫자값만큼 정렬 빈칸은, 옵션값으로 채우기

# rpartition()	Returns a tuple where the string is parted into three parts

a = "Hello my name is HongYeol"
a.partition("is") #문자열을 맨 처음 일치문자열 기준으로 쪼개서 3개의 요소를 갖는 Tuple 생성. 

# rsplit()	Splits the string at the specified separator, and returns a list
"Hello/World/and/korea".rsplit("/",2) #오른쪽부터쪼개기


#오른쪽부터 문자열을 지정 구분자 기준으로 쪼개기 후 List 생성.

# rstrip()	Returns a right trim version of the string
'     apple         '.rstrip() #오른쪽공백제거

# split()	Splits the string at the specified separator, and returns a list

"Hello/World/and/korea".split("/") #문자 나누기

# splitlines()	Splits the string at line breaks and returns a list
"Hello\nWorld/and/korea".splitlines() #줄바끔 기호 기준으로 쪼개기

# startswith()	Returns true if the string starts with the specified value
"apple".startswith("a") #첫 문자열이 원소값으로 시작하는지

# strip()	Returns a trimmed version of the string
"Hello/World/and/korea".split("/",2) #왼쪽부터 쪼개기

# swapcase()	Swaps cases, lower case becomes upper case and vice versa
'Apple'.swapcase() #소문자는 대문자로, 대문자는 소문자로

# title() Converts the first character of each word to upper case
#문자열 내 띄어쓰기 기준으로 각 단어의 첫글자는 대문자로, 나머지는 소문자로 변환한다.

"HELLO WORLD".title()

# translate()	Returns a translated string
# 문자열 일부를 dictionay 또는 매핑 테이블에 설정된 값으로 변환 후,
# 변환된 문자열을 반환.

a = {104:  72}
b = "hello world"
print(b.translate(a))

"hello world".translate({104:  72})

# 예제1 - maketrans() 메서드 사용 시, 아스키 코드 사용 안 해도 됨.
# hz = "홈짱닷컴 homzzang.com"
# ch = hz.maketrans("h", "H")
# print(hz.translate(ch))


# upper()	Converts a string into upper case

'apple'.upper()

# zfill()	Fills the string with a specified number of 0 values at the beginning

'a'.zfill(5) 

# rjust()	Returns a right justified version of the string
#문자열을 숫자값만큼 할당하고, 빈것은 0으로 채우기

a = "Hello my name is HongYeol"
print(a.partition("name"))
print(a.rpartition("name"))
#질문! 