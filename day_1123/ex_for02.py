# 내포
# for 반복문 - 리스트 컨프리핸션(내포)
# 함수의 반환값을 받을때, 또 사용하게 되면 또 만들필요가 없다. / C언어를 꼭 배우라! 메모리 주소값가지고 하는 애들 / C가 필수였다. / 메모리체크 / 
# 걸리는 시간이랑 메모리 => 성능 / 이럴때 자료구조랑 알고리즘 고민해야한다.
# nums 리스트의 요소들을 nums2에 담겠습니다.
# 단, nums요소들의 값을 3을 곱한 값으로, 담아주세요.

# nums = [1,2,3]
# nums2 = []
# for n in nums :
#     nums2.append(n*3) 

# print(f'{nums2}')

# #단순 리스트와 for문
# nums3 = [n*3 for n in nums] 
# print(f'{nums3}')



nums = [1,2,3,4,5,6,7]
nums2 = []

#리스트와 for문과 조건문
# nums의 요소값이 짝수인것만 num2에 곱해서 넣어주세요.

for n in nums : 
    if not n%2 : 
        nums2.append(n*3)

print(nums2)


nums = [1,2,3,4,5,6,7]
nums3 = [n*3 for n in nums if not n%2]
print(nums3)


# ----------------------------

nums = [1,2,3,4,5,6,7]
nums2 = []

#list와 for문과 if문과 else
#짝수는 *3을하고, 홀수인것은 그대로 리스트에 추가

nums2 = [n if n%2 else n*3 for n in nums]
print(nums2) 

