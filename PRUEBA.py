# def factorial(n):
#     if n < 2:
#         return 1
#     else:
#         print(n)
#         return factorial(n - 1)

# print(factorial(200))

# def sum_positive_numbers(n):
#     if n < 1:
#         return n
#     return n + sum_positive_numbers(n - 1)

# print(sum_positive_numbers(4)) # Should be 6
# print(sum_positive_numbers(5)) # Should be 15

# def is_power_of(number, base):
#   # Base case: when number is smaller than base.
#   if number < base:
#     # If number is equal to 1, it's a power (base**0).
#     if number == 1:
#         return True
#   number / base
#   return is_power_of(number, base)

# print(is_power_of(8,2)) # Should be True
# print(is_power_of(64, 4)) # Should be True
# print(is_power_of(70, 10)) # Should be False

# def factorial(n):
#     result = n
#     start = n
#     n -= 1
#     while n > 0: # The while loop should execute as long as n is greater than 0
#         result *= n # Multiply the current result by the current value of n
#         start -= 1 # Decrement the appropriate variable by -1
#     return result


# print(factorial(3)) # Should print 6
# print(factorial(9)) # Should print 362880
# print(factorial(1)) # Should print 1

# def countdown(start):
#     x = start
#     if x > 0:
#         return_string = "Counting down to 0: "
#         while x < start  # Complete the while loop
#             ___ # Add the numbers to the "return_string"
#             if x > 0:
#                 return_string += ","
#             ___ # Decrement the appropriate variable
#     else:
#         return_string = "Cannot count down to 0"
#     return return_string

# num1 = 0
# num2 = 0

# for x in range(5):
#     num1 = x
#     for y in range(14):
#         num2 = y + 3

# print(num1 + num2)

# number = 15 # Initialize the variable
# while number >= 5: # Complete the while loop condition
#     print(number, end=" ")
#     number -= 5 # Increment the variable

# # Should print 15 10 5 

# number = 5
# while number >= 0:
#     print(number)
#     number -= 1
# # Should print:
# # 5
# # 4
# # 3
# # 2
# # 1
# # 0

# def factorial(n):
#     result = n
#     start = n
#     n -= 1
#     while n > 0: # The while loop should execute as long as n is greater than 0
#         result *= n # Multiply the current result by the current value of n
#         n -= 1 # Decrement the appropriate variable by -1
#     return result


# print(factorial(3)) # Should print 6
# print(factorial(9)) # Should print 362880
# print(factorial(1)) # Should print 1

# def rows_asterisks(rows):
#     # Complete the outer loop range to control the number of rows
#     for x in range(rows + 1): 
#         # Complete the inner loop range to control the number of 
#         # asterisks per row
#         for y in range(x): 
#             # Prints one asterisk and one space
#             print("*", end=" ")
#         # An empty print() function inserts a line break at the 
#         # end of the row 
#         print()


# rows_asterisks(5)
# # Should print the asterisk rows shown above

# def countdown(start):
#     x = start
#     if x > 0:
#         return_string = "Counting down to 0: "
#         while x >= 0: # Complete the while loop
#             return_string += str(x) # Add the numbers to the "return_string"
#             if x > 0:
#                 return_string += ","
#             x -= 1 # Decrement the appropriate variable
#     else:
#         return_string = "Cannot count down to 0"
#     return return_string


# print(countdown(10)) # Should be "Counting down to 0: 10,9,8,7,6,5,4,3,2,1,0"
# print(countdown(2)) # Should be "Counting down to 0: 2,1,0"
# print(countdown(0)) # Should be "Cannot count down to 0"

# def all_numbers(minimum, maximum):

#     return_string = "" # Initializes variable as a string

#     # Complete the for loop with a range that includes all 
#     # numbers up to and including the "maximum" value.
#     for x in range(minimum, maximum + 1):

#         # Complete the body of the loop by appending the number
#         # followed by a space to the "return_string" variable.
#         return_string += str(x) + " "

#     # This .strip command will remove the final " " space 
#     # at the end of the "return_string".
#     return return_string.strip()


# print(all_numbers(2,6))  # Should be 2 3 4 5 6
# print(all_numbers(3,10)) # Should be 3 4 5 6 7 8 9 10
# print(all_numbers(-1,1)) # Should be -1 0 1
# print(all_numbers(0,5))  # Should be 0 1 2 3 4 5
# print(all_numbers(0,0))  # Should be 0

# def test_code(num):
#   x = num
#   while x % 2 == 0:
#     x = x / 2

# test_code(10)

# operation = 0

# def sum_positive_numbers(n):
#   operation = 0
#   if n < 1:
#     return operation
#   else: 
#     operation += n
#     print(operation)
#   sum_positive_numbers(n-1)



# print(sum_positive_numbers(3)) # Should be 6
# print(sum_positive_numbers(5)) # Should be 15

# #
# variable = ["Hello", "World", "Says", "Me"]

# print(" ".join(variable))

# def is_palindrome(input_string):
#     new_string = ""
#     reverse_string = ""
#     for letter in input_string:
#         if letter != " ":
#             new_string += letter
#             reverse_string = letter + reverse_string
#     if new_string.lower() == reverse_string.lower():
#         return True
#     return False

# print(is_palindrome("Never Odd or Even")) # Should be True
# print(is_palindrome("abc")) # Should be False
# print(is_palindrome("kayak")) # Should be True

def replace_ending(sentence, old, new):
    if sentence.endswith(old):
        i = sentence[sentence.index(old):-1]
        # new_sentence = 
        return i

    return sentence
    
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
print(replace_ending("The weather is nice in May", "may", "april")) 
print(replace_ending("The weather is nice in May", "May", "April")) 

