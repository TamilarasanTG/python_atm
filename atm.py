motea=0
b=10000
while a<2:
    card =input("ATM card")
    print("Wlecome to ATM\n")
    pin = int(input("Enter a pin :"))
    pinnum =4567
    if(pin==pinnum):
     print("Savings /Current")
     #amt = [100,500,1000]
     getamt = int(input("Enter amount"))
     if getamt<b:
         print("Rs",getamt,"withdraw successfully")
         b=b-getamt
         print(b, "balance")
         break


    else:
      print("pin not validate")
      break
