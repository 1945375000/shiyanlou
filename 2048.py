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

    def transpose(field):
        return [list(row) for row in zip(*field)]

    def invert(field):
        return [row[::-1] for row in field]

    def move_is_possible(direction):
        def row_left_is_possible(row):
            def change(i):
                if row[i]==0 and row[i+1]!=0:
                    return True
                if row[i]!=0 and row[i+1]==row[i]:
                    return True
            return any(change(i) for i in range(len(row)-1))

        global cells
        if direction=='a':
            return any(row_left_is_possible(row) for row in cells)
        if direction=='d':
            return any(row_left_is_possible(row) for row in invert(cells))
        if direction=='w':
            return any(row_left_is_possible(row) for row in transpose(cells))
        if direction=='s':
            return any(row_left_is_possible(row) for row in invert(transpose(cells)))

    def move(direction):
        def move_row_left(row):
            def tighten(row):
                new_row=[i for i in row if i>0]
                new_row+=[0 for i in range(len(row)-len(new_row))]
                return new_row
            def merge(row):
                pair=False
                new_row=[]
                for i in range(len(row)):
                    if pair:
                        new_row.append(0)
                        pair=False
                    else:
                        if i+1<len(row) and row[i]==row[i+1]:
                            pair=True
                            new_row.append(row[i]*2)
                        else:
                            new_row.append(row[i])
                return new_row
            return tighten(merge(tighten(row)))

        if move_is_possible(direction):
            global cells
            if direction=='a':
                cells=[move_row_left(row) for row in cells]
            elif direction=='d':
                cells=invert([move_row_left(row) for row in invert(cells)])
            elif direction=='w':
                cells=transpose([move_row_left(row) for row in transpose(cells)])
            elif direction=='s':
                cells=transpose(invert([move_row_left(row) for row in invert(transpose(cells))]))

            spawn()
            draw_game()
            return True
        else:
            return False

    curses.use_default_colors()

    char=''
    while char!='q':
        char=chr(stdscr.getch())
        if char in ['w','a','s','d']:
            move(char)
        if char=='r':
            init_game()
            spawn()
            spawn()
            draw_game()

curses.wrapper(main)

