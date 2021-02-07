number = int(input("Enter month number: "))
if number <= 12 and number >= 1:
    month = {1: 'January',
                  2: 'February',
                  3: 'March',
                  4: 'April',
                  5: 'May',
                  6: 'June',
                  7: 'Jule',
                  8: 'August',
                  9: 'September',
                  10: 'October',
                  11: 'November',
                  12: 'December'}
    list = list(month.values())
    for i, el in enumerate(list):
        if i == number-1:
            print(f"Month from list is {list[i]}")
            break
    print(f"Month from {month[number]}")
else:
    print(f"You entered the wrong number")