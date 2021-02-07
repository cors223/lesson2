number = int(input(f"Insert the number: "))
list = [2, 8, 6, 1, 9]
i = list.count(number)
for element in list:
    if i > 0:
        n = list.index(number)
        list.insert(n+i, number)
        break
    else:
        if number > element:
            j = list.index(element)
            list.insert(j, number)
            break
        elif number < list[len(list) - 1]:
            list.append(number)
print(list)