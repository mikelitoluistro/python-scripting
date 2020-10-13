money = int(input("How much you money:"))
price = int(input("Price:"))
count = int(input("How many:"))
total = price * count
change = money - total

if total <= money:
  print("Your change is " + str(change))
else:
    print("Your money is not enough")