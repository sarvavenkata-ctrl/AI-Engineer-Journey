# Day 3 — Python Functions

## What is a Function?

A function is a reusable block of code that performs a specific task.

### Defining a Function

Example:

```python
def greet():
    print("Hello World")
```

### Calling the Function

```python
greet()  # Output: Hello World
```

## Function Parameters

Functions can accept parameters (arguments) to work with different data:

```python
def greet(name):
    print("Hello", name)

greet("Sarva")  # Output: Hello Sarva
greet("Alice")  # Output: Hello Alice
```

## Return Values

Functions can return values using the `return` keyword:

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8
```

### Arbitrary Arguments

Python allows functions to accept an arbitrary number of positional arguments using `*args`:

```python
def total_marks(*marks):
    return sum(marks)

print(total_marks(80, 75, 90))  # Output: 245
```

You can also accept arbitrary keyword arguments with `**kwargs`:

```python
def student_info(**info):
    for key, value in info.items():
        print(key, value)

student_info(name="Sarva", age=25)
```

## Key Concepts

- **Parameters**: Variables in the function definition
- **Arguments**: Actual values passed when calling the function
- **Return**: Sends a value back to the caller
- **Scope**: Variables inside a function only exist within that function

---

# 🎯 Why This Matters for AI

Functions help you:

- organize code
- reuse logic
- build ML pipelines
- structure large projects

Example in AI:

load_data()
preprocess_data()
train_model()
evaluate_model()

