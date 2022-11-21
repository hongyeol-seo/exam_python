nums = [16,3,7,9,12]
nums1 = [16,3,7,9,12]


num = input("숫자를 입력해주쇼 : ").strip()

if num.isdecimal():
    num = int(num)

    if num in nums :
        print(f"{num}는 이미 존재합니다.")

    elif (num > min(nums)) and (num < max(nums)):
        # print(num)
        # print(min(nums))
        # print(max(nums))
        print(f'{num}는 최소값 {min(nums)}보다 크고, 최대값 {max(nums)}보다 작으므로 리스트에 추가합니다.')
        nums.append(num)

else :
    print(f'{num}는 숫자가 아닙니다.')
print(nums)


# 존재하지 않으면 숫자를 추가해주세요.
# 단 가장 작은 값보다 크고, 가장 큰 값보다 작은 경우에만 추가해주세요