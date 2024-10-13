

#--------------- PROBLEM 1 ------------------
#-------------INTRODUCTION-------------------
# Solved: 7/7

# Say "Hello, World!" With Python
print("Hello, World!")

# Python If-Else
n = int(input())

if n % 2 == 0:
    if n >= 6 and n <= 20:
        print("Weird")
    elif n >= 2 and n <= 5:
        print("Not Weird")
    elif n > 20:
        print("Not Weird")
elif n % 2 == 1:
    print("Weird")
        
# Arithmetic Operators

a = int(input())
b = int(input())
print(a+b)
print(a-b)
print(a*b)

# Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

# Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)

# Write a Function
def is_leap(year):
    leap = False
    if year % 100 == 0 and year % 4 == 0:
        if year % 400 == 0:
            leap = True
    elif year % 4 == 0:
        leap = True
    return leap

year = int(input())
print(is_leap(year))

# Print Function
if __name__ == '__main__':
    n = int(input())
    list = []
    i = 0
    while i < n:
        i += 1
        list.append(str(i))
    print("".join(list))

#-------------BASIC DATA TYPES---------------
# Solved: 5/6
# Missing: Tuples

# List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

print(list([i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n))


# Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

new_arr = list(arr)
for i in range(len(new_arr)):
    for j in range(len(new_arr)-i-1):
        if new_arr[j] < new_arr[j+1]:
            new_arr[j], new_arr[j+1] = new_arr[j+1], new_arr[j]

first = new_arr[0]
for i in new_arr:
    if i == first:
        continue
    elif i != first:
        print(i)
        break

# Nested Lists
if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    rec_sor = sorted(records, key= lambda record:record[1])
    #print(rec_sor)
    lowest = rec_sor[0][1]
    second = 0
    sec_names = []
    for i in rec_sor:
        if i[1] == lowest:
            continue
        elif i[1] > lowest and second == 0:
            second += i[1]
            sec_names.append(i[0])
            #print(i[0])
        elif i[1] == second:
            #print(i[0])
            sec_names.append(i[0])
        else:
            break
    names = sorted(sec_names)
    for name in names:
        print(name)

# Finding the percentage
import decimal
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

sum_of_marks= 0
number_of_marks = 0
for i in student_marks[query_name]:
    sum_of_marks += i
    number_of_marks += 1
marks_mean = sum_of_marks/number_of_marks

print("%.2f" % marks_mean)

# Lists
if __name__ == '__main__':
    N = int(input())
    arr = []
    for i in range(0,N):
        input_str = input()
        i_list = input_str.split()
        if i_list[0] == 'append':
            arr.append(int(i_list[1]))
        elif i_list[0] == 'remove':
            arr.remove(int(i_list[1]))       
        elif i_list[0] == 'reverse':
            arr.reverse()
        elif i_list[0] == 'sort':
            arr.sort()
        elif i_list[0] == 'print':
            print(arr)
        elif i_list[0] == 'pop':
            arr.pop()
        elif i_list[0] == 'insert':
            arr.insert(int(i_list[1]), int(i_list[2]))

# Tuples
#
#
#
#
#-------------STRINGS-----------------
# Solved: 14/14

# sWAP cASE
def swap_case(s):
    new_s = ""
    for i in range(len(s)):
        if s[i].islower():
            new_s += s[i].upper()
        elif s[i].isupper():
            new_s += s[i].lower()
        else:
            new_s += s[i]
    return new_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# String Split and Join
def split_and_join(line):
    # write your code here
    return '-'.join(line.split())

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# What's Your Name?

def print_full_name(first, last):
    # Write your code here
    print('Hello {first} {last}! You just delved into python.'.format(first=first, last=last) )

def split_and_join(line):
    # write your code here
    return '-'.join(line.split())


# Mutations
def mutate_string(string, position, character):
    new_str = list(string)
    new_str[position] = character
    new_str2 = "".join(new_str)
    return new_str2

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# Find a string
def count_substring(string, sub_string):
    count =0
    for i in range(0, len(string)):
        if string[i: i+len(sub_string)] == sub_string:
            count +=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

# String Validators
if __name__ == '__main__':
    s = input()
    num = False
    alpha = False
    digit = False
    lower = False
    upper = False
    for i in s:
        if i.isalnum():
            num = True
        if i.isalpha():
            alpha = True
        if i.isdigit():
            digit = True
        if i.islower():
            lower = True
        if i.isupper():
            upper = True
        
    list = (num, alpha, digit, lower, upper)
    for i in list:
        print(i)


# Text Alignment
#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))



# Text Wrap
import textwrap

def wrap(string, max_width):
    '''m = 0
    n = int(max_width)
    length = int(len(string)/max_width)
    for i in range(length):
        print(string[m:n])
        m += max_width
        n += max_width'''
    lines = int((len(string)/max_width))
    return '\n'.join(textwrap.wrap(string, width = max_width))#, max_lines = lines))
        

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# Designer Door Mat

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
n,m = input().split()
n = int(n)
m = int(m)
m_half = int(math.floor(m/2))
m_border = m_half-3
s = "-"
p = ".|."
i = 1
j = 1
for k in range(math.floor(n/2)):
    print((s*(m_half-i)) + p*(j) + (s*(m_half-i)))
    i += 3
    j += 2
print(s*m_border+"WELCOME"+s*m_border)
i += -3
j += -2
for k in range(math.floor(n/2)):
    print((s*(m_half-i)) + p*(j) + (s*(m_half-i)))
    i += -3
    j += -2


# String Formatting
import math
def print_formatted(number):
    # your code goes here
    def binary(n):
        list = []
        i = n
        while i>0:
            remainder = str(i%2)
            list.append(remainder)
            i = math.floor(i/2)
        return "".join(list[::-1])
    def octal(n):
        if n < 8:
            return n
        else:
            list = []
            while n > 7:
                remainder = str(n%8)
                list.append(remainder)
                n = math.floor(n/8)
            return str(n)+"".join(list[::-1])
            
    def hexadec(n):
        h = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
        list = []
        while n > 15:
            remainder = int(n%16)
            list.append(h[remainder])
            n = math.floor(n/16)
        return h[n]+"".join(list[::-1])
    i = 1
    b = binary(number)
    l = len(b)
    while i in range(number+1):
        '''print("{i:>l} {oct:>{l}} {:>{l}} {:>{l}}".format(i,octal(i), hexadec(i),b))
'''
        print("{:>{}}".format(i,l),"{:>{}}".format(octal(i),l), "{:>{}}".format(hexadec(i),l), "{:>{}}".format(binary(i),l))
        i+=1
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

# Alphabet Rangoli
def print_rangoli(size):
    # your code goes here
    alp = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    '''for i in reversed(range(size)):
        print(alp[i])
    return i
    i = size
    while i > 0:
        print(alp[i-1])
        i += -1'''
    if size == 1:
        return print(alp[size-1])
    i = size
    n_slash = int((4*size-4)/2)
    s = "-"
    for j in reversed(range(size)):
        if j == size-1:
            new_list = alp[j:i]
            joint = s*n_slash+s.join(new_list[::-1]) +s+ s.join(new_list[1:])+ s*(n_slash-1)
            print(joint)
            n_slash = n_slash - 2
        else:
            new_list = alp[j:i]
            joint = s*n_slash+s.join(new_list[::-1]) +s+ s.join(new_list[1:])+ s*n_slash
            print(joint)
            n_slash = n_slash - 2
        if len(new_list) == size:
            n_slash = 2
            for j in range(size-1):
                if j == size-2:
                    new_list = alp[j+1:i]
                    joint = s*n_slash + s.join(new_list[::-1]) +s+ s.join(new_list[1:])+ s*(n_slash-1)
                    print(joint)
                    n_slash += 2
                else:
                    new_list = alp[j+1:i]
                    joint = s*n_slash + s.join(new_list[::-1]) +s+ s.join(new_list[1:])+ s*n_slash
                    print(joint)
                    n_slash += 2
            break
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

# Capitalize!
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    print(s)
    new_s = ""
    i = 0
    while i in range(len(s)):
        if i == 0:
            new_s += s[i].upper()
            i += 1
        elif s[i] == " ":
            if s[i+1] == " ":
                new_s += " "
                i += 1
            else:
                new_s += " "+s[i+1].upper()
                i += 2
        else:
            new_s += s[i]
            i += 1
    return new_s
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

# The Minion Game
def minion_game(string):
    # your code goes here
    vowels = ["A", "E", "I", "O", "U"]
    c_list = []
    v_list = []
    c_count = 0
    v_count = 0
    for i in range(len(string)):
        if string[i] in vowels:
            v_count += len(string) - i
            '''j = i+1
            while j in range(len(string)+1):
                #if string[i:j] not in v_list:
                #v_list.append(string[i:j])
                v_count += 1
                j+=1
        else:
            continue'''
    for i in range(len(string)):
        if string[i] not in vowels:
            c_count += len(string) - i
            '''j = i+1
            while j in range(len(string)+1):
                #if string[i:j] not in c_list:
                #c_list.append(string[i:j])
                c_count += 1
                j+=1
        else:
            continue
        elif string[i] not in vowels:
            j = i+1
            while j in range(len(string)+1):
                #if string[i:j] not in c_list:
                #c_list.append(string[i:j])
                c_count += 1
                j+=1'''
    stuart = c_count
    kevin = v_count
    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    elif stuart == kevin:
        print("Draw")
    #print(c_list, v_list)
if __name__ == '__main__':
    s = input()
    minion_game(s)

# Merge the Tools!
def merge_the_tools(string, k):
    # your code goes here
    n = int(len(string)/k)
    i = 0
    j = k
    s = set()
    for m in range(n):
        sub = string[i:j]
        for i in range(j-i):
            s.add(sub[i])
        i += k
        j += k
        '''
        if s[0] == s[1]:
            s = s[0]+s[2]
        elif s[0] == s[2]:
            s = s[:1]
        elif s[1] == s[2]:
            s = s[:1]
        
        if s.count(s[0]) > 1:
            s = s.strip(s[0])
        elif s.count(s[1]) > 1:
            s = s.strip(s[1])
        '''
        print(s)
        s = set()
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


#----------------------Sets-----------------------
# Solved: 13/13

# Introduction to Sets
def average(array):
    # your code goes here
    h = set(map(float, array))
    avg = sum(h)/(len(h))
    #print(avg)
    return round(avg, 3)
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

# No Idea!
n,m = input().split()
arr = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))
#print(arr)
count = 0
for i in arr:
    if i in a:
        count += 1
    if i in b:
        count += -1
print(count)


# Symmetric Difference
m = int(input())
m_numbers = input().split()
n = int(input())
n_numbers = input().split()

m_num = list(map(int,m_numbers))
n_num = list(map(int,n_numbers))
#print(m, m_num)
m_set = set(m_num)
n_set = set(n_num)

dif = m_set.difference(n_set)
dif.update(n_set.difference(m_set))
dif = sorted(list(dif))
for i in dif:
    print(i)#, n_set.difference(m_set))

# Set .add()

s = set()
N = int(input()) 
for i in range(N):
    s.add(input())
l = []
count = 0
for i in s:
    if type(i) == str:
          if i not in l:
              l.append(i)
              count +=1
    else: count += 0
print(count)

# Set .discard(), .remove() & .pop()
if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    N = int(input())
    sum = 0
    if (N<20 and N>0 and n<20 and N>0):
        for j in range(N):
            cmd = input().split()
            if (cmd[0] == 'remove'):
                if int(cmd[1]) in s:
                    s.remove(int(cmd[1]))
                else: 
                    continue
            elif (cmd[0] == 'pop'):
                s.pop()
            elif (cmd[0] == 'discard'):
                if int(cmd[1]) in s:
                    s.discard(int(cmd[1]))
                else:
                    continue
        for i in s:
            sum += i
        print(sum)

# Set .union() Operation
if __name__ == '__main__':
    n = int(input())
    n_numbers = set(input().split(" "))
    b = int(input())
    b_numbers = set(input().split(" "))
    all = b_numbers.union(n_numbers)
    total = 0
    for i in all:
        total+=1
    print(total)


# Set .intersection() Operation
if __name__ == '__main__':
    n = int(input())
    n_set = set(input().split(" "))
    b = int(input())
    b_set = set(input().split(" "))
    sum = 0
    all = b_set.intersection(n_set)
    for i in all:
        sum += 1
    print(sum)


# Set .difference() Operation
if __name__ == '__main__':
    n = int(input())
    n_set = set(input().split(' '))
    b = int(input())
    b_set = set(input().split(' '))
    sum = 0
    diff = n_set.difference(b_set)
    for i in diff:
        sum += 1
    print(sum)
    
# Set .symmetric_difference() Operation
e = int(input())
eng = set(input().split())
f = int(input())
french = set(input().split())

dif = eng.difference(french)
dif.update(french.difference(eng))
print(len(dif))

# Set Mutations
a = int(input())
a_set = set(map(int,input().split()))
m = int(input())

for i in range(m):
    op, l = input().split()
    n = set(map(int,input().split()))
    if op == "intersection_update":
        a_set.intersection_update(n)
    elif op == "update":
        a_set.update(n)
    elif op == "symmetric_difference_update":
        a_set.symmetric_difference_update(n)
    elif op == "difference_update":
        a_set.difference_update(n)
        
print(sum(list(map(int,a_set))))


# The Captain's Room
k  = int(input())
room_list = list(map(int,input().split()))
room_set = set(room_list)
room_set2 = set(room_list)

room_list.sort()
print(room_list)
room_list.remove(1)
print(room_list)

'''
for room in room_set:
    if room_list.count(room) > 1:
        room_set2.remove(room)
    if len(room_set2) == 1:
        print("".join(str(room) for room in room_set2))
        break'''


# Check Subset
t = int(input())
sets = []
for i in range(t):
    n_a = int(input())
    a = set(map(int, input().split()))
    n_b = int(input())
    b = set(map(int, input().split()))
    
    if a.issubset(b):
        print(True)
    else:
        print(False)


# Check Strict Superset

a = set(map(int, input().split()))
n = int(input())
superset = False
#print(a)
for i in range(n):
    s = set(map(int, input().split()))
    if superset:
        if ((a.issuperset(s)) or (s.issubset(a))) == False:
            superset = False
            break
    
    superset = a.issuperset(s)
    superset = s.issubset(a)
    #print(a-s)
print(superset)

#-----------------Collections---------------------
# Solved: 4/8
# Missing: Piling Up!, Company Logo, Word Order, Collections.namedtuple()

# collections.Counter()
from collections import Counter

x = int(input())
l = list(map(int, input().split()))
shoe_sizes = Counter(l)
n = int(input())
#print(shoe_sizes)
total = 0

for i in range(n):
    customer = list(map(int, input().split()))
    n_shoes = shoe_sizes[customer[0]]
    if n_shoes != 0:
        total += customer[1]
        shoe_sizes[customer[0]] = n_shoes-1
        
print(total)

# DefaultDict Tutorial
from collections import defaultdict

integers = list(map(int,input().split()))
a = []
b = []
d = defaultdict(list)
p = 0
for i in range(integers[0]):
    d[input()].append(i+1)
for i in range(integers[1]):
    b = str(input())
    if b in d.keys():
        print(*d[b])
        #pos = "".join(str((d[b])))
        p +=1
    else:
        print(-1)
        '''
    if (i == integers[1]) and (p == 0):
        print(-1)'''
   
# Collections.OrderedDict()
from collections import OrderedDict
from collections import Counter
import re

d = OrderedDict()
n = int(input())
l = []
for i in range(n):
    order = input()
    
    name = re.search(r"[A-Z\s]*(?=[0-9])", order).group()
    price = re.search(r"[0-9]+",order).group()
    d[name] = price
    l.append(name)
rep = Counter(l)
for k,v in d.items():
    #print(k)
    #print(v) 
    #print(rep[k])
    print(k[:-1], int(v)*int(rep[k])) 

# Collections.deque()
from collections import deque

n = int(input())
d = deque()
for i in range(n):
    command = list(input().split())
    if command[0] == "append":
        d.append(command[1])
    elif command[0] == "appendleft":
        d.appendleft(command[1])
    elif command[0] == "popleft":
        d.popleft()
    elif command[0] == "pop":
        d.pop() 
        
print(*(d))

#-------------------DATE AND TIME-----------------
# Solved: 1/2
# Missing: Time Delta

# Calendar Module
import calendar
month, day, year = input().split()
#print(month,day,year)
days_in_week = ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
print(days_in_week[int(calendar.weekday(int(year),int(month),int(day)))])

#-------------------EXCEPTIONS-------------------------
# Solved: 1/1
# Exceptions
n = int(input())
for i in range(n):
    a, b = input().split()
    try: print(int(a)//int(b)) 
    except ZeroDivisionError as e:
        print("Error Code:", e)# integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:", e)

#----------------------BUILT-INS-------------------------
# Solved: 3/3

# Zipped!
import statistics as s

students, n_grades = input().split()

y = []
for i in range(int(n_grades)):
    l = [float(x) for x in input().split()]
    y.append(l)

'''for i in range(int(students)):
    a = map(int, input())
    list.append(a)'''
zipped = list(zip(*y))
for i in zipped:
    print(s.mean(i))
# Python Sort Sort

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    arr_1 = arr.sort(key = lambda arr: arr[k])
    for i in arr:
        print(*i)

# Ginorts
s = input()
low = []
upper = []
odd = []
even = []
e="24680"
o="13579"
for i in range(len(s)):
    if s[i].islower():
        low.append(s[i])
    elif s[i].isupper and s[i] not in e and s[i] not in o:
        upper.append(s[i])
    elif s[i] in e:
        even.append(s[i])
    elif s[i] in o:
        odd.append(s[i])
    
rev = ''.join(sorted(low)) + ''.join(sorted(upper)) + ''.join(sorted(odd)) + ''.join(sorted(even))
print(rev)

#----------------FUNCTIONALS-----------------------
# Solved: 1/1

# Map and Lambda Function
cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    n = n
    l = []
    for i in range(n):
        if l == []:
            l.append(0)
        elif len(l) == 1:
            l.append(1)
        else:
            l.append(l[-1]+l[-2])
        #print(l)
    return l
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

#-------------REGEX AND PARSING CHALLENGES-----------------
# Solved: 10/17
# Missing: Re.start()&Re.end(), Validating Roman Numerals, HTML Parser - Part1, HTML Parser - Part 2, 
# Missing: Detect HTML Tags, Attributes and Attribute Values, Validating Postal Codes, Matrix Script

# Detect Floating Point Number
import re

t = int(input())
for i in range(t):
    s = input()
    '''
    m = bool(re.search(r"""((\A\+{1}(?=\.{1}|\d\.))
                            |((A-{1})(?=\.{1}|\d\.))
                            |(\A\.{1})
                            |(\A\d\.)\d+""",s))
    #m = bool(re.search(r"\A"))
    '''
    m = bool(re.search(r"\A((\+|\+\d+)|(\-|\-\d+)|(\d+))\.{1}\d+", s))
    try: 
        float(s)
    except Exception:
        m = False
    print(m)

# Re.split()
regex_pattern = r"\,|\."	# Do not delete 'r'.
import re
print("\n".join(re.split(regex_pattern, input())))

# Group(), Groups() & Groupdict()
import re

s = input()
s = re.sub(r"_",r"+",s)
position = re.search(r"(\w+)\1", s)

if bool(re.search(r"(\w+)\1", s)) == False:
    print("-1")
else:
    print(position.group(0)[0])


# Re.findall() & Re.finditer()

import re

s = input()

vowel_list = list(map(lambda x: x.group(), re.finditer(r"(?<=[b-dfghj-np-tv-z])[aeiou]{2,}(?=[b-dfghj-np-tv-z])", s, re.IGNORECASE)))
if bool(re.findall(r"(?<=[b-dfghj-np-tv-z])[aeiou]{2,}(?=[b-dfghj-np-tv-z])", s, re.IGNORECASE)) == False:
    print("-1")
else:
    for i in vowel_list:
        print(i)


# Regex Substitiution
import re

lines = []
n = int(input())
for i in range(n):
    lines.append(input())
text = "\n".join(lines)
    
#print(text)
text_and = re.sub(r" &{2} ", r" and ", text, re.MULTILINE)
text_and = re.sub(r" &{2} ", r" and ", text_and, re.MULTILINE)
text_or = re.sub(r" \|{2} ", r" or ", text_and, re.MULTILINE)
#print(text_and)
print(text_or)

# Validating phone numbers
import re

n = int(input())

for i in range(n):
    s = input()
    phone_n = re.fullmatch(r"^([789]{1})(\d{9})", s)
    if bool(phone_n):
        print("YES")
    else:
        print("NO")


# Validating and Parsing Email Addresses
import re
import email.utils

n = int(input())

for i in range(n):
    #name, mail = email.utils.parseaddr(input())
    name, mail = input().split()
    #s = re.fullmatch(r"<"+re.escape(name)+ r"[a-z0-9-_]*" + r"([\w\-]?)+@([a-z]).([a-z]{1,3})>", mail)
    s = re.search(r"(\A<[a-z]{1,})([a-z0-9._-]+)?@([a-z])+\.([a-z]{1,3})>", mail)
    #([a-z0-9._-]+)?@([a-z])+\.([a-z]{1,3})>", mail)
    #print(s, name, mail)
    if bool(s):
        #print(email.utils.formataddr((name, mail)))
        print(name, mail)
        #print(s)

# Hex Color Code
import re

n = int(input())
open = False
for i in range(n):
    s = input()
    if "{" in s:
        open = True 
    elif "}" in s:
        open = False
    if (open == True) and ("{" not in s) :
        l = len(s) -1
        #print(s)
        # search first for the position of # and then for the expression
        color = re.findall(r"(?:(#[a-fA-F0-9]{6})|(#[a-fA-F0-9]{3}))", s)
        #color2 = re.search("(#[a-fA-F0-9]{6})", s)
        color2 = list(map(lambda x: x.group(), re.finditer(r"(?:(#[a-fA-F0-9]{6})|(#[a-fA-F0-9]{3}))", s, re.IGNORECASE)))
        '''
        if bool(re.search(r"(?:(#[a-fA-F0-9]{6})|(#[a-fA-F0-9]{3}))", s)) == True:
            if color[0] == "":
                print(color[1])
            elif color:'''
        #if bool(re.search("([a-fA-F0-9]{6})", s)):
            #print(color2.group(0))
        #print(color)
        for i in color2:
            print(i)
    else:
        continue


# Validating UID
import re

l = []
t = int(input())
for i in range(t):
    s = input()
    uid = False
    '''
    if bool(re.fullmatch(w{10}, s, flags=ascii)):
        print("Valid")
    else:
        print("Invalid")
    '''
    new_s = sorted(s)
    l = "".join(new_s)
    #print(re.fullmatch(r"(\w{10})", s))
    #print(re.search)
    if bool(re.fullmatch(r"\w{10}", s)):
        #print(1)
        if bool(re.search(r"(.)\1", l)) == False:
            
            #if re.search(r"\w", s, ):
                #print(3)
            
            number = 0
            upper = 0
            l = "".join(new_s)
            for i in new_s:
                if i in "1234567890":
                    number += 1
                elif i in "QWERTYUIOPASDFGHJKLZXCVBNM":
                    upper += 1
            if (number >= 3) and (upper >= 2):
                uid = True
            else:
                uid = False
            '''
            # problematic expression: n of times a char appears not necessarily consecutively
            if bool(re.search(r"", s)):
                print(3)
                if bool(re.search(r"[A-Z]{2,}", s)):
                    uid = True'''
    if uid == True:
        print("Valid")
    else:
        print("Invalid")


# Validating Credit Card Numbers
import re

n = int(input())

for i in range(n):
    s = input()
    m = re.fullmatch(r"(\A[456]{1})([0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})", s)
    p = re.sub(r"-", r"", s)
    n = re.search(r"(.)\1{3}", p)
    #print(bool(n))
    #print(p)
    if bool(m) and bool(n) == False:
        print("Valid")
    else:
        print("Invalid")

#------------------------XML---------------------
# Solved: 1/2
# Missing: XML2 - Find the Maximum Depth

# XML 1 - Find the Score
import sys
import xml.etree.ElementTree as etree
def get_attr_number(node):

    # your code goes here
    n_attrib = 0
    for child in node.iter():
        n_attrib += len(child.attrib)
        
    #print(node)
    '''
    print(len(node))
    for i in range(len(node)):
        n_attrib += len(node[i].attrib)
        #print(i)
        print(node[i])
        print(n_attrib)
    '''
    return n_attrib
if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))

#-------------CLOSURES AND DECORATIONS-------------------
# Solved: 1/2
# Missing: Decorators 2 - Name Directory

# Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        numbers = []
        for i in l:
            if len(i) == 12:
                n = "+91 "+ i[2:7] + " "+i[7:]
            elif len(i) == 10:
                n = "+91 "+ i[:5] +" "+ i[5:]
            elif i[0] and len(i) == 11:
                n = "+91 "+ i[1:6] + " "+i[6:]
            elif "+" in i:
                n = "+91 "+ i[3:8] + " "+i[8:]
            numbers.append(n)
        numbers = sorted(numbers)
        #print(*numbers, sep = "\n")
        for i in numbers:
            print(i)
        # complete the function
    return fun
@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 



#------------------NUMPY----------------------------------
# Solved: 15/15

# Arrays
import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    arr = numpy.array(arr)
    arr = arr[::-1]
    arr = arr.astype(float)
    return arr
arr = input().strip().split(' ')
result = arrays(arr)
print(result)

# Shape and Reshape
import numpy

arr = numpy.array(input().split())
arr = arr.astype(int)
arr.shape = (3, 3)
print(arr)

# Transpose and Flatten
import numpy

l = list(map(int, input().split()))
#print(l)
a = list()
for i in range(l[0]):
    a.append(numpy.array(input().split(), dtype = int))
arr = numpy.array(a)
print(numpy.transpose(arr))
print(arr.flatten())
    

# Concatenate
import numpy
n,m,p = list(map(int,input().split()))
a = []
b = []
for i in range(n+m):
    arr = numpy.array(input().split(), dtype = int)
    a.append(arr)
a = numpy.array(a)
'''
for i in range(n,n+m):
    arr = numpy.array(input().split(), dtype = int)
    b.append(arr)
b = numpy.array(b)
#print(a) 
#print(b)
#print(a+b)'''
print(a)
# Zeros and Ones
import numpy
z = list(map(int,input().split()))
#i = int(i)
#j = int(j)
#k = int(k)
#print(i,j,k)
#for m in range(k):
print(numpy.zeros((z), dtype = int)) 

print(numpy.ones((z), dtype = int))


# Eye and Identity
import numpy
numpy.set_printoptions(legacy='1.13')

n,m = list(map(int, input().split()))
print(numpy.eye(n,m))


# Array Mathematics
import numpy
n,m = list(map(int, input().split()))

a = []
b = []
for i in range(n):
    arr = numpy.array(input().split(), dtype = int)
    a.append(arr)
a = numpy.array(a)

for i in range(n):
    arr = numpy.array(input().split(), dtype = int)
    b.append(arr)
b = numpy.array(b)
#print(a) 
#print(b)
print(numpy.add(a,b))
print(numpy.subtract(a,b))
print(numpy.multiply(a,b))
print(numpy.floor_divide(a,b))
print(numpy.mod(a,b))
print(numpy.power(a,b))


# Floor, Ceil and Rint
import numpy
numpy.set_printoptions(legacy='1.13')

arr = list(map(float,input().split()))
arr = numpy.array(arr)

print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))


# Sum and Prod
import numpy

n,m = list(map(int, input().split()))

a = []
for i in range(n):
    arr = numpy.array(input().split(), dtype = int)
    a.append(arr)
a = numpy.array(a)
sum_a = numpy.sum(a, axis = 0)
print(numpy.prod(sum_a))

# Min and Max
import numpy
l = list(map(int,(input().split())))
s = []
for i in range(l[0]):
    arr = numpy.array(input().split(), dtype = int)
    s.append(arr)
s = numpy.array(s)
print(numpy.max(numpy.min(s, axis = 1)))


# Mean, Var and Std
import numpy

l = list(map(int, input().split()))
m = []
for i in range(l[0]):
    arr = numpy.array(input().split(), dtype = int)
    m.append(arr)
m = numpy.array(m)
#print(m)
print(numpy.mean(m, axis = 1))
print(numpy.var(m, axis = 0))
print(round(numpy.std(m, axis = None), 11))

# Dot and Cross
import numpy

n = input()
n = int(n)
a = []
b = []
for i in range(n):
    arr = numpy.array(input().split(), dtype = int)
    a.append(arr)
a = numpy.array(a)

for i in range(n):
    arr = numpy.array(input().split(), dtype = int)
    b.append(arr)
b = numpy.array(b)
#print(a) 
#print(b)
print(numpy.matmul(a,b))

# Inner and Outer
import numpy

a = numpy.array(list(map(int, input().split())))

b = numpy.array(list(map(int, input().split())))

print(numpy.inner(a,b))
print(numpy.outer(a,b))

# Polynomials
import numpy

a = numpy.array(list(map(float, input().split())))
x = int(input())

print(numpy.polyval(a,x))


# Linear Algebra
import numpy

n = int(input())
arr = []
for i in range(n):
    a = list(map(float, input().split()))
    arr.append(a)
arr = numpy.array(arr)
print(round(numpy.linalg.det(arr),2))


#----------------------------------------------------------
#----------------------------------------------------------
#------------------- PROBLEM 2 ----------------------------

# Solved: 3/6
# Missing: Strange Advertising, Recursive Digit Sum, Insertion Sort 2

# Birthday Cake Candles
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    highest = 0 
    num = 0
    for i in range(len(candles)):
        if candles[i] > highest:
            highest = candles[i]
            num = 1
        elif candles[i] == highest:
            num += 1
        else:
            continue
    return num
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

# Kangaroo
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    
    for i in range(10000):
        if x1 == x2:
            return "YES"
            break
        else:
            x1 += v1
            x2 += v2
            #if i == 99999:
    return "NO"
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

# Insertion Sort1
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    n_sort = arr[-1]
    for i in range(1,len(arr)):
        if n_sort < arr[-i-1]:
            arr[-i] = arr[-i-1]
            print(*(arr))
            if i+1 == len(arr):
                if arr[0] < n_sort:
                    arr[1] = n_sort
                else:
                    arr[0] = n_sort
                print(*(arr))
                break
        if n_sort >= arr[-i-1]:
            
            #elif n_sort > arr[-i-1]:
            arr[-i] = n_sort
            print(*(arr))
            break

        #print(*(arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
