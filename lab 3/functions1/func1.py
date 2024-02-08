#1
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

#2
def fahrenheit_to_centigrade(Fahrenheit):
    centigrade = (5/9)*(Fahrenheit-32)
    return centigrade

#3
def solve(numheads, numlegs):
    rabbits = (numlegs - 2 * numheads) / 2
    chickens = numheads - rabbits
    return rabbits, chickens

#4
def isPrime(num):
    if num<2:
        return False
    for i in range(2, num):
        if(num % i == 0):
            return False
    return True        

def filter_prime(*args):
    prime_list = []
    for i in args:
        if(isPrime(i)):
            prime_list.append(i)
    return prime_list

#5
from itertools import permutations

def print_permutations():
    user_input = input("Enter a string: ")
    
    for perm in permutations(user_input):
        print(''.join(perm))
        
print_permutations()

#6
def reverse_word():
    return input("Enter a sentence: ")[::-1]

result = reverse_word()
print(result)

#7
def has_33(nums):
    has = False
    for i in range(len(nums)-1):
        if(nums[i]==3 and nums[i+1]==3):
            has = True
    return has

print(has_33([1, 3, 3])) 
print(has_33([1, 3, 1, 3])) 
print(has_33([3, 1, 3])) 

#8
def spy_game(nums):
    required_nums = [0, 0, 7]
    
    for i in nums:
        if i == required_nums[0]:
          required_nums.pop(0)         
    
        if not required_nums:
            return True
    return False

print(spy_game([1,2,4,0,0,7,5]))  
print(spy_game([1,0,2,4,0,5,7]))  
print(spy_game([1,7,2,0,4,5,0]))  

#9
def volume(radius):
    volume = (4 * 3.14 * radius **3)/3
    
    print (volume)
    
#10
def uniques(list):
    return list(dict.fromkeys(list))

#11
def palindrome(word):
    reverse_word = palindrome[::-1]
    if (reverse_word == word):
        return True
    return False
    # return word == word[::-1]

#12
def histogram(list):
    for i in list:
        print ('*' * i)
        
#13 
def guess_the_number(n):
    count = 0
    print ("Hello! What is your name?")
    username = input()
    
    print(f'Well, {username}, I am thinking of a number between 1 and 20.')
    
    while True:
        print('Take a guess')
        user_input = int(input())
        count += 1

        if user_input < n:
            print('Your guess is too low.')
        elif user_input > n:
            print('Your guess is too high')
        else:
            print(f'Good job, {username}! You guessed my number in {count} guesses!')
            break

guess_the_number(5)

#14
import random
def guess_the_number():
    count = 0
    bobik = random.randint(1, 20)
    print ("Hello! What is your name?")
    username = input()
    
    print(f'Well, {username}, I am thinking of a number between 1 and 20.')
    
    while True:
        print('Take a guess')
        user_input = int(input())
        count += 1

        if user_input < bobik:
            print('Your guess is too low.')
        elif user_input > bobik:
            print('Your guess is too high')
        else:
            print(f'Good job, {username}! You guessed my number in {count} guesses!')
            break

guess_the_number()
        
    
    