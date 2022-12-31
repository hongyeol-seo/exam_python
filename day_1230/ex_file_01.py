import shutil
# ----------------------------------------
# 파일 입력과 출력 (I/O)
# 스트림(Stream) : 흐름 / 데이터의 흐름 / 데이터의 이동 통로
#                   입력 스트림/출력 스트림
# ----------------------------------------
# with ~ as 구문 / 데이터를 흘려보내는 (열었다가 닫았다가하는 곳에서)
# close 기능을 자동으로 해줌
#

FILE_NAME = "new_year.txt"

FILE_NAME1 = "new_new_year.txt"

# with open(FILE_NAME1, mode="r",encoding="utf-8") as f:
#     if f :
#         print("있다")
#     else :
#         print("없다")


# 파일 쓰기 w(덮어쓰기) / a(추가) / x(이미 존재하는 파일이면오류발생)
with open(FILE_NAME, mode="w", encoding="utf-8") as f:
    f.write("새해 복 많이 ~~ 검은 토끼\n")
    f.write("새해 복 많이 ~~ 검은 토끼\n")
    f.write("새해 복 많이 ~~ 검은 토끼\n")
    f.write("새해 복 많이 ~~ 검은 토끼\n")
    f.write("새해 복 많이 ~~ 검은 토끼\n")
    f.write("새해 복 많이 ~~ 검은 토끼\n")

# 파일 열기 r
# with open(FILE_NAME, mode="r",encoding="utf-8") as f:
#     # print(f.read())
#     for i in f.read():
#         with open(FILE_NAME1, mode="a",encoding="utf-8") as j:
#             j.write(i)

# 파일복사(copy)

# shutil.copyfile("new_year.txt", "./new_year3.txt")
# with open(FILE_NAME, mode="r",encoding="utf-8") as f:
#     if f :
#         print("있다")
#     else :
#         print("없다")

# shutil.copy("new_year.txt", "./test3.txt")
# shutil.copy2("new_year.txt", "./test4.txt")
# copyfile과 copy는 메타정보는 복사되지 않습니다.
# copy2는 메타정보도 복사합니다.
# 즉, copy2를 사용하면 파일을 작성한 날짜도 복사되지만 copyfile과 copy는 파일을 작성한 날짜가 복사한 날짜로 변경됩니다.


def copyFile(fileNmae):
    # 파일명 만들기
    _fileNmae = fileNmae.replace('.txt', '_1.txt')
    print(f'{_fileNmae}')

    # 방법1번
    # 파일 읽어서 새 파일에 쓰기
    # with open(fileNmae, mode="r",encoding="utf-8") as f:
    #     data = f.read()
    #     print(data)

    # with open(_fileNmae, mode="w",encoding="utf-8") as p:
    #     p.write(data)

    # #방법2번
    with open(fileNmae, mode="r",encoding="utf-8") as f1:
        with open(_fileNmae, mode="w",encoding="utf-8") as f2:
            lines = f1.readlines()
            for idx in range(1,len(lines)):
                f2.write(f"[{idx}]" + lines[idx-1])
            
            # p.write(f.read())

    # 방법3번 (실패)
    # count = 1
    # with open(fileNmae, mode="r", encoding="utf-8") as f:
    #     # data =
    #     # print(data)

    #     while True:

    #         with open(_fileNmae, mode="w", encoding="utf-8") as p:
    #             if not  f.readline():
    #                 break
    #             # print()
    #             p.write(f'{count} : {f.readline()}')
    #             count += 1

    # 복사본에는 줄 번호를 달아주세요.


copyFile(FILE_NAME)
