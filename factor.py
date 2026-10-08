def factors(x):
    factor=[]
    banana = 1
    for i in range (1, x+1):
        if i == 0:
            banana = i+1 
        else:
            banana= i  
        if y % banana == 0 :
            factor.append(i)
    return(factor)



y= int(input("i reqiure a numerical value that is a integer, kind and generous human "))
print(factors(y))










