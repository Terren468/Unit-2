def space( n,y,t):
    output = 0 
    for i in range(n):
        if y[i] =="C" and t[i]== "C":
                output +=1 
                print(output)
        
space ( 5,"CC...", ".C...")