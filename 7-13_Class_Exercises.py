#VERSION 1: import(modulename)
import math #built-in python module that gives users access to various mathematical operations and functions
import random #built-in python module with various functions to generate random numbers and perform many probability options
 
result_1 = math.pow(2, 4) #access the pow(x,y) function in the math module, computes x exponent y
print("result_1 is", result_1)

result_2 = math.sqrt(16) #access the sqrt(x) function in the math module, computes square root of x
print("result 2 is", result_2)

result_3 = random.randint(0,100) #access the randint(x,y) function in the random module, returns a random integer between x and y
print("result_3 is", result_3)

names = ["Amaryllis", "Godson", "Emily", "Reina", "Derin", "Elena", "Inacio"]
print("Original names: ", names)
# 
random.shuffle(names) #access the shuffle(x) function in the random module, shuffles the elements in the collection of elements X
print("Names after shuffling: ", names)

result_4 = random.choice(names) #access the choice(x) funcition in the random module, makes a random choice from the elements in the collection X
print("Chosen name is: ", result_4)

#VERSION 2: from (modulename) import (functionname)
from math import pow
from math import sqrt
from random import randint
from random import shuffle
from random import choice
result_1 = pow(2, 4) #access the pow(x,y) function in the math module, computes x exponent y
print("result_1 is", result_1)

result_2 = sqrt(16) #access the sqrt(x) function in the math module, computes square root of x
print("result 2 is", result_2)

result_3 = randint(0,100) #access the randint(x,y) function in the random module, returns a random integer between x and y
print("result_3 is", result_3)

names = ["Amaryllis", "Godson", "Emily", "Reina", "Derin", "Elena", "Inacio"]
print("Original names: ", names)

shuffle(names) #access the shuffle(x) function in the random module, shuffles the elements in the collection of elements X
print("Names after shuffling: ", names)

result_4 = choice(names) #access the choice(x) funcition in the random module, makes a random choice from the elements in the collection X
print("Chosen name is: ", result_4)


#VERSION 3: from (modulename) import (functionname) as (alternativename)
from math import pow as p    
from math import sqrt as s
from random import randint as r
from random import shuffle as sh 
from random import choice as c 
result_1 = p(2, 4) #access the pow(x,y) function in the math module, computes x exponent y
print("result_1 is", result_1)

result_2 = s(16) #access the sqrt(x) function in the math module, computes square root of x
print("result 2 is", result_2)

result_3 = r(0,100) #access the randint(x,y) function in the random module, returns a random integer between x and y
print("result_3 is", result_3)

names = ["Amaryllis", "Godson", "Emily", "Reina", "Derin", "Elena", "Inacio"]
print("Original names: ", names)

sh(names) #access the shuffle(x) function in the random module, shuffles the elements in the collection of elements X
print("Names after shuffling: ", names)

result_4 = c(names) #access the choice(x) funcition in the random module, makes a random choice from the elements in the collection X
print("Chosen name is: ", result_4)
 
#Version 4: import (modulename) as (alternativename)
import math as m #built-in python module that gives users access to various mathematical operations and functions
import random as r #built-in python module with various functions to generate random numbers and perform many probability options
 
result_1 = m.pow(2, 4) #access the pow(x,y) function in the math module, computes x exponent y
print("result_1 is", result_1)

result_2 = m.sqrt(16) #access the sqrt(x) function in the math module, computes square root of x
print("result 2 is", result_2)

result_3 = r.randint(0,100) #access the randint(x,y) function in the random module, returns a random integer between x and y
print("result_3 is", result_3)

names = ["Amaryllis", "Godson", "Emily", "Reina", "Derin", "Elena", "Inacio"]
print("Original names: ", names)

r.shuffle(names) #access the shuffle(x) function in the random module, shuffles the elements in the collection of elements X
print("Names after shuffling: ", names)

result_4 = r.choice(names) #access the choice(x) funcition in the random module, makes a random choice from the elements in the collection X
print("Chosen name is: ", result_4)

