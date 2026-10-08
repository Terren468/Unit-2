def gcf(num, Num): 
    num = input ("give me a number kind and generous sire ")
    Num = input ("give me another number kind and generous sire")
    factor=[]
    Factor =[]
    for i in range (1, num+1):
        num % i ==0 
    factor.append (i)
    for i in range (1, Num+1):
        Num % i ==0 
        Factor.append(i)
    return(factor, Factor)
print(gcf)