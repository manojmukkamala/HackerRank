# ### Strings

# sWAP cASE
def swap_case(s):
    return s.swapcase()
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# String Split and Join
def split_and_join(line):
    # write your code here
    line = line.split()
    return "-".join(line)
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


# What's Your Name?
def print_full_name(a, b):
    print("Hello {0} {1}! You just delved into python.".format(a, b))
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


# Mutations
def mutate_string(string, position, character):
    return string[:position]+character+string[(position+1):]
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# Find a string
def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)-len(sub_string)+1):
        if((string[i:(i+len(sub_string))]) == sub_string):
            count += 1
    return count
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


# String Validators
if __name__ == '__main__':
    s = input()
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.isupper() for c in s))
    print(any(c.islower() for c in s))


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
    return textwrap.fill(string, max_width)
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# String Formatting
def print_formatted(number):
    # your code goes here
    w = len(bin(number)[2:])
    for i in range(1, number+1): 
        print(str(i).rjust(w, ' '), str(oct(i)[2:]).rjust(w, ' '), str(hex(i)[2:]).rjust(w, ' '), str(bin(i)[2:]).rjust(w, ' '), sep = ' ')
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
