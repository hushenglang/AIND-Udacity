columns = "123456789"
rows = "ABCDEFGHI"

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a+b for a in A for b in B]

# build boxes
boxes = cross(rows, columns)
# build units including row_units, column_units, square_units, diagonal_units
row_units = [cross(r,columns) for r in rows]
column_units = [cross(rows,c) for c in columns]
square_units = [cross(r,c) for r in ("ABC","DEF","GHI") for c in ("123","456","789")]
diagonal_units = [[r+c for r, c in zip(rows, columns)],[r+c for r, c in zip(rows[::-1], columns)]]
units_list = row_units + column_units + square_units + diagonal_units
units = {box:[units for units in units_list if box in units] for box in boxes}
peers = {box: (set(sum(unit,[]))-set([box])) for box, unit in units.items()}


print(diagonal_units)