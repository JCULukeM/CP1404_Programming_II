

do_it = True
numbers = [3, 1, 4, 1, 5, 9, 2]
print(numbers[0],numbers[-1],numbers[3],numbers[:-1],numbers[3:4],
      5 in numbers,7 in numbers,"3" in numbers,numbers + [6, 5, 3], end = "" )
if do_it:
    numbers.pop(0)
    numbers.insert(0,10)
    numbers.pop(-1)
    numbers.append(1)
    print(numbers[2:])
    print(9 in numbers)
print(numbers)





