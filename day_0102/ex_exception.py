# ------------------------------
# 예외처리
# ------------------------------
# 실행 중 발생되는 오류로 프로그램이 중단되는 것을 막아주기 위한 방법 
import logging

logger = logging.getLogger()

num1 = 10

try:
    num2 = int(input("숫자 입력"))
    print(f'{num1}/{num2}={num1/num2}')
except Exception as e:
    print("에러",e)
    # 오류무시
    logging.error(e)   

finally :
    print("그냥 실행")
    #문제가 있든 말든 오픈 된 파일을 닫아야 하는 경우
    # if fp : #파일이 열려있다면 
    #     fp.close() 
print("========END=========")


# ValueError: invalid literal for int() with base 10:
# ZeroDivisionError: division by zero


# try:
# 	f = open(file_name,'w')
# 	data = dict_input['data']
# 	f.write(data)
# 	f.close()
# except KeyError:
# 	print('Key not found')
# except (FileNotFoundError, TypeError) :
# 	print('Could not open file')
# except:
# 	print('other error')
