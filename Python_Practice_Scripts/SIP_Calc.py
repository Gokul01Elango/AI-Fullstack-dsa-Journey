# for each year you have to add 10 % of the value 
# print each year invesment value

amount=int(input("initial amount : "))
n=int(input("Enter year : "))
for i in range(n+1):
    print(f"{i} Year SIP Amount : {int(amount)}")
    amount=amount+(amount*0.1)
    
