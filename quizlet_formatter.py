import os 
import csv
'''
This file parses a csv file and creates a text file for each letter of the alphabet.
input file: 
    - a csv file with two columns: word and definition
    - the first row should be the column names
    - the first column should be the word
    - the second column should be the definition
Note that the word list doesn't have to be sorted alphabetically. The script will sort it for you.
output file:
    - a text file for each letter of the alphabet
    - the file name is output_letter_{letter}.txt
    - the file content is a list of words and definitions separated by a semicolon
    - the words and definitions are separated by a pipe
    - the words and definitions are sorted alphabetically
'''
# Get the current directory and the file name
curdir = os.path.dirname(os.path.realpath(__file__))
filename = input("Enter the name of the file:")

filepath = os.path.join(curdir, filename)

content = {}
with open(filepath, 'r') as f:
    read_obj = csv.reader(f)
    while read_obj:
        try:
            line = next(read_obj)
            letterHead = line[0][0]
            if letterHead not in content:
                content[letterHead] = [[line[0], line[1]]]
            else: 
                content[letterHead].append([line[0], line[1]])
        except StopIteration:
            break 
'''
content['a'] = [['abandon', '1.freedom from constraint\n2.withdraw']] + content['a']
del(content['ï'])
'''

output_dir = os.path.join(curdir, 'output')
os.makedirs(output_dir, exist_ok=True)
for letter in content.items(): 
    filename = f'output_letter_{letter[0].upper()}.txt'
    filepath = os.path.join(output_dir, filename)
    with open(filepath, 'w') as f:
        for i in letter[1]: 
            f.write(f'{i[0]};{i[1]}|')
    print(f'File saved to {filepath}')