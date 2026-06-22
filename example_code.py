def greet_user(name):
    """A simple function to greet a user."""
    return f"Hello, {name}! Welcome to Python."

# Get input from the user
user_name = input("Enter your name: ")

# Call the function and print the result
greeting = greet_user(user_name)
print(greeting)