def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

#Example usage
my_numbers = [10,20,30,40,50]
print(calculate_average(my_numbers)) #Output 30.0

my_numbers = []
print(calculate_average(my_numbers)) #Output 0

my_numbers = [10,20, 'a', 40,50]
print(calculate_average(my_numbers)) #TypeError: unsupported operand type(s) for +: 'int' and 'str'