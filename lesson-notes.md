# Lesson Notes
## Python List Comprehensions

### Directions
- Read these notes and check out the related resources before you start writing any code for this lesson

### Related Resources
- In *Python Crash Course*, see pp. 59 60 (List Comprehensions)
- [Python List Comprehension](https://www.programiz.com/python-programming/list-comprehension)


### Notes

- *List comprehension* means:
    - you're making a NEW list by changing or doing something to the values in an existing list
- Example: You have a list named *numbers* that contains the numbers 1, 2, 3 and 4
- Using list comprehension, you create a NEW list named *doubled* by taking each number in the original list and multiplying it by 2
- Your *doubled* list would then contain the numbers 2, 4, 6 and 8
- You can modify numbers or strings (text data) using list comprehension
- Of course, you can use a traditional `for` loop to create a new Python list, but usually the code for doing so is cleaner and more concise if you use **list comprehension** instead

```
# Making a new list using a FOR loop
numbers = [1, 2, 3, 4, 5]
squared_numbers = []

# for loop to square each list element
for num in numbers:
    squared_numbers.append(num * num)
    
print(squared_numbers)

# Output: [1, 4, 9, 16, 25]

# Using a FOR loop to make a list of squared numbers
numbers = [1, 2, 3, 4, 5]

# Create a NEW list using list comprehension
squared_numbers = [num * num for num in numbers]

print(squared_numbers)

# Output: [1, 4, 9, 16, 25]
```
