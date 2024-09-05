# Overview
This Python script contains several functions and a class that demonstrate basic programming concepts:

#add_numbers(num1, num2): Adds two numbers and returns the result.

is_even(number): Checks if a number is even and returns True or False.

reverse_string(text): Reverses the given string and returns it.

count_vowels(text): Counts the number of vowels in a given string.

calculate_factorial(n): Computes the factorial of a non-negative integer n.

sort_by_age(people): Sorts a list of tuples (name, age) by age in ascending order.

merge_dicts(dict1, dict2): Merges two dictionaries, summing values for common keys.

Car class: Defines a Car class with attributes for make, model, and year, and a method to display car information.

# Functions
## add_numbers(num1, num2)
```
Adds two numbers.

Example Usage:

python:

print(add_numbers(2, 7))  # Output: 9
```

## is_even(number)
```
Determines if the given number is even.

Example Usage:

python

print(is_even(2))  # Output: True
reverse_string(text)
```
## Reverses the provided string.
```

Example Usage:

python code:

print(reverse_string("hydee"))  # Output: "eedyh"

```
## count_vowels(text)
```
Counts the number of vowels in the given string.


Example Usage:

python code:

print(count_vowels("hello"))  # Output: 2
```
## calculate_factorial(n)
```
Calculates the factorial of a non-negative integer.

Example Usage:

python code:

print(calculate_factorial(5))  # Output: 120
```

### sort_by_age(people)
```
Sorts a list of tuples (name, age) by age.

Example Usage:

python code:

people = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
print(sort_by_age(people))  # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
```


## merge_dicts(dict1, dict2)
```

Merges two dictionaries, summing values for common keys.

Example Usage:

python code:

print(merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}))  # Output: {'a': 1, 'b': 5, 'c': 4}
```

## Class : car

A class representing a car with make, model, and year attributes.

Methods:
__init__(self, make, model, year): Initializes the car with make, model, and year.
display_info(self): Prints the car's information.
Example Usage:

python code:

my_car = Car("Porsche", "Gt3rs", 2011)
my_car.display_info()  # Output: Your car's information is: Make- Porsche, Model- Gt3rs, Year- 2011
