WIDTH = 1440
HEIGHT = 720
cust_input = int(input("Enter the value of X for game of X * X cells less than 7 "))
if cust_input > 7:
    GRID_SIZE = 7
else:
    GRID_SIZE = cust_input
CELL_COUNT = GRID_SIZE**2
MINES_COUNTER = int((GRID_SIZE**2)*0.25)