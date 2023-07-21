# hello function
def hello(name, country = "Finland"):
    return f"Hello, {name}, how are things in {country}?"

# spelling function
def spell(word):
    s_word = ""
    for letter in word:
        s_word += letter + '.'
    return f'{s_word[:-1]}'

# editing strings
def relative_path(arr):
    for file in arr:
        if file is not None:
            new_file = f'./subjects/mock_recording_{file}.rec'
            print(new_file)

# creating a class     
class Gizmo:
    def __init__(self,name = "default"):
        self.name = name
        
    def speak(self):
        print(self.name)
    
# function for fibonacci
def generate_fibonacci_sequence(n):
    seq = []
    a, b = 0,1
    while len(seq) < n:
        seq.append(a)
        a, b = b, a + b
    return seq

