# ----------------------------------------------------------
# 파일 입력과 출력 (I/O)
# 스트림(Stream) - 흐름 , 데이터의 흐름, 데이터의 이동 통로
#               - 종류 : 입력 스트림, 출력 스트림
# ----------------------------------------------------------
# with ~ as 구문
# - close 기능을 자동 실행 
# ----------------------------------------------------------
FILE_NAME='new_year.txt'

# 파일 쓰기(write) =====================================================
# mode  - w : 덮어쓰기  
#       - a : 추가
#       - x : 이미 존재하는 파일이면 오류 발생 , 존재하지 않는 파일만 가능
# ======================================================================
with open(FILE_NAME, mode='w', encoding='utf-8') as f:
    f.write("새해 복 많이 받으세요~~~2023 검은 토끼\n")
    f.write("새해 복 많이 받으세요~~~2024 용\n")
    f.write("새해 복 많이 받으세요~~~2025 뱀\n")
    f.write("새해 복 많이 받으세요~~~2026 호랑이\n")

# 파일 읽기(read) =====================================================
# mode  - r : 읽기
# ====================================================================
with open(FILE_NAME, mode='r', encoding='utf-8') as f:
    print(f.read())
 
# 파일 복사(Copy) 함수 ==================================================
# 조건 : 파일명 끝 부분에 숫자 추가
# 예시 : data.txt => data_1.txt, data_2.txt, ...
# ======================================================================   
def copyFile(filename):
    # 파일명 만들기
    _filename = filename.replace('.', '_1.')
    print(f'_filename : {_filename}')
    
    # 파일 읽어서 새 파일에 쓰기 - 방법 (1)
    with open(filename, mode='r', encoding='utf-8') as f:
        data= f.read()
        
    with open(_filename, mode='w', encoding='utf-8') as f:
        f.write(data)   
        
    # 방법 (2)
    _filename2 = _filename.replace('_1.', '_2.')
    with open(_filename, mode='r', encoding='utf-8') as f1:
        with open(_filename2, mode='w', encoding='utf-8') as f2:
            lines=f1.readlines()
            for idx in range(1, len(lines)+1):
                f2.write(f'[{idx}]'+lines[idx-1])
                

copyFile(FILE_NAME)

#copyFile('DAY_1230\ex_class_duck_type.py')