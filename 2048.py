#!/usr/bin/env python3

import curses

def main(stdscr):

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

    curses.use_default_colors()

    draw_hor()
    draw_row([2,3,0,7])
    draw_hor()
    draw_row([0,4,6,0])
    draw_hor()
    draw_row([343,556,676,0])
    draw_hor()
    draw_row([565,676,45,6])
    draw_hor()

    stdscr.getch()
curses.wrapper(main)

