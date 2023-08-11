# Advanced topics in Python

""" 
* Regular expressions
* Generators and iterators
* Decorators
* Context managers
* Multithreading and multiprocessing

"""
# Regular expressions
""" __summary__ 
\d: Matches any digit (0-9)
\w: Matches any alphanumeric character (a-z, A-Z, 0-9, and underscore)
\s: Matches any whitespace character (space, tab, newline)
.: Matches any character except a newline
*: Matches zero or more occurences of the preceding character or group.
+: Matches one or more occurences of the preceding character or group
?: Matches zero or one occurence of the preceding character or group.
[ ]: Matches any character within the square brackets
[^ ]: Matches any character not within the square brackets
^: Matches the start of a line
$: Matches the end of a line

"""

# Matching; regex re.match()
# Searching; regex re.search()
# Find matching: re.findall()

# Example: Demonstrating regex | match first word, Match group words, Match all numbers
import re
text = "Hello, my name is Joe. I am a student with one year experience"

# Match First word
match = re.search(r"\b\w+\b", text)

if match:
    print("Matches:", match.group())
    
matches = re.findall(r"\d+", text)
print("Matches:", matches)

# Example 2; VAlidate the email format or email address
def validate_email(email):
    patern = r"^[\w\.\-]+@[\w\.\-]+\.\w+$"
    if re.match(patern, email):
        return True
    else:
        return False
    
# Example usage
email1 = "joe@example.com"
email2 = "joe@examplecom"
print(validate_email(email1))
print(validate_email(email2))

# Generators and iterators
# Use the keyword 'yield'
# Iterator '__iter__' '__next__' iterator

def factrial(n):
    # return the factorial of a number
    if n ==0:
        yield 1
    else:
        yield n * factrial(n-1)
        fact = 1
    for i in range(1, n-1):
        fact *= i

# Print the factorial of a number from 1-10
for i in range(1, 10):
    print(factrial(i))
    
def factorial(n):
    if n ==0 or n ==1:
        return 1
    else:
        return n * factorial(n-1)

# # Print the factorial of a number using a geneartor
# def factorial_generator(n,m):
#     for i in range(n, m):
#         yield factorial(i)
    
# for factorial_value in factorial_generator(1,10):
#     print(factorial_value)
    
# Example 3;
