# 1. Write a Python program with builtin function to multiply all the numbers in a list
def multiply_list(l):
    # Используем функцию reduce() для последовательного умножения всех элементов списка
    from functools import reduce
    result = reduce(lambda x, y: x * y, l)
    print(result)

# 2. Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
def group_letters(s):
    # Используем функцию sum() для подсчета количества заглавных и строчных букв в строке
    upper_count = sum(1 for x in s if x.isupper())
    lower_count = sum(1 for x in s if x.islower())
    print(upper_count)
    print(lower_count)

# 3. Write a Python program with builtin function that checks whether a passed string is palindrome or not.
def is_palindrome(s):
  print("".join(reversed(list(s))) == s)


# 4. Write a Python program that invoke square root function after specific milliseconds.
# Sample Input:
# 25100
# 2123
# Sample Output:
# Square root of 25100 after 2123 miliseconds is 158.42979517754858
import time

def square_root_with_delay():
  n = int(input())
  d = int(input())
  time.sleep(d / 1000) 
  print(f"Square root of {n} after {d} miliseconds is {n ** (1 / 2)}")

# 5. Write a Python program with builtin function that returns True if all elements of the tuple are true.
def all_true(t):
  return eval(" and ".join(map(lambda x : str(x), t)))