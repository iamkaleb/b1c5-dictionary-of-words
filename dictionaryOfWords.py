"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()
"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""
word_definitions['Frog'] = 'A slimy animal.'
word_definitions['Dog'] = 'A hairy animal.'
word_definitions['Bird'] = 'A feathery animal.'
"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
print(word_definitions['Frog'])
print(word_definitions['Dog'])
"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""
for key, value in word_definitions.items():
    print(f'The definition of {key} is {value}')