#My first file tracked by Git
# Author: Abril Bustos

def greet(name):
    """Return a wellcome message for the given name."""
    return f"Hello, {name}! Welcome to Git."

#This block runs only when the file is executed directly,
# not when it is imported as a module from another file.
if __name__ == "__main__":
    print(greet("World")) # Call the greet function and print the result.