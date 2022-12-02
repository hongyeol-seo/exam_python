check = True
strNum =2 
endNum = 4
endNum2 = endNum + 1 
dan = 1 

while check :
    if check or strNum < endNum2:            
        if check and dan < 10 and strNum < endNum2:
            print(f'{strNum} * {dan} = {strNum * dan}')
            dan +=1
            continue
        
        elif check and dan == 10:
            print(f"==========")
            dan = 1
            strNum +=1
            continue

        else :
            print(check, dan, strNum)
            # print("b")
            check = False
            break
        
    continue