shopping_list = []
while True:
    item = input("Add a item: ")
    if item == "":
        break
    else:
        shopping_list.append(item)

print (shopping_list)