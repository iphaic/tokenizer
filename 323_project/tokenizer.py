import keyword
import re

# open and read input file
with open('input.py', 'r') as file:
    lines = file.readlines()

# remove spaces and comments
cleaned_lines = []
for line in lines:
    stripped_line = line.strip()
    if stripped_line.startswith('#') or stripped_line == '':
        continue
    else:
        cleaned_lines.append(line.rstrip())

# output 1
print('Output 1:')
for line in cleaned_lines:
    print(line)

print()

# turn the code into a single string
code_string = '\n'.join(cleaned_lines)

# define the different types of tokens
categories = {
    'Keywords': [],
    'Identifiers': [],
    'Operators': [],
    'Separators': [],
    'Literals': []
}

# patterns for tokens in input.py
token_specification = [
    ('LITERAL',        R'\b\d+\b'),
    ('STRING_LITERAL', R'\".*?\"|\'.*?\''),
    ('IDENTIFIER',     R'\b[a-zA-Z_]\w*\b'),
    ('OPERATOR',       R'==|[=+]'),
    ('SEPARATOR',      R'[(),:]')
]

# organize into a single regex i.e. "LITERAL, 5"
token_regex = '|'.join('(?P<%s>%s)' % (name, pattern) for name, pattern in token_specification)

total = 0

# search for matches in a loop
for match in re.finditer(token_regex, code_string):
    token_type = match.lastgroup
    value = match.group()
    if token_type == 'IDENTIFIER':
        if value in keyword.kwlist:
            categories['Keywords'].append(value)
        else:
            categories['Identifiers'].append(value)
    elif token_type == 'LITERAL':
        categories['Literals'].append(value)
    elif token_type == 'STRING_LITERAL':
        categories['Literals'].append(value)
    elif token_type == 'OPERATOR':
        categories['Operators'].append(value)
    elif token_type == 'SEPARATOR':
        categories['Separators'].append(value)
    total += 1

# output 2
print('Output 2:')
print(f'{"Category":<12} Tokens')
for category, tokens_list in categories.items():
    tokens_string = ' '.join(f"'{token}'" for token in tokens_list)
    print(f'{category:<12} {tokens_string}')
print(f'\nTotal: {total}')
