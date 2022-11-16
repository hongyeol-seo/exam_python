# ➀ 아래 데이터를 jumsu라는 변수명으로 저장해 주세요.
jumsu = [98,71,90,82,88]

# ➁ “Good Luck Happy New Year” 단어로 나누어 리스트로 저장하세요. #  그리고 개수와 데이터를 출력하세요.
msg = 'Good Luck Happy New Year'
newMsg = msg.split(" ") #리스트 형태로 반환
print('newMsg 개수 : {}, 데이터 : {}'.format(len(newMsg),newMsg))

#  ➂ 중간고사 5과목 점수를 입력 받아 점수별로 구성된 리스트로 저장하세요. / #  input()함수는 1번만 사용하세요.

sublist = ["국어", "영어", "수학", "사회", "과학"]
score = []
for i in range(len(sublist)) :
    score.append(int(input("{} 점수를 입력하세요 : ".format(sublist[i]))))
        
print('점수 : {0}\n최고점수 : {1}\n최저점수 : {2}\n평균 : {3}'.format(score,max(score),min(score),int(sum(score)/len(score))))

#  ④ [1,3,5,7,9,11]를 [1,3,5,7,9,11,13,15]가 되도록 리스트를 확장시켜주세요. 
numlist = [1,3,5,7,9,11]
numlist.extend([13,15])
# list += [13,15] #다른 닶
print(numlist)

#  ⑤ 리스트 [1,3,5,7,9,11]에서 데이터 5를 꺼내는 코드를 작성하세요. 
newList = [1,3,5,7,9,11] #이건 꺼내는게 아니다!? .pop(2)
if 3 in newList : 
    nIdx = newList.index(3)
    print(newList.pop(newList.index(3)))
    print(f' pop 사용 후 newList : {newList}')

    # print(f' 인덱스 newList : {nIdx}')
    # print(f' pop 사용 전 : {newList}')
    # print(f' pop 사용 : {newList.pop(nIdx)}')
    

# ⑥ [ ‘kiwi’, ‘banana’. ‘orange’, ‘apple’ ]을 내림차순으로 정렬해주세요. 
strSort = ['kiwi', 'banana', 'orange', 'apple']
strSort.sort(reverse=True)
print(strSort) #내림차순

# ⑦ [10, 20, 30, 15, 20, 40]을 뒤집어서 역순으로 출력하세요.
strReverse = [10, 20, 30, 15, 20, 40]
strReverse.reverse()
print(strReverse)

# ⑧ 비어있는 리스트에 사용자로부터 좋아하는 숫자 3개 입력 받아 저장하는 코드를 작성해 주세요.

numlist = []

for i in range(3) : 
    numlist.append(input("좋아하는 숫자를 입력해주세요 : ").strip())

print("입력숫자 {}".format(numlist))

# ----------------다른 방법
num = input("좋아하는 숫자를 입력해주세요 : ex) \'20, 30, 40\'")
num = num.split(",")
numlist.append(num[0].strip())
numlist.append(num[1].strip())
numlist.append(num[2].strip())

print(numlist)

# ⑨ [1,2,3,4,5,6] 리스트의 모든 요소를 삭제하는 코드를 작성해 주세요. (슬라이싱과 메서드 2가지 방법)

numlist = [1,2,3,4,5,6]
#슬라이싱
numlist[:] = []
print(numlist)

numlist = [1,2,3,4,5,6]
#메서드
numlist.clear() 
print(numlist)

numlist = [1,2,3,4,5,6]
del numlist[:] #del 예약어
print(numlist)

  
# ⑩ [1,2,3,4,5,6] 리스트에 2번째(인덱스) 위치에 100 추가, 제일 마지막에 200을 추가하는 코드를 작성해 주세요. append 메서드 사용하지 마세요.
numlist = [1,2,3,4,5,6]
numlist.insert(2,100)
numlist.extend([200])
print(numlist)

#   ⑪ [“Good’, 32, False, 8.91, ‘A’, 32 ]에서 8.91의 인덱스를 출력하세요. #  데이터 32를 모두 삭제해 주세요.
strlist = ['Good', 32, False, 8.91, 'A', 32 ]
print("8.91의 인덱스 : {}".format(strlist.index(8.91)))
strlist.remove(32) #첫번째 32를 삭제
print(strlist)
# list.remove(32) 
strlist.pop() #뒤에서 삭제
print(strlist)


# ⑫ ['가나다', '한글', '가방', '국가', '쏘핫'] 에서 최대값, 최소값, 개수 출력하는 코드 작성하세요. 
strList = ['가나다', '한글', '가방', '국가', '쏘핫']
print(f'최대값 : {max(strList)} ') #최대값
print(f'최소값 : {min(strList)} ') #최대값
print(f'최대값 : {len(strList)} ') #최대값

# ⑬ 1~10000범위에서 3의 배수만으로 구성된 리스트를 생성하세요. 
print(list(range(1,10000, 3))) #변수명으로 list 금지! #'list' object is not callable

# list = []
# for i in range(10000) :
#     if i%3 == 0 :
#         list.append(i)
#         # continue
# print(list)

threeNums=list(range(3,10001, 3))
print(f'3의배수 리스트 : {threeNums}') #'threeNums' is not defined

# ⑭ 사용자로부터 숫자 2개를 입력 받아서 해당 숫자 범위의 데이터로 리스트를 생성하세요.

numList = [] 
numList.append(int(input("첫 번째 숫자를 입력해주세요 : ")))
numList.append(int(input("두 번째 숫자를 입력해주세요 : ")))

numList.sort()
print(numList)
print(f'리스트 : {list(range(numList[0],numList[1]))}')

# list = [] 

# if intX > intY : 
#     for i in range(intY,intX+1) : 
#         list.appen (i)
    
# else :
#     for i in range(intX,intY+1) : 
#         list.append(i)

# print(list)
