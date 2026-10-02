bill=50
service= input("how was the service?")

if service== "okay":
    print(bill * 1.15)
    print ("the service was okay heres a 15% tip")

elif service == "bad":
    print (bill)
    print ("The service sucked no tip for you!")


elif service == "good":
    print (bill * 1.20)
    print ("The service was very good thank you so much!")

elif service == "amazing":
    print (bill * 1.30)
    print ("the service was amazing! heres a 30% tip")

   