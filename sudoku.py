import re


def pretty_print(s):
    for i in range(9):
        print('---' * 12)
        print('| ' + ''.join([n + ' | ' for n in s[9 * i: 9 * i + 9]]).replace('0', ' '))
    print('---' * 12)
    print(f'\n{round(sum([c == "0" for c in interim_solution(sol)]) / 81, 2)}% to go!!')


def interim_solution(d):
    s = ''
    for k, v in d.items():
        if isinstance(v, set):
            s += '0'
        else:
            s += str(v)
    return s


with open('p096_sudoku.txt') as f:
    sudokus = [''.join(x.split('\n')) for x in re.compile('Grid \d\d\\n').split(f.read())[1:]]

puz = sudokus[0]
# pretty_print(puz)

rows = [list(range(i * 9 + 1, i * 9 + 10)) for i in range(9)]
cols = [list(range(i, 9 * 9 + i, 9)) for i in range(1, 10)]
blocks = [[n % 3 * 3 + n // 3 % 3 * 27 + 1 + (9 * j) + k for j in range(3) for k in range(3)] for n in range(9)]

sol = {x[0]: int(x[1]) for x in zip(range(1, 82), puz)}

# get constraints
constraints = lambda iterable: [set(range(10)).difference(sol[sq] for sq in unit) for unit in iterable]
row_constraints, col_constraints, block_constraints = constraints(rows), constraints(cols), constraints(blocks)

# filter by constraints
for col, constr in zip(cols, col_constraints):
    for square in col:
        if sol[square] == 0:
            sol[square] = constr

for row, constr in zip(rows, row_constraints):
    for square in row:
        if isinstance(sol[square], set):
            sol[square] = sol[square] & constr

for block, constr in zip(blocks, block_constraints):
    for square in block:
        if isinstance(sol[square], set):
            sol[square] = sol[square] & constr

# update dict
for k, v in sol.items():
    if isinstance(v, set):
        if len(v) == 1:
            sol[k] = list(v)[0]

print('solution so far...')
pretty_print(interim_solution(sol))

