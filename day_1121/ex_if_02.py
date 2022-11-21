# 다양한 조건문 ------------------------
# [실습] : 해당 점수가 합격/불합격/대기 인지 출력하세요
# 80점 이상 합격 / 70점 이상이면 대기 / 나머지는 불합격/ 

score = int(input("점수를 입력해주세요 : ").strip())

if score >= 80 :
    print(f'{score}점은 합격입니다.')

elif score >= 70 :
    print(f'{score}점은 대기입니다.') 

else :
    print(f'{score}점은 불합격입니다.') 
    
"d".upper