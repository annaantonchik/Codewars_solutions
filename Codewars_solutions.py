'''№34 Building blocks <7 kyu>
The constructor should take an array as an argument, this will contain 3 integers of the form [width, length, height] from which the Block should be created.
Define these methods:
`get_width()` return the width of the `Block`
`get_length()` return the length of the `Block`
`get_height()` return the height of the `Block`
`get_volume()` return the volume of the `Block`
`get_surface_area()` return the surface area of the `Block`
'''
class Block:
    
    def __init__(self, parameters):
        self.width, self.length, self.height = parameters
        self.volume = self.width * self.length * self.height
        self.surface_area = 2 * (self.width * self.length + self.length * self.height + self.width * self. height)
        
    def get_width(self):
        return self.width
    
    def get_length(self):
        return self.length
    
    def get_height(self):
        return self.height
    
    def get_volume(self):
        return self.volume
    
    def get_surface_area(self):
        return self.surface_area


'''№34 Spin Around, Touch the Ground <7 kyu>
Arguments for the constructor
radius -> integer or float (do not round it)
mass -> integer or float (do not round it)
Methods to be defined
get_radius()       =>  radius of the Sphere (do not round it)
get_mass()         =>  mass of the Sphere (do not round it)
get_volume()       =>  volume of the Sphere (rounded to 5 place after the decimal)
get_surface_area() =>  surface area of the Sphere (rounded to 5 place after the decimal)
get_density()      =>  density of the Sphere (rounded to 5 place after the decimal)
'''
class Sphere(object):
    
    from math import pi
    
    pi = pi
      
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
    
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        return round(4 / 3 * self.pi * self.radius ** 3, 5)
    
    def get_surface_area(self):
        return round(4 * self.pi * self.radius ** 2, 5)
    
    def get_density(self):
        return round(self.mass / self.get_volume(), 5)


'''№33 Spin Around, Touch the Ground <7 kyu>
Given a list of directions to spin, "left" or "right", return an integer of how many full 360° rotations were made. Note that each word in the array counts as a 90° rotation in that direction.
'''
def spin_around(lst):
    res = 0
    for item in lst:
        if item == 'right':
            res += 1
        if item == 'left':
            res -= 1
    return abs(res) // 4


'''
№32 Simple string indices <6 kyu>
In this Kata, you will be given a string with brackets and an index of an opening bracket and your task will be to return the index of the matching closing bracket. 
Both the input and returned index are 0-based except in Fortran where it is 1-based. An opening brace will always have a closing brace. '
Return -1 if there is no answer (in Haskell, return Nothing; in Fortran, return 0; in Go, return an error).
Input will consist of letters, numbers and special characters, but no spaces. The only brackets will be ( and ).
'''
def solve(st, idx):
    if st[idx] != '(':
        return -1
    counter = 0
    for i in range(idx, len(st)):
        if st[i] == '(':
            counter += 1
        elif st[i] == ')':
            counter -= 1
        if counter == 0:
            return i


'''
№31 Simple Pig Latin <5 kyu>
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
'''
def pig_it(text):
    text = text.split()
    for i in range(len(text)):
        if text[i].isalpha():
            text[i] = text[i][1:] + text[i][0] + 'ay' 
    return ' '.join(text)


'''
№30 Every possible sum of two digits <7 kyu>
Given a long number, return all the possible sum of two digits of it.
'''
def digits(num):
    res = []
    for i in range(len(str(num))):
        for j in str(num)[i+1:]:
            res.append(int(str(num)[i]) + int(j))
    return res


''' 
№29 Duplicate Arguments <6 kyu>
Complete the solution so that it returns true if it contains any duplicate argument values. 
Any number of arguments may be passed into the function.
The array values passed in will only be strings or numbers. The only valid return values are true and false.
'''
def solution(*args):
    return not (len(list(args)) == len(set(args)))


''' 
№28 Find The Parity Outlier <6 kyu>
You are given an array (which will have a length of at least 3, but could be very large) containing integers. 
The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. 
Write a method that takes the array as an argument and returns this "outlier" N.
'''
#first solution
def find_outlier(integers):
    count_odd = 0
    odd = 0
    count_even = 0
    even = 0
    for i in integers:
        if i % 2 != 0:
            count_odd += 1
            odd = i
        else:
            count_even += 1
            even = i
    if count_odd == 1:
        return odd
    if count_even == 1:
        return even

#another solution
def find_outlier(integers):
    odd = [i for i in integers if i % 2 != 0]
    if len(odd) == 1:
        return odd[0]
    return sum(integers) - sum(odd)


''' 
№27 Number of Divisions <7 kyu>
Calculate how many times a number can be divided by a given number.
Example
For example the number 6 can be divided by 2 two times:
1. 6 / 2 = 3
2. 3 / 2 = 1 remainder = 1
'''
def divisions(n, divisor):
    counter = 0
    while n >= divisor:
        n = n // divisor
        counter += 1
    return counter


''' 
№26 Count the smiley faces! <6 kyu>
Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.
Rules for a smiling face:
- Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
- A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
- Every smiling face must have a smiling mouth that should be marked with either ) or D
No additional characters are allowed except for those mentioned.
'''
def count_smileys(arr):
    counter = 0
    for i in arr:
        if i[0] in ':;' and i[-1] in ')D':
                if len(i) == 2 or (len(i) == 3 and i[1] in '-~' ):
                    counter +=1
    return counter


''' 
№25 Credit card issuer checking <7 kyu>
Given a credit card number we can determine who the issuer/vendor is with a few basic knowns.
Complete the function get_issuer() that will use the values shown below to determine the card issuer for a given card number. 
If the number cannot be matched then the function should return the string Unknown.
'''
def get_issuer(number):
    variants = {'34':['AMEX', 15], '37':['AMEX', 15], '6011':['Discover', 16], '51':['Mastercard', 16], '52':['Mastercard', 16], '53':['Mastercard', 16], '54':['Mastercard', 16], '55':['Mastercard', 16], '4':['VISA', 13, 16]}
    for item in variants.keys():
        if str(number).startswith(item) and len(str(number)) in variants[item]:
            return variants[item][0]
    return 'Unknown'


''' 
№24 Break camelCase <6 kyu>
Complete the solution so that the function will break up camel casing, using a space between words.
'''
def solution(s):
    res = ''
    for i in s:
        if i.upper() == i:
            res = res + ' ' + i
        else:
            res += i
    return res


''' 
№23 Find the missing element between two arrays <7 kyu>
Given two integer arrays where the second array is a shuffled duplicate of the first array with one element missing, find the missing element.
Please note, there may be duplicates in the arrays, so checking if a numerical value exists in one and not the other is not a valid solution.
'''
def find_missing(arr1, arr2):
    for i in arr1:
        if arr1.count(i) > arr2.count(i):
            return i


''' 
№22 Sum a list but ignore any duplicates <7 kyu>
Please write a function that sums a list, but ignores any duplicate items in the list.
For instance, for the list [3, 4, 3, 6] , the function should return 10.
'''
def sum_no_duplicates(l):
    for i in set(l):
        if l.count(i) > 1:
            while l.count(i) != 0: 
                l.pop(l.index(i))
    return sum(l)


''' 
№21 Product of the main diagonal of a square matrix. <7 kyu>
Given a list of rows of a square matrix, find the product of the main diagonal.
'''
def main_diagonal_product(mat):
    res = 1
    for i in range(len(mat)):
        res *= mat[i][i]
    return res


''' 
№20 How many twos? <7 kyu>
Write a function that returns the number of '2's in the factorization of a number
'''
def two_count(n):
    from decimal import Decimal
    counter = 0
    n = Decimal(n)
    while Decimal(n % 2) == 0:
        n = Decimal(n / 2)
        counter += 1
    return counter


''' 
№19 Elapsed Seconds <7 kyu>
Complete the function so that it returns the number of seconds that have elapsed between the start and end times given.
Tips:
The start/end times are given as Date (JS/CoffeeScript), DateTime (C#), Time (Nim), datetime(Python) and Time (Ruby) instances.
The start time will always be before the end time.
'''
def elapsed_seconds(start, end):
    import datetime
    return (end - start).total_seconds()


''' 
№18 From A to Z <7 kyu>
Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter. 
Note that if the range is given in capital letters, return the string in capitals also!
Notes
- A hyphen will separate the two letters in the string.
- You don't need to worry about error handling in this one (i.e. both letters will be the same case and the second letter will always be after the first alphabetically).
'''
def gimme_the_letters(sp):
    res = ''
    for i in range(ord(sp[0]), ord(sp[2])+1):
        res += chr(i)
    return res


''' 
№17 Float Precision <7 kyu>
Update the solution method to round the argument value to the closest precision of two. The argument will always be a float.
'''
def solution(n):
    return round(n, 2)


''' 
№16 Swapping Cards <7 kyu>
Two players draw a pair of numbered cards so that both players can form a 2 digit number. A winner can be decided if one player's number is larger than the other.
However, there is a rule where a player can swap any one of their cards with any one of the other player's cards in a gamble to get a higher number! 
Note that it is illegal to swap the order of your own cards. That means if you draw a 1 then a 9, you cannot swap them to get 91.
Paul's strategy is to always swap his lowest number with the opponent's ten's digit. Return whether this results in Paul winning the round.
- n1 is Paul's number
- n2 is his opponent's number
'''
def swap_cards(n1, n2):
    n1_digits = [n1 // 10, n1 % 10]
    n2_digits = [n2 // 10, n2 % 10]
    n1_digits[n1_digits.index(min(n1_digits))], n2_digits[0] = n2_digits[0], n1_digits[n1_digits.index(min(n1_digits))]
    return int(str(n1_digits[0]) + str(n1_digits[1])) > int(str(n2_digits[0]) + str(n2_digits[1]))


''' 
№15 Stop gninnipS My sdroW! <6 kyu>
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed 
(Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.
'''
def spin_words(sentence):
    words = sentence.split()
    for i in range(len(words)):
        if len(words[i]) >= 5:
            words[i] = words[i][::-1]
    return ' '.join(words)


''' 
№15 String ends with? <7 kyu>
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).
'''
def solution(text, ending):
    return text[-len(ending):] == ending


''' 
№14 Odd or Even? <7 kyu>
Given a list of integers, determine whether the sum of its elements is odd or even.
Give your answer as a string matching "odd" or "even".
If the input array is empty consider it as: [0] (array with a zero).
'''
def odd_or_even(arr):
    total = 0
    for i in arr:
        total +=i
    if total % 2 == 0:
        return 'even'
    return 'odd'


''' 
№13 Is he gonna survive? <8 kyu>
A hero is on his way to the castle to complete his mission. However, he's been told that the castle is surrounded with a couple of powerful dragons! 
Each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry.. 
Assuming he's gonna grab a specific given number of bullets and move forward to fight another specific given number of dragons, will he survive?
Return true if yes, false otherwise :)
'''
def hero(bullets, dragons):
    if bullets == 0:
        return False
    return bullets // dragons == 2


''' 
№12 Calculate average <8 kyu>
Write a function which calculates the average of the numbers in a given list.
Note: Empty arrays should return 0.
'''
def find_average(numbers):
    if len(numbers) == 0:
        return 0
    total = 0
    for i in numbers:
        total += int(i)
    return total / len(numbers)


''' 
№11 Price of Mangoes <8 kyu>
There's a "3 for 2" (or "2+1" if you like) offer on mangoes. For a given quantity and price (per mango), calculate the total cost of the mangoes.
'''
def mango(quantity, price):
    counter = 0
    n = quantity
    while n > 2:
        n -=3
        counter +=2
    res = counter * price + n * price 
    return res


''' 
№10 What is between? <8 kyu>
Complete the function that takes two integers (a, b, where a < b) and return an array of all integers between the input parameters, including them.
'''
def between(a,b):
    return [i for i in range(a, b+1)]


''' 
№9 get character from ASCII Value <8 kyu>
Write a function which takes a number and returns the corresponding ASCII char for that value.
'''
def get_char(c):
  return chr(c)


''' 
№8 Pillars <8 kyu>
There are pillars near the road. The distance between the pillars is the same and the width of the pillars is the same. Your function accepts three arguments:
1. number of pillars (≥ 1);
2. distance between pillars (10 - 30 meters);
3. width of the pillar (10 - 50 centimeters).
Calculate the distance between the first and the last pillar in centimeters (without the width of the first and last pillar).
'''
def pillars(num_pill, dist, width):
    if num_pill == 1:
        return 0
    n1 = width * (num_pill - 2)
    n2 = dist * (num_pill - 1)
    return n1 + n2 * 100


'''
№7 Sum of Multiples <8 kyu>
Your Job: Find the sum of all multiples of n below m
Keep in Mind: n and m are natural numbers (positive integers) m is excluded from the multiples
'''
def sum_mul(n, m):
    total = 0
    if n <= 0 or m <= 0:
        return 'INVALID'
    for i in range(n,m,n):
        total +=i
    return total


'''
№6 Find the position! <8 kyu>
When provided with a letter, return its position in the alphabet.
'''
def position(alphabet):
    n = ord(alphabet.lower()) - 96
    return f'Position of alphabet: {n}'


'''
№5 No zeros for heros <8 kyu>
Numbers ending with zeros are boring.
They might be fun in your world, but not here.
Get rid of them. Only the ending ones.
'''
def no_boring_zeros(n):
    if n != 0:
        while n % 10 == 0:
            n = n // 10
    return n


'''
№4 Quarter of the year <8 kyu> 
Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.
'''
def quarter_of(month):
    return (month + 2) // 3


'''
№3 Who ate the cookie? <8 kyu> 
For this problem you must create a program that says who ate the last cookie. 
If the input is a string then "Zach" ate the cookie. If the input is a float or an int then "Monica" ate the cookie. 
If the input is anything else "the dog" ate the cookie. The way to return the statement is: "Who ate the last cookie? It was (name)!" 
'''
def cookie(x):
    if type(x) == str:
        return 'Who ate the last cookie? It was Zach!'
    elif type(x) == int or type(x) == float:
        return 'Who ate the last cookie? It was Monica!'
    else:
        return 'Who ate the last cookie? It was the dog!'
    

'''№2 Reverse List Order <8 kyu>
In this kata you will create a function that takes in a list and returns a list with the reverse order. 
'''
def reverse_list(l):
    return l[::-1]


'''
№1 Returning Strings <8 kyu> 
Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?". 
'''
def greet(name):
    return f"Hello, {name} how are you doing today?"