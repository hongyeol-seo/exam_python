# set 
# 아래 문자열에서 중복 알파벳을 제거 후 저장하기

msg = "merrychristmas Happy new year"
msg = msg.replace(" ","") #공백제거
data= set(msg)

#set 자료형에 요소 추가하기 set.add()


# data.add() #문자열! #이터러블 /= 쪼개져서 갈 수 있다./ string 같은 경우에는 쪼개지 않고
print(data)

# set 자료형에 여러개의 요소 추가하는 메소드
data.update(["a","Happy"]) #string을 interable 타입으로 입력해라! 
print(data)

nums = {1,4,2,3} #set자료형 #셋의 데이터 타입을 보고 할 수가 없다.
nums.add("ㄴ")
nums.remove(4) 
print(nums)
print(nums.pop()) #요소꺼내는는 셋 # 제일 먼저 인서트 된 애가 사라짐

nums.update([5,24,5]) #리터러블 인스를 넣어다랄
str = {"gk","하"}
# str.add()
# str.update()

#이런 요소들을 파악하기 위해서 지우든가, 말던가...

nums = {1,4,2,3} #
nums.pop(1)
print(nums)
nums2 = [1,4,2,3]
nums2.pop(1) #
print(nums2)

#멤머연산자 


