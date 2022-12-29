# ------------------------------
# 파일 입출력
# ----------------------------

# 모드 (mode):
# mode w 파일이 존재하면 내용을 짖지우기 그리고 쓰기
# mode a 파일이 존재하면 끝부분에 내용 추가
# 파일이 없으면 새로추가 

FILE_NAME = 'mydata.txt'

fp = open(FILE_NAME, mode="w",encoding='utf-8')

fp.write("132465789")
fp.close()

# 모두 x로 파일 쓰기
# 존재하는 파일이면 오류 발생
# 존재하지 않는 파일이면, 파일 생성 후 쓰기
FILE_NAME = 'mybigdata.txt'
fp = open(FILE_NAME, mode="x",encoding='utf-8') #FileExistsError: [Errno 17] File exists: 'mydata.txt'

fp.write("132465789")
fp.close()

# a 존재하는 파일이면 끝부분에 a 추가
FILE_NAME = 'mybigdata.txt'
fp = open(FILE_NAME, mode="a",encoding='utf-8') #FileExistsError: [Errno 17] File exists: 'mydata.txt'

fp.write("하하하하하하하")
fp.close()