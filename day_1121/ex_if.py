num = 0

if num : 
    print("True인 경우 실행되는 코드")

else :
    print("False".center(30,"-"))
    print("거짓".center(30,"-"))

print("END".center(30,"-"))

#짝수, 홀수구하기
# %2 가 0이라면 짝수, 그렇지 않다면 홀수

#[실습] 숫자를 입력받아서 해당 숫자가 3의 배수인지 아닌지를 출력해주세요.

num = int(input("숫자를 입력해주세요. : ").strip())

if num%3 == 0 :
    print(f'{num}은 3의 배수입니다.')

else :
    print(f'{num}은 3의 배수가 아닙니다.')


#숫자가 양수인지, 음수인지, 0인지 식별해서 출력하세요.
#다중조건

#조건문 안에 조건문 => 중첩 조건문
#if if 

#다중조건문
#if ~ 
#elif

