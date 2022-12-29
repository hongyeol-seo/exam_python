def gugudan(start_n,end_n):
    n = start_n
    k = 1
    switch = True
    
    while k != 10:
        if switch:
            print(f"--[{n}단]--",end='     ')
            n +=10
            if n==end_n+1: 
                switch = False; 
                n = start_n; 
                print()

        if not switch:
            print(f"{n}*{k}= {n*k:2}",end='       ')
            n +=1
            if n==end_n+1: 
                n = start_n; 
                k +=1; 
                print()

gugudan(2,4)                      