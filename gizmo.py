# hello function - f formatting
import shutil


def hello2(name, country = "Finland"):
    return f"Hello, {name}, how are things in {country}?"

# hello function
def hello(name, country = 'Finland'):
    print("Hello", name + ", how are things in", country + "?")

# spelling function - f formatting
def spell2(word):
    s_word = ""
    for letter in word:
        s_word += letter + '.'
    return f"{s_word[:-1]}"

# spelling function 
def spell(word):
    s_word = ""
    for letter in word:
        s_word += letter + '.'
    print(s_word[:-1])
    
# editing strings
def relative_path(arr):
    new_names = []
    for file in arr:
        if file is not None:
            new_file = './subjects/mock_recording_'+file+'.rec'
            new_names.append(new_file)
    return(new_names)

# creating a class     
class Gizmo:
    def __init__(self,name = "default"):
        self.name = name
        
    def speak(self):
        print(self.name)
    
# generator for fibonacci
def generate_fibonacci_sequence(n):
    """
    generate_fibonacci_sequence(n)

    Generate a Fibonacci sequence to the nth element.

    Parameters
    ----------
    n : int
        The length of the Fibonacci sequence to generate.

    Yields
    ------
    int
        The next number in the Fibonacci sequence.

    Extended Summary
    ----------------
    The `generate_fibonacci_sequence` function takes an integer `n` as input and
    generates the Fibonacci sequence of length `n`. It starts with 0 and 1 as the
    first two numbers and then generates subsequent Fibonacci numbers by adding the
    last two numbers in the sequence.

    Example
    -------
    >>> list(generate_fibonacci_sequence(10))
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    yield 0  # Yield 0 as the first value
    a, b = 0, 1
    try:
        for _ in range(n - 1):  # We already yielded the first value (0), so n - 1 iterations needed
            assert b != 0, "Divisor cannot be zero in Fibonacci sequence."
            a, b = b, a + b
            yield a
    except AssertionError as e:
        print(f"An AssertionError occurred: {e}")