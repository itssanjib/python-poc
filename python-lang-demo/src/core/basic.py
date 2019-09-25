
"""This is a sample file to test the basic python syntax.

s - strings
d - decimal integers (base-10)
f - floating point display
c - character
b - binary
o - octal
x - hexadecimal with lowercase letters after 9
X - hexadecimal with uppercase letters after 9
e - exponent notation

<   :  left-align text in the field
^   :  center text in the field
>   :  right-align text in the field  

End of the multiple line comments.
"""

from core import i, name, map_test, array_test, list_test, log_string, log_multiple_string,\
    fibo
from builtins import str, set
from _ast import Str
import math
import json
import os

print("Hello world")

print(str(i)+name)
print(map_test.get('key1'))
print(array_test[0])
print(list_test[0])

# Printing the list [1,2,3,4,5]
print(list_test)

# Slicing the list [1,2,3,4,5]
print(list_test[3:])

# Printing a
a, b = 10, 19
print(a, b)

# String concatenation
str1, str2 = 'Hi ', 'Sanjib!'
print(str1 + str2)

# If Else condition example
flag = False
if flag:
    print("True")
elif a > b:
    print("a > b")
else:
    print("False")
    
# For statement example
for j in range(10):
    print('j: ' +  str(j))
    
for val in array_test[:]:
    print("val:" + val)

# While loop example
num = 1
while num < 10:
    print(num)
    num = num + 1
    
# range function example
print("Range example:")
for r in range(2, 10, 5):
    print(r)
print(list(range(3)))

# Pass example
#while True:
#    pass

# Calling a method defined core
log_string("Bad Gateway!")
log_string()

# Calling a method with arbitrary argument
days = ["Four", "Five", "Six", "Seven"]
log_multiple_string("One")
log_multiple_string("Two", "Three")
log_multiple_string(*days)

# Lambda expression example
concatString = lambda a, b: a + " " + b
print("Lambda expression example")
double = lambda x : x * 2
print(double(5))
print(concatString("Hello", "World"))

# Printing the documentation
print(__doc__)

# Printing function annotations
def func_annotatin_example(a:'String', b:'String'="0") -> 'String':
    return a + b
#print(log_string.__annotations__)
print(func_annotatin_example.__annotations__)
print(func_annotatin_example("2", "3"))
print(func_annotatin_example("2"))

# Working on list
print("Basic list is")
print(list_test)
list_test.append((6,7))
print(list_test[2])
print(list_test[5])
list_test.pop(1)
print(list_test)
list_test.extend(array_test)
print(list_test)
list_test.insert(1, 2)
print(list_test)
list_test.remove((6,7))
print(list_test)
print("index of 5: " + str(list_test.index(5)))
print("index of 5: " + str(list_test.index(5, 0, 5)))
print("size of list is: " + str(list_test.__len__()))
print("Number of appear of a in the list is: " + str(list_test.count('a')))
list_test.clear()
print(list_test)

# List comprehension examle
print("Test list comprehension")
# list_comp = list(z for z in range(10, 100, 20) if z > 50)
# list_comp = [[i,j] for i in range(10, 100, 20) for j in range(10, 100, 20) if i > 50 and j < 90]
list_comp = [[i,j] for i in range(10, 100, 20) for j in range(10, 100, 20) if i == j]
# for z in range(10, 100, 20):
#     list_comp.append(z)
print(list_comp)


# Touple example immutable list
tpl = (1, 2, 19, 'sanjib', 'subhaj', [9, 4, 3, 2])
empty_tpl = ()
print(tpl)
print(empty_tpl)


# Set example
print("Set example")
#unique_letter = set('ajfskfjdfjsjfluerier')
unique_letter = {'ab', 'bc', 'cd', 'ab'}
print(unique_letter)

# Dictionary example
print(map_test)
print("Printing the keys of the dict.")
print(list(map_test))
print(map_test.get(11, 'Not Found!'))
for k, v in map_test.items():
    print(k, v)
for i, v in enumerate(map_test):
    print(i, v)
    
# Splitting string example
months = "January, February, March, April"
print(months)
print(months.split(','))
for month in months.split(','):
    print(month.strip().strip('M'))
    
# dir() Function example
print("Printing dir() of fibo:")
print(dir(fibo))
print(fibo.__name__)
print(fibo.__file__)


# Input Output example
name = "Sanjib Pal"
print(f'My name is {name}')
print(f'''My name is {name}''')

# str.format() example
print('My name is {0} {2} {1}'.format("Sanjib", "Pal", "Kumar"))
print('My name is {0} {2} {1}. I am a {occupation}.'.format("Sanjib", "Pal", "Kumar", occupation = "service man"))
print('Employee {2:3d} name is {0} {1}'.format("Sanjib", "Pal", 1))
print('Employee {2:3d} name is {0} {1}'.format("Sanjib", "Pal", 10))
print('Employee {2:>3} name is {0} {1}'.format("Sanjib", "Pal", "1"))
print('Employee {2:>3} name is {0} {1}'.format("Sanjib", "Pal", "10"))
print("{:*^20s}".format("Geeks"))
print('Employee {2:*^3} name is {0} {1}'.format("Sanjib", "Pal", "1"))
print('Employee {2:*>3} name is {0} {1}'.format("Sanjib", "Pal", "10"))
print('{:f}'.format(109.42345))
print('{:3.3%}'.format(109.42345))
print('The value of pi is approximately %5.3f.' % math.pi)


# Creating new file and save into directory.
f = open("D:/python_projects/dump_files/my_py_file.txt", 'w')
f.write("Hi, this is the first content in this file.")

# Reading file content from the existing directory.
f = open("D:/python_projects/dump_files/my_py_file_1.txt", 'r')
file_data = f.read()
print(file_data)

f = open("D:/python_projects/dump_files/my_py_file_2.txt", 'r')
for line in f:
    print("#" + line)
    
# JSON example
jf = open("D:/python_projects/dump_files/my_jsonfile.json", 'w')
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
json_str = json.dumps(x)
print(json_str)
#Writing json string to a file.
json_str = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(json_str)
json.dump(y, jf)
jf.close()

f = open("D:/python_projects/dump_files/my_jsonfile.json", 'r')
jf_data = f.read()
y = json.loads(jf_data)
print("age:" + str(y["age"]))


# Standard Library code testing
help(os)