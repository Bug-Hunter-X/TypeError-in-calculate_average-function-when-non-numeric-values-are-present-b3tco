def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    return sum(numeric_numbers) / len(numeric_numbers)

#Example usage
my_numbers = [10,20,30,40,50]
print(calculate_average(my_numbers)) #Output 30.0

my_numbers = []
print(calculate_average(my_numbers)) #Output 0

my_numbers = [10,20, 'a', 40,50]
print(calculate_average(my_numbers)) #Output 30.0