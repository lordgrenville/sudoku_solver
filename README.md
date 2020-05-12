Peter Norvig has [already done](http://norvig.com/sudoku.html) the canonical Python sudoku solution, but I thought as an AI giuy it would be fun to try to code it the way _I_ think...

Start with dict(zip(range(1, 81), zeros)) each cell starts as blank. Fill in known values from puzzle - parse string

Each cell has 3 peer groups: row is 
row_num = cell / 9 ; row_num: row_num + 9
col is
col_num = cell % 9 ; col_num: col_num + 9
box is
if cell < 27, cell % 9 % 3
if cell > 54, that + 2. otherwise that + 1
give each cell its box peers

then:
sort all 27 groups by number of unknown. start with one with fewest unknown. for each cell in it: constraints are complement of the set union of the three peer sets, with (1..9) 
if this is greater than one, not conclusive move on. if it is conclusive, update hash table, sort again and restart, recalculating constraints

This is pretty much how I think?

Add pretty print function?

Extra: if stuck on a puzzle:
For n in range (9):
Each box must have an n
Fill grid with zeros
Divide into 9 boxes
If there's an n in the box, fill with 1s
And if there's an n in a row, fill row with 1s
And ditto for column
If there's a box with only one zero, flip it to n in the grid
