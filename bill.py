bill = int(input( "how much was the meal"))
tip = input ("how was the service")
tip= [0, 0.15, 0.20, 0.25]
total= (bill + bill*tip) 

if tip == "bad":
    print (total (bill + tip[0] ))
elif tip=="okay":
    print( total (bill + tip[1]))
elif tip == "good":
    print(total (bill + tip[2]))
elif tip =="great":
    print (total(bill + tip[3]))
