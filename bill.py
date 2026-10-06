bill = float(input("how much was the meal"))
tip = str(input("how was the service"))
tip_2= [0, 0.15, 0.20, 0.25]

if tip == "bad":
    print("your total is $", str(bill + bill* tip_2[0]))
elif tip=="okay":
    print("your total is $",str(bill + bill*tip_2[1]))
elif tip == "good":
    print("your total is $" ,str(bill + bill*tip_2[2]))
elif tip =="great":
    print("your total is $",str (bill + bill*tip_2[3]))