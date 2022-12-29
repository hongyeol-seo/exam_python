# 파일 읽기 살펴보기
# ----------------------------------------

FILE_NAME = "mydata.txt"

fp = open(FILE_NAME, mode='r',encoding='utf-8')
allDate = fp.read()
fp.close()

print(type(allDate),allDate,len(allDate))


# readLines() 파일 내용을 줄(Line) 단위로 가져옴
fp = open(FILE_NAME, mode='r',encoding='utf-8')
allLInes = fp.readlines()
fp.close()

print(allLInes,len(allLInes))


fp = open(FILE_NAME, mode='r',encoding='utf-8')
# allLIne = fp.readline()

# for i in fp.readline():
#     print(i)

# fp.close()


# while True :
#     line = fp.readline()
#     print(line)
#     if not line : break


count = 1 
while True :
    line = fp.readline()
    if not line : break
    print(f'{count} : {line}')
    count +=1

# 더 이상읽을게 없어서, 처음으로 돌려야하기때문에 그때는 
#fp.seek()를 써서 처음으로 돌린다.


# print(allLIne,len(allLIne))

# 줄바꿈 자동이 아님
# raadline() => str
# read = > string
# readline 
