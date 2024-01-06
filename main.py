from cell import Cells
from tkinter import *
import settings
import utils

root = Tk()

# override window setting
root.configure(bg="black")

root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Minesweeper Game')
root.resizable(False, False)

top_frame = Frame(root, bg="blue", width=settings.WIDTH, height=utils.height_prct(25))
top_frame.place(x=0, y=0)

game_title = Label(top_frame, bg="red", fg="black", text="Minesweeper Game", font=('', 48))
game_title.place(x=utils.width_prct(25), y=0)

left_frame = Frame(root, bg="black", width=utils.width_prct(25), height=utils.height_prct(75))
left_frame.place(x=0, y=utils.height_prct(25))

centre_fram = Frame(root, bg='green', width=utils.width_prct(75), height=utils.height_prct(75))
centre_fram.place(x=utils.width_prct(25), y=utils.height_prct(25))

# creating all cells based on their positions
for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cells(x, y)
        c.create_btn_object(centre_fram)
        c.cell_btn_object.grid(column=x, row=y)
Cells.create_cell_count_label(left_frame)
Cells.cell_count_label.place(x=0, y=0)

Cells.randomize_mines()

# run the window
root.mainloop()

# end
