'''№52 Scrabble best word <6 kyu>
You're playing to scrabble. But counting points is hard.
You decide to create a little script to calculate the best possible value.
The function takes two arguments :
1. `points` : an array of integer representing for each letters from A to Z the points that it pays
2. `words` : an array of strings, uppercase
You must return the index of the shortest word which realize the highest score.
If the length and the score are the same for two elements, return the index of the first one.
'''
def get_best_word(points, words):
    max_score = 0
    best_word_index = 0
    
    for i, word in enumerate(words):
        total_score = sum(points[ord(letter) - ord("A")] for letter in word)
        if total_score > max_score or (total_score == max_score and len(word) < len(words[best_word_index])):
            max_score = total_score
            best_word_index = i
    
    return best_word_index

'''№51 Remember <6 kyu>
Write a function that takes a string and returns an array of the repeated characters (letters, numbers, whitespace) in the string.
If a charater is repeated more than once, only show it once in the result array.
Characters should be shown by the order of their first repetition. Note that this may be different from the order of first appearance of the character.
Characters are case sensitive.
'''
def remember(str_: str):
    seen = set()
    res = []
    for simbol in str_:
        if str_.count(simbol) > 1 and simbol in seen and simbol not in res:
            res.append(simbol)
        if str_.count(simbol) > 1 and simbol not in seen:
            seen.add(simbol)
    return res

'''№50 Decipher this! <6 kyu>
You are given a secret message you need to decipher. Here are the things you need to know to decipher it:

For each word:
the second and the last letter is switched (e.g. Hello becomes Holle)
the first letter is replaced by its character code (e.g. H becomes 72)
there are no special characters used, only letters and spaces
words are separated by a single space
there are no leading or trailing spaces
'''
def decipher_this(s: str):
    s = s.split()
    res = []
    for word in s:
        print(len(word))
        new_word = ''
        if len(word) == 2 or (len(word) == 3 and word[2].isdigit()):
            new_word = chr(int(word))
        elif len(word) == 3:
            new_word = chr(int(word[0:2])) + word[2]
        elif len(word) == 4 and word[2].isdigit():
            new_word = chr(int(word[0:3])) + word[3]
        elif len(word) == 4:
            new_word = chr(int(word[0:2])) + word[-1] + word[2]
        elif len(word) > 4 and word[2].isalpha():
            new_word = chr(int(word[0:2])) + word[-1] + word[3:-1] + word[2]
        else:
            new_word = chr(int(word[0:3])) + word[-1] + word[4:-1] + word[3]
        res.append(new_word)
    return " ".join(res)

'''№49 Are all elements equal? (Infinity version) <6 kyu>
Create a function eq_all that determines if all elements of any iterable are equal; the iterable may be infinite. Return value is a bool.
Notes.
For the function result to be True, the iterable must be finite; False, however, can result from an element finitely far from the left end. 
There will be no tests with infinite series of equal elements.
Elements will be primitive values.
'''
def eq_all(iterable):
    for check in iterable:
        for item in iterable:
            if item != check:
                return False
    return True

'''№48 Square Matrix Multiplication <6 kyu>
Create a function that returns the lowest product of 4 consecutive digits in a number given as a string.
This should only work if the number has 4 digits or more. If not, return "Number is too small".
lowest_product("123456789") --> 24 (1x2x3x4)
lowest_product("35") --> "Number is too small"
'''
def lowest_product(num: str):
    if len(num) < 4:
        return "Number is too small"
    nums = [int(i) for i in num]
    res = []
    for i in range(len(num) - 3):
        product = 1
        for j in range(4):
            product *= nums[i + j]
        res.append(product)
    return min(res)

'''№47 Square Matrix Multiplication <7 kyu>
Write a function that given, an array arr, returns an array containing at each index i the amount of numbers that are smaller than arr[i] to the right.
For example:
* Input [5, 4, 3, 2, 1] => Output [4, 3, 2, 1, 0]
* Input [1, 2, 0] => Output [1, 1, 0]
'''
def smaller(arr: list):
    res = [sum([arr[i] > arr[j] for j in range(i, len(arr))]) for i in range(len(arr))]
    return res

'''№46 Square Matrix Multiplication <5 kyu>
Write a function that accepts two square (NxN) matrices (two dimensional arrays), and returns the product of the two. Only square matrices will be given.
How to multiply two square matrices:
We are given two matrices, A and B, of size 2x2 (note: tests are not limited to 2x2). 
Matrix C, the solution, will be equal to the product of A and B. To fill in cell [0][0] of matrix C, you need to compute: A[0][0] * B[0][0] + A[0][1] * B[1][0].
More general: To fill in cell [n][m] of matrix C, you need to first multiply the elements in the nth row of matrix A by the elements in the mth column of matrix B, then take the sum of all those products. 
This will give you the value for cell [m][n] in matrix C.
'''
def matrix_mult(a: list, b: list):
    res = [[0] * len(a[0]) for _ in range(len(a))]
    for i in range(len(b)):
        for j in range(len(a)):
            for k in range(len(a[0])):
                res[i][j] += a[i][k] * b[k][j]
    return res

'''№45 Who likes it? <6 kyu>
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.
Implement the function which takes an array containing the names of people that like an item. 
Note: For 4 or more names, the number in "and 2 others" simply increases.
'''
def likes(names: list):
    if len(names) == 0:
        return('no one likes this')
    elif len(names) == 1:
        return(f'{names[0]} likes this')
    elif len(names) == 2:
        return(f'{names[0]} and {names[1]} like this')
    elif len(names) == 3:
        return(f'{names[0]}, {names[1]} and {names[2]} like this')
    else: 
        return(f'{names[0]}, {names[1]} and {len(names) - 2} others like this')

'''№44 Good vs Evil <6 kyu>
Middle Earth is about to go to war. The forces of good will have many battles with the forces of evil. 
Different races will certainly be involved. Each race has a certain worth when battling against others. 
On the side of good we have the following races, with their associated worth: Hobbits = 1, Men = 2, Elves = 3, Dwarves = 3, Eagles = 4, Wizards = 10
On the side of evil we have: Orcs = 1, Men = 2, Wargs = 2, Goblins = 2, Uruk Hai = 3, Trolls = 5, Wizards = 10
Although weather, location, supplies and valor play a part in any battle, if you add up the worth of the side of good and compare it with the worth of the side of evil, the side with the larger worth will tend to win.
Thus, given the count of each of the races on the side of good, followed by the count of each of the races on the side of evil, determine which side wins.

Input:
The function will be given two parameters. Each parameter will be a string of multiple integers separated by a single space. Each string will contain the count of each race on the side of good and evil.
The first parameter will contain the count of each race on the side of good in the following order:
Hobbits, Men, Elves, Dwarves, Eagles, Wizards.
The second parameter will contain the count of each race on the side of evil in the following order:
Orcs, Men, Wargs, Goblins, Uruk Hai, Trolls, Wizards.
All values are non-negative integers. The resulting sum of the worth for each side will not exceed the limit of a 32-bit integer.

Output:
Return "Battle Result: Good triumphs over Evil" if good wins, "Battle Result: Evil eradicates all trace of Good" if evil wins, or "Battle Result: No victor on this battle field" if it ends in a tie.
'''
def good_vs_evil(good: str, evil: str):
    good = [int(i) for i in good.split()]
    evil = [int(i) for i in evil.split()]
    good_forse = [1, 2, 3, 3, 4, 10]
    evil_forse = [1, 2, 2, 2, 3, 5, 10]
    res_good = sum([good[i] * good_forse[i] for i in range(len(good))])
    res_evil = sum([evil[i] * evil_forse[i] for i in range(len(evil))])
    if res_good > res_evil:
        return 'Battle Result: Good triumphs over Evil'
    elif res_good < res_evil:
        return 'Battle Result: Evil eradicates all trace of Good' 
    return 'Battle Result: No victor on this battle field'

'''№43 Password generator <6 kyu>
You need to write a password generator that meets the following criteria:
6 - 20 characters long
contains at least one lowercase letter
contains at least one uppercase letter
contains at least one number
contains only alphanumeric characters (no special characters)
Return the random password as a string.
Note: "randomness" is checked by counting the characters used in the generated passwords - all characters should have less than 50% occurance. Based on extensive tests, the normal rate is around 35%.
'''
def password_gen():
    import random as r
    numbers = '1234567890'
    letters = ''.join([chr(i) for i in range(65, 91)])
    res = numbers[r.randint(0,9)] + letters[r.randint(0, len(letters) - 1)] + letters.lower()[r.randint(0, len(letters) - 1)] 
    n = r.randint(3, 17)
    for i in range(n):
        char = [numbers[r.randint(0,9)], letters[r.randint(0, len(letters) - 1)], letters.lower()[r.randint(0, len(letters) - 1)]][r.randint(0,2)]
        res += char
    return res

'''№42 Sum of integers in string. <7 kyu>
Your task in this kata is to implement a function that calculates the sum of the integers inside a string. 
For example, in the string "The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog", the sum of the integers is 3635.
Note: only positive integers will be tested.
'''
def sum_of_integers_in_string(s):
    lst = []
    num = ''
    for i in range(len(s)):
        if s[i].isdigit():
            num += s[i]
        else:
            if num !='':
                lst.append(int(num))
                num = ''
        if num != '' and i + 1 == len(s):
            lst.append(int(num))
    return sum(lst)

'''№41 String to list of integers. <7 kyu>
Given a string containing a list of integers separated by commas, write the function string_to_int_list(s) that takes said string and returns a new list containing all integers present in the string, preserving the order.
For example, give the string "-1,2,3,4,5", the function string_to_int_list() should return [-1,2,3,4,5]
Please note that there can be one or more consecutive commas whithout numbers, like so: "-1,-2,,,,,,3,4,5,,6"
'''
def string_to_int_list(s):
    return [int(i) for i in s.split(',') if i != '']

'''№40 Integer depth <7 kyu>
Write a function that can return the smallest value of an array or the index of that value. The function's 2nd parameter will tell whether it should return the value or the index.
Assume the first parameter will always be an array filled with at least 1 number and no duplicates. Assume the second parameter will be a string holding one of two values: 'value' and 'index'.
'''
def find_smallest(numbers, to_return):
    return numbers.index(min(numbers)) if to_return == 'index' else min(numbers)

'''№39 Integer depth <6 kyu>
The depth of an integer n is defined to be how many multiples of n it is necessary to compute before all 10 digits have appeared at least once in some multiple.
'''
def compute_depth(n):
    mask = [i for i in range(10)]
    res = 0
    digits = set()
    while len(digits) != len(mask):
        res += 1 
        product = n * res
        for i in str(product):
            digits.add(int(i))
    return res

'''№38 Small enough? - Beginner <7 kyu>
You will be given an array and a limit value. You must check that all values in the array are below or equal to the limit value. 
If they are, return true. Else, return false.
You can assume all values in the array are numbers.
'''
def small_enough(array, limit):
    res = True
    for i in array:
        if i > limit:
            res = False
            break
    return res

'''№37 Disemvowel Trolls <7 kyu>
Trolls are attacking your comment section!
A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.
Your task is to write a function that takes a string and return a new string with all vowels removed.
For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
Note: for this kata y isn't considered a vowel.
'''
def disemvowel(string_):
    letters = 'aeuio'
    res = ''
    for i in string_:
        if i.lower() not in letters:
            res += i
    return res

'''№36 Sum of array singles <7 kyu>
In this Kata, you will be given an array of numbers in which two numbers occur once and the rest occur only twice. 
Your task will be to return the sum of the numbers that occur only once.
For example, repeats([4,5,7,5,4,8]) = 15 because only the numbers 7 and 8 occur once, and their sum is 15. Every other number occurs twice.'''
def repeats(arr):
    arr_set = set(arr)
    res = sum([i for i in arr_set if arr.count(i) == 1])
    return res

'''№35 RGB To Hex Conversion <5 kyu>
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. 
Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.
Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
'''
def rgb(r, g, b):
    if r < 0:
        r = 0
    elif r > 255:
        r = 255
    if g < 0:
        g = 0
    elif g > 255:
        g = 255
    if b < 0:
        b = 0
    elif b > 255:
        b = 255
    return str(hex(r)).upper()[2:].zfill(2) + str(hex(g)).upper()[2:].zfill(2) + str(hex(b)).upper()[2:].zfill(2)


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