# hello function - f formatting
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
    a, b = 0,1
    for _ in range(n):
        a, b = b, a + b
        yield (a)


