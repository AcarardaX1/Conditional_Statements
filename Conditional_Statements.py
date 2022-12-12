is_hot = False #Specify if it's a hot day or not

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif not is_hot:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("Do whatever you want")
    
print("Enjoy your day")


print("----------------------------------------------------------------")
 
price = 1000000
good_score4credit = True #Specify if the credit score is good or not

if good_score4credit:
    down_payment = 0.1 * price
else:
    down_payment= 0.2 * price
print(f"Down payment: ${down_payment}")