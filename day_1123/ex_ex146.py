#Q2. while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해보자.

arr = []

for i in range(1,1001) :
    if i%3 == 0:
        arr.append(i)

print(sum(arr))


num = 0
sum = 0 

while num < 1001 :
    if num % 3 == 0 :
        sum = sum + num
        num +=1
    num +=1

print(sum) 
        
#Q3 while문을 사용해서 별찍기

star = 0

while star < 6 :
    print("{:<5}".format("*"*star))
    star+=1

#05 for문을 사용하여 A학급의 평균점수를 구해보자
arr = [70,60,55,75,95,90,80,80,85,100]
sum = 0

for a in range(len(arr)):
    sum += arr[a]

print(f"평균 : {sum/len(arr)}")

#06 리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드가 있다.
number = [1,2,3,4,5]

result = [i*2 for i in number if not i%2] #이거뭐지!!!?? 
print(result)

