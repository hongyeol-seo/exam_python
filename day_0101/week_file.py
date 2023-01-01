FILE_NAME = "testfile.txt"
NULL_FILE_NAME = "null_file.txt"

with open(FILE_NAME, mode="w", encoding="utf-8") as f:

    for i in range(10):
        f.write(f'{[i] :} 새해 복 많이 받으세요.\n')

with open(FILE_NAME, mode="r", encoding="utf-8") as f:

    # readline()
    print(f'====readline()=====')
    while True:
        t = f.readline()
        if not t:
            print(type(t))
            if t == "":
                print("빈값")
            break
        print(t)

    # readlines() 사용
    print(f'====readlines()=====')
    f.seek(0)
    for i in f.readlines():
        print(i, end="")

    # read()
    f.seek(0)
    print(f'====read()=====')
    print(f.read())

# 파일복사

_filename = FILE_NAME.replace(".txt", "_1.txt")

# 방법1
# with open(FILE_NAME, mode="r", encoding="UTF-8") as f :
#     data = f.read()
#     with open(_filename, mode="w", encoding="UTF-8") as p :
#         p.write(data)

# 방법2
# with open(FILE_NAME, mode="r", encoding="UTF-8") as f :
#     data = f.readlines()
#     with open(_filename, mode="w", encoding="UTF-8") as p :
#         for i in data:
#             p.write(f'복사 줄 : {i}')

# 방법3
with open(FILE_NAME, mode="r", encoding="UTF-8") as f:
    with open(_filename, mode="w", encoding="UTF-8") as p:

        while True:
            data = f.readline()
            if not data:
                break
            print(data)
            p.write(f'readline을 활용한 {data}')