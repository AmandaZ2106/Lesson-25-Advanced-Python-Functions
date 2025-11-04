num = int(input("Enter a number: "))
odd_numbers = [i for i in range(1, num + 1) if i % 2 != 0]
print("List of odd numbers:", odd_numbers)

fruits=["apple","banana","strawberry","pear"]
capitalized_fruits=[fruit.capitalize() for fruit in fruits]
print("Capitalized fruits:",capitalized_fruits)