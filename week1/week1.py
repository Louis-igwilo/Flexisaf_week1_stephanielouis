
total_price = 0
items = []
while True:
    item = input("Enter the name of item or type 'done' to finish: ")
    if item == "done":
        break
    price = float(input("Enter the price of {}: ".format(item)))
    quantity = int(input("Enter the quantity of {}: ".format(item)))
    total_cost = price * quantity
    total_price += total_cost
    items.append((item, total_cost))

print("\nItems:")

for item, total_cost in items:
    print("{}: ${:.2f}".format(item, total_cost))

print("\nTotal price for all items: ${:.2f}".format(total_price))