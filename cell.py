from tkinter import Button, Label
import random
import settings
import ctypes
import sys
from time import sleep


class Cells:
    all = []  # to store all cell
    cell_count_label = None  # A display label to show remaining cells
    cell_count = settings.CELL_COUNT  # total cell counts

    def __init__(self, x, y, is_mine=False):
        self.x = x
        self.y = y
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.is_open = False
        self.is_mine_candidate = False
        Cells.all.append(self)

    def create_btn_object(self, location):
        """Creating Button"""
        btn = Button(location, width=12,
                     height=4)
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
        """Creating cell count label and showing number of remaining cells to win"""
        label = Label(location, text=f"Cells Left:{Cells.cell_count}", width=12, height=4,
                      bg='Black', fg='yellow',
                      font=("", 30))
        Cells.cell_count_label = label

    def left_click_actions(self, event):
        """Defining actions to happen with left click"""
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:  # Opening all if surrounded mines are 0
                for cell_obs in self.surrounded_cells:
                    cell_obs.show_cell()
            self.show_cell()
            if settings.MINES_COUNTER == Cells.cell_count:  # If cell remaining are equal to mine
                ctypes.windll.user32.MessageBoxW(0, "you won the game", "Congratulations !!", 0)
                sleep(5)
                sys.exit()
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')

    def show_mine(self):
        """ If cell is mine game over !"""
        self.cell_btn_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0, "you clicked on mine", "Game Over", 0)
        # sleep(3)
        self.cell_btn_object.configure(bg='red')
        sleep(2)
        sys.exit()

    def get_cell_by_axis(self, x, y):
        """get the cell by raw & col position"""
        for cell in Cells.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):
        """finding all surrounding cells """
        xs = [-1, -1, -1, 0, 0, 1, 1, 1]
        ys = [-1, 0, 1, -1, 1, -1, 0, 1]

        cells = [self.get_cell_by_axis(self.x + xs[i], self.y + ys[i]) for i in range(len(xs))]
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mines_length(self):
        """counting total number of mines around a cell"""
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def show_cell(self):
        """refreshing cell counts and also opening the clicked cells"""
        if not self.is_open:
            Cells.cell_count -= 1
            self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
            if Cells.cell_count_label:
                Cells.cell_count_label.configure(text=f"{Cells.cell_count}")
            if self.is_mine_candidate:
                self.cell_btn_object.configure(bg="SystemButtonFace")
            self.is_open = True

    def right_click_actions(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(bg="orange")
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(bg="SystemButtonFace")
            self.is_mine_candidate = False

    def __repr__(self):
        return f"Cells({self.x}, {self.y})"

    @staticmethod
    def randomize_mines():
        """ from all cells, create random mines"""
        picked_cells = random.sample(Cells.all, settings.MINES_COUNTER)
        for cell in picked_cells:
            cell.is_mine = True
