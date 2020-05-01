#!/usr/bin/env python3

import curses
from random import randrange,choice

def main(stdscr):
    cells=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    def cast(str):
        stdscr.addstr(str+'\n')

    def draw_hor():
        cast('+------'*4+'+')

    def get_cell(cell):
        if cell>0:
            return '|{: ^6}'.format(cell)
        else:
            return '|      '

    def draw_row(row):
        cast(''.join([get_cell(cell) for cell in row])+'|')

    def draw_game():
        global cells
        stdscr.clear()
        for row in cells:
            draw_hor()
            draw_row(row)
        draw_hor()

    def init_game():
        global cells
        cells=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    def spawn():
        global cells
        new_cell=4 if randrange(100)>89 else 2
        (i,j)=choice([(i,j) for i in range(4)  for j in range(4) if cells[i][j]==0])
        cells[i][j]=new_cell

    def move_is_possible(direction):
        def move_left_is_possible(row):
            def change(i):
                if row[i]==0 and row[i+1]!=0:
                    return True
                if row[i]!=0 and row[i+1]==row[i]:
                    return True
            return any(change(i) for i in range(len(row)-1))

        global cells
        return any(move_left_is_possible(row) for row in cells)

    def move():




    curses.use_default_colors()

    stdscr.getch()
curses.wrapper(main)

