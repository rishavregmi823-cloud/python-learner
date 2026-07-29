#shoppingcartprgm
foods= []
prices= []
total=0
while True:
    food=input("Enter a food to buy (q to quit) :")
    if food.lower() =="q" :
     break

    price= float(input(f"Enter the price of {food} :$"))
    foods.append(food)
    prices.append(price)

    total+=price
print(f"Your total bill is : ${total}\n ")
print("Thank you visit again!!")