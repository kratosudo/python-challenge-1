#solution 1
def add_numbers(num1, num2):
    return num1 + num2
print(add_numbers(2, 7))

#solution 2


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
print(is_even(2))

#solution 3

def reverse_string(text):
    return text[::-1]

print(reverse_string("hydee"))

#solution 4

def count_vowels(text):
    vowels="aeiou"
    text=text.lower()
    return sum(1 for letter in text if letter in vowels)
print(count_vowels("hello"))

#solution 5
def calculate_factorial(n):
    if n == 0:
        return 1
    factorial=1
    for i in range(1, n+1):
        factorial *= i
    return factorial

print(calculate_factorial(5))

#solution 6

def apply_decorator(func):
    
    def decorator_func(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return decorator_func

@apply_decorator
def sample_function():
    return "Function executed"

print(sample_function()) 

#solution 7

def sort_by_age(people):
    return sorted(people, key=lambda x: x[1])
people = [
    ("Alice", 25),
    ("Bob", 30),
    ("Charlie", 35),    
]
sorted_people = sort_by_age(people)
print(sorted_people)

#solution 8

def merge_dicts(dict1, dict2):
    merged = dict2.copy()
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged
print(merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}))

#solution 9 .

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def display_info(self):
        print(f"Your car's information is: Make- {self.make}, Model- {self.model}, Year- {self.year}")

# Creating an instance of Car
my_car = Car("Porsche", "Gt3rs", 2011)
my_car.display_info()

       
    