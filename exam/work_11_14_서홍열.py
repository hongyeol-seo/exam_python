# ➀ 아래 데이터를 jumsu라는 변수명으로 저장해 주세요.
jumsu = [98,71,90,82,88]

# ➁ “Good Luck Happy New Year” 단어로 나누어 리스트로 저장하세요. #  그리고 개수와 데이터를 출력하세요.
msg = 'Good Luck Happy New Year'
newMsg = msg.split(" ") #리스트 형태로 반환
print('newMsg 갯수 : {}, 데이터 : {}'.format(len(newMsg),newMsg))

#  ➂ 중간고사 5과목 점수를 입력 받아 점수별로 구성된 리스트로 저장하세요. / #  input()함수는 1번만 사용하세요.

# list = ["국어", "영어", "수학", "사회", "과학"]
# score = []
# for i in range(len(list)) :
#     score.append(int(input("{} 점수를 입력하세요 : ".format(list[i]))))
        
# print(f'과목 : {list}')
# print(f'점수 : {score}')

# jumsu=input("중간고사 5과목 점수 입력(예: 90, 90, 90, 80, 90) ")
# jumsu=jumsu.split(',')
# jumsu[0]=int(jumsu[0])
# jumsu[1]=int(jumsu[1])
# jumsu[2]=int(jumsu[2])
# jumsu[3]=int(jumsu[3])
# jumsu[4]=int(jumsu[4])
# print(f'최고점수 : {max(jumsu)}, 최저점수: {min(jumsu)},
# 평균: {sum(jumsu)/len(jumsu)}'

#  ④ [1,3,5,7,9,11]를 [1,3,5,7,9,11,13,15]가 되도록 리스트를 확장시켜주세요. 
list = [1,3,5,7,9,11]
list += [13,15] #다른 닶
# list.extend([13,15])
print(list)

#  ⑤ 리스트 [1,3,5,7,9,11]에서 데이터 5를 꺼내는 코드를 작성하세요. 

newList = [1,3,5,7,9,11] #이건 꺼내는게 아니다!? .pop(2)
print(newList[2])

# ⑥ [ ‘kiwi’, ‘banana’. ‘orange’, ‘apple’ ]을 내림차순으로 정렬해주세요. 
strSort = ['kiwi', 'banana', 'orange', 'apple']
strSort.sort()
print(strSort) #오름차순
strSort.sort(reverse=True)
print(strSort) #내림차순

# ⑦ [10, 20, 30, 15, 20, 40]을 뒤집어서 역순으로 출력하세요.
strReverse = [10, 20, 30, 15, 20, 40]
strReverse.reverse()
print(strReverse
)
# ⑧ 비어있는 리스트에 사용자로부터 좋아하는 숫자 3개 입력 받아 저장하는 코드를 작성해 주세요.

# list = []
# for i in range(3) : 
#     list.append(input("좋아하는 단어를 입력해주세요 : "))

# print("입력숫자 {}".format(list))

# ⑨ [1,2,3,4,5,6] 리스트의 모든 요소를 삭제하는 코드를 작성해 주세요. (슬라이싱과 메서드 2가지 방법)

list = [1,2,3,4,5,6]

#슬라이싱
list[:] = []
print(list)

#메서드
del list[:] 
print(list)

#  
# ⑩ [1,2,3,4,5,6] 리스트에 2번째(인덱스) 위치에 100 추가, 제일 마지막에 200을 추가하는 코드를 작성해 주세요. append 메서드 사용하지 마세요.
list = [1,2,3,4,5,6]
list[2] = 100
list.extend([200])
print(list)

#   ⑪ [“Good’, 32, False, 8.91, ‘A’, 32 ]에서 8.91의 인덱스를 출력하세요. #  데이터 32를 모두 삭제해 주세요.
list = ['Good', 32, False, 8.91, 'A', 32 ]
print("8.91의 인덱스 : {}".format(list.index(8.91)))
list.remove(32)
print(list)

# ⑫ ['가나다', '한글', '가방', '국가', '쏘핫'] 에서 최대값, 최소값, 개수 출력하는 코드 작성하세요. 
strList = ['가나다', '한글', '가방', '국가', '쏘핫']
print(f'최대값 : {max(strList)} ') #최대값
print(f'최소값 : {min(strList)} ') #최대값
print(f'최대값 : {len(strList)} ') #최대값

# ⑬ 1~10000범위에서 3의 배수만으로 구성된 리스트를 생성하세요. 
# i/3 = 
list = []
for i in range(10000) :
    if i%3 == 0 :
        list.append(i)
        # continue
print(list)

# ⑭ 사용자로부터 숫자 2개를 입력 받아서 해당 숫자 범위의 데이터로 리스트를 생성하세요.

intX = int(input("첫 번째 숫자를 입력해주세요 : "))
intY = int(input("두 번째 숫자를 입력해주세요 : "))

list = [] 

if intX > intY : 
    for i in range(intY,intX+1) : 
        list.append(i)
    
else :
    for i in range(intX,intY+1) : 
        list.append(i)

print(list)
