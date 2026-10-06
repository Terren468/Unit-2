bill = float(input( "how much was the meal"))
tip = input ("how was the service")
tip= [0, 0.15, 0.20, 0.25]

if tip == "bad":
    print ("your total is $", str(bill + bill* tip[0]))
elif tip=="okay":
    print ("your total is $",str(bill + bill*tip[1]))
elif tip == "good":
    print ("your total is $" ,str(bill + bill*tip[2]))
elif tip =="great":
    print ("your total is $",str (bill + bill*tip[3]))
