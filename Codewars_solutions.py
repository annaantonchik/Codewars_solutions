''' 
№25 Credit card issuer checking <5 kyu>
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