even_total = 0
odd_total = 0

starting_integer = int(input("Enter starting integer: "))
ending_integer = int(input("Enter ending integer: "))

for num in range(starting_integer, ending_integer + 1):
    if num % 2 == 0:
        even_total += num
    else:
        odd_total += num

print(f"The total of even integers from {starting_integer} to {ending_integer} is {even_total}")
print(f"The total of odd integers from {starting_integer} to {ending_integer} is {odd_total}")