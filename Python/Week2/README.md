Here are the solutions to each of your tasks:

### 1. Program that accepts user input to create a list of integers and computes the sum of all the integers in the list:

```python
# Accept user input to create a list of integers
numbers = input("Enter a list of integers separated by spaces: ").split()
numbers = [int(num) for num in numbers]

# Calculate the sum of all integers in the list
total_sum = sum(numbers)

# Output the result
print(f"The sum of the integers is: {total_sum}")
```

### 2. Create a tuple containing the names of five favorite books and print each book name on a separate line:

```python
# Create a tuple with the names of 5 favorite books
favorite_books = ("1984", "Brave New World", "To Kill a Mockingbird", "The Great Gatsby", "Moby Dick")

# Print each book name on a separate line using a for loop
for book in favorite_books:
    print(book)
```

### 3. Program that uses a dictionary to store information about a person, asking for user input, and then printing the dictionary:

```python
# Create an empty dictionary to store person info
person_info = {}

# Ask the user for input
person_info['name'] = input("Enter your name: ")
person_info['age'] = int(input("Enter your age: "))
person_info['favorite_color'] = input("Enter your favorite color: ")

# Print the dictionary
print(f"Person information: {person_info}")
```

### 4. Program that accepts user input to create two sets of integers and creates a new set that contains only the elements common to both sets:

```python
# Accept user input for the first set
set1 = set(map(int, input("Enter the integers for the first set separated by spaces: ").split()))

# Accept user input for the second set
set2 = set(map(int, input("Enter the integers for the second set separated by spaces: ").split()))

# Create a new set that contains only the elements common to both sets
common_elements = set1 & set2

# Output the result
print(f"The common elements in both sets are: {common_elements}")
```

### 5. Program that stores a list of words and uses list comprehension to create a new list containing only the words with an odd number of characters:

```python
# Store a list of words
words = ["apple", "banana", "cherry", "date", "kiwi", "orange", "pear"]

# Use list comprehension to create a new list with words that have an odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]

# Output the result
print(f"Words with an odd number of characters: {odd_length_words}")
```

These programs cover a variety of basic Python concepts such as lists, tuples, dictionaries, sets, and list comprehension.
