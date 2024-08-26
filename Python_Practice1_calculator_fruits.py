print("Type 1 for Accumulative Calculator. Type 2 for Restaurant Price Calculator. Type 3 for Fruit Price Calculator. Type 4 to calculate a factorial.")
a=int(input(""))
while a<1 or a>4:
    print("Type 1 for Accumulative Calculator. Type 2 for Restaurant Price Calculator. Type 3 for Fruit Price Calculator. Type 4 to calculate a factorial.")
    a=int(input(""))
while (a==1 or a==2 or a==3 or a==4):
        #restaraunt
    if (a == 2):
        print("Restaurant Price Calculator")
        appetizer = float(input("Enter appetizer cost: ")) #appetizer cost
        entree = float(input("Enter entree cost: "))#entree cost
        dessert = float(input("Enter dessert cost: "))#dessert cost
        taxpercent = float(input("Enter tax percantage: ")) #tax percentage
        taxrate = 0.01 * taxpercent
        subtotal = appetizer + entree + dessert #subtotal
        tax=subtotal*(taxrate) #tax
        tip=tax*2+1.00 #tip
        total=subtotal+tip+tax #total
    #Calculator
    
    if (a == 1):
        print ("Accumulative Calculator")
        
        number = float(input("Enter number: "))
        currentnumber = 1
        total = 0
        while (currentnumber <=number):
            total = total + currentnumber
            currentnumber = currentnumber + 1
        #fruits
    if (a == 3):   
        print ("Fruit Price Calculator")
        pounds=-1
        while (pounds <=0):
            pounds = float(input("Enter pounds: "))
            costPound =  float(input("Enter cost per pound in dollars: "))
            costFruit = pounds * costPound
            if pounds <= 100:
                shipping = 7.50
                total = costFruit + shipping
            else:
                    shipping = 6.00
                    total = costFruit + shipping
            if pounds < 1:
                shipping = 0.00
                print ("There has been an error in the number of pounds. Please try again.")
                print("Maybe type a positive intger?")
                total=""
    if a==4:
        #factorial
        numberRightnow=int(input("Enter a number for factorial: "))
        total=1
        for i in range (numberRightnow, 1, -1):
            total=i*total
    if a==1:
        print("Sum of numbers from 1 to number chosen:")
        print(total)
    elif a==4:
        print(str(numberRightnow)+"! is equal to:")
        print(total)
    else:
        print("Total Cost:")
        print("$" + str(total))
    print("To try again, type yes. To quit, type no.")
    b=str(input(""))
    while b != "yes" and b != "no":
        print("To try again, type yes. To quit, type no.")
        b=input("")
    if b== "yes":
        print("Type 1 for Accumulative Calculator. Type 2 for Restaurant Price Calculator. Type 3 for Fruit Price Calculator. Type 4 to calculate a factorial.")
        a=int(input(""))
        while a<1 or a>4:
            print("Type 1 for Accumulative Calculator. Type 2 for Restaurant Price Calculator. Type 3 for Fruit Price Calculator. Type 4 to calculate a factorial.")
            a=int(input(""))
    if b=="no":
        break