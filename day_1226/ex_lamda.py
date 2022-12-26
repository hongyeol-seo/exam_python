# -----------------------
# 람다(lamda) 함수 : 익명함수, 1줄 함수
# 여기에서만 반복적으로 쓰이는 함수
# 짧은 코드의 함수
# 문법 형식 : lamda 인자 : 실행코드
# -----------------------
# 입력 받은 숫자를 모두 더해서 합계를 출력하는 코드
nums = input("원하는 수만큼 데이터를 입력해주세요.")

nums = nums.split()
#str  요소 => int 요소로 변환


for i in range(len(nums)):
    nums[i] = int(nums[i])

print('1 =>',nums)
# for j in enumerate(nums): #인덱스 값을 반환 
#     nums[j] = int(nums(j))

#리스트 컴프리핸션
nums = [int(n) for n in nums]
print('2 =>',nums)
#내장함수 => map(함수명, 반복가능객체) -> 반환값 map 객체

nums2 = list(map(str, nums))
print('3 =>',nums2)

#원래 있었던 값에 결과를 반환하는 함수
def threeNum(num):
    return num * 3 

nums4 = list(map(threeNum,nums))
print("4 ->", nums4)

nums5 = list(map(lambda n : n*3,nums)) #map 이랑 많이 씀
print("5 ->", nums4)

data = '1 2 3 4 5'
#str ---> list() 형변환 => 추가 작업 필요
print(list(data))

#str 클래스 -> 문자열을 나누어주는 기능
#리스트로 변환

data = data.split(",")
print(data)
