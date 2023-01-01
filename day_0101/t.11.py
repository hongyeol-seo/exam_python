
FILE_NAME = "testfile.txt"

with open(FILE_NAME, mode="r", encoding="utf-8") as f:
    # print(f.readlines())
    data = f.readlines()
    

    for i in f.readlines():
        print(i, end="")
