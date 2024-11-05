
Below are the examples that show you how to work with Python lists using two techniques:

- a **`for` loop** (a more traditional approach)
- **list comprehension** (a shorter and more modern approach)

### 1. **Creating a List of Squares**

#### Without List Comprehension (Using a `for` Loop)
```python
# Create a list of squares for numbers 1 through 5
squares = []
for x in range(1, 6):
    squares.append(x**2)
print(squares)
```
**Output:**
```
[1, 4, 9, 16, 25]
```

#### With List Comprehension
```python
# Create a list of squares for numbers 1 through 5
squares = [x**2 for x in range(1, 6)]
print(squares)
```
**Output:**
```
[1, 4, 9, 16, 25]
```

---

### 2. **Filtering Even Numbers**

#### Without List Comprehension (Using a `for` Loop)
```python
# Get a list of even numbers from 1 to 10
even_numbers = []
for x in range(1, 11):
    if x % 2 == 0:
        even_numbers.append(x)
print(even_numbers)
```
**Output:**
```
[2, 4, 6, 8, 10]
```

#### With List Comprehension
```python
# Get a list of even numbers from 1 to 10
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)
```
**Output:**
```
[2, 4, 6, 8, 10]
```

---

### 3. **Converting Strings to Uppercase**

#### Without List Comprehension (Using a `for` Loop)
```python
# Convert a list of strings to uppercase
words = ["apple", "banana", "cherry"]
uppercase_words = []
for word in words:
    uppercase_words.append(word.upper())
print(uppercase_words)
```
**Output:**
```
['APPLE', 'BANANA', 'CHERRY']
```

#### With List Comprehension
```python
# Convert a list of strings to uppercase
words = ["apple", "banana", "cherry"]
uppercase_words = [word.upper() for word in words]
print(uppercase_words)
```
**Output:**
```
['APPLE', 'BANANA', 'CHERRY']
```
---

### 4. **Extracting the First N Elements of a List**

#### Without List Comprehension (Using a `for` Loop)
In this example, we will extract the first `n` elements from a list.

```python
# Extract the first N elements from a list
numbers = [10, 20, 30, 40, 50, 60, 70]
n = 4
first_n_elements = []
for i in range(n):
    first_n_elements.append(numbers[i])
print(first_n_elements)
```
**Output:**
```
[10, 20, 30, 40]
```

#### With List Comprehension
Using list comprehension, this same task can be completed with fewer lines of code.

```python
# Extract the first N elements from a list
numbers = [10, 20, 30, 40, 50, 60, 70]
n = 4
first_n_elements = [numbers[i] for i in range(n)]
print(first_n_elements)
```
**Output:**
```
[10, 20, 30, 40]
```

*Explanation:* Both methods *iterate* (loop) through the first `n` elements of the `numbers` list and add them to a new list. The list comprehension does it in a single line, while the `for` loop requires you to first create a list and then add items to your list using the `append()` method.

---

### 5. **Making a New List of Words that Start with a Vowel**

#### Without List Comprehension (Using a `for` Loop)
In this example, we will create a new list containing only the words that start with a vowel.

```python
# Make a list of words that start with a vowel
words = ["apple", "banana", "orange", "umbrella", "grape"]
vowels = "aeiou"
vowel_words = []
for word in words:
    if word[0].lower() in vowels:
        vowel_words.append(word)
print(vowel_words)
```
**Output:**
```
['apple', 'orange', 'umbrella']
```

#### With List Comprehension
You can achieve the same result with list comprehension.

```python
# Make a list of words that start with a vowel
words = ["apple", "banana", "orange", "umbrella", "grape"]
vowels = "aeiou"
vowel_words = [word for word in words if word[0].lower() in vowels]
print(vowel_words)
```
**Output:**
```
['apple', 'orange', 'umbrella']
```

---

### Summary of Differences:

- **Using `for` loops** requires more lines of code, as you manually create and then add items to your list.
- **List comprehension** streamlines the process of creating and adding items to a list into a single line of code, making your code easier to read and maintain. It's especially helpful when you just need to create or modify lists based on some condition or math operation.
  
