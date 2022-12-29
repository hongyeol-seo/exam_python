# ------------------------------------------------------------
# 파일 읽기, 쓰기 => 파일 입출력 IO
# ------------------------------------------------------------
# (1) 열기 / 동작모드 mode = w 쓰기 / r 읽기 
# (2) 쓰기 & 읽기
# (3) 닫기 close
# ------------------------------------------------------------
# 파일쓰기

FILE_NAME = 'data.txt' #프로그램을 하다보면 안 바뀌는 데이터 => 상수 / 파이썬에는 상수가 없다. 
# FILE_NAME = ('data.txt',) #파일 이름 변경 안됨 / 튜플로 만든다면
# FILE_NAME = 'data',

# (1) 파일 열기(파일경로 + 파일명, 모드, 인코딩)
fp = open(FILE_NAME, mode='w',encoding='utf-8') 
# fp = open(FILE_NAME[0], mode='w',encoding='utf-8')  #튜플이라서

# (2) 쓰기 => write("데이터")
fp.write("Good\n") #적힌문자대로
fp.write("Happy")

# (3) 닫기
fp.close()

# 파일 읽기 ======================================
# (1) 파일 열기(파일경로 + 파일명, 모드, 인코딩)
fp = open(FILE_NAME, mode="r", encoding='utf-8')

# (2) 파일 읽기 => read() 파일 안에 모든 내용 가져오기==> str 타입
allContext = fp.read()

# (3) 파일 닫기
fp.close()

# (4) 파일 내용 확인
print(f'allContext => {allContext}')


# fp1 = open(r'day_1229\ex_class_03.py', mode="r", encoding='utf-8')
# fp1 = open(r'C:\Users\seo\Desktop\exam_python-1\day_1229\ex_file.py', mode="r", encoding='utf-8')
# fp1 = open("C:/Users/seo/Desktop/exam_python-1/day_1229/ex_class_03.py", mode="r", encoding='utf-8')

allContext = fp1.read()
fp1.close()
print(f'allContext => {allContext}')

