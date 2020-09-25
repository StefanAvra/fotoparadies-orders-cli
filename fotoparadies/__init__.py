import curses
from curses import panel
from . import api


class Menu(object):
    def __init__(self, items, stdscr):
        self.window = stdscr.subwin(0,0)
        self.window.keypad(1)
        self.panel = panel.new_panel(self.window)
        panel.update_panels()

        self.items = items
        self.current_entry = 0

    def navigate(self, direction):
        self.current_entry += direction
        if self.current_entry < 0:
            self.current_entry = len(self.items) - 1
        elif self.current_entry >= len(self.items):
            self.current_entry = 0

    def display(self):
        self.panel.top()
        self.window.clear()

        while True:
            self.window.refresh()
            curses.doupdate()
            for index, item in enumerate(self.items):
                if index == self.current_entry:
                    mode = curses.A_REVERSE
                else:
                    mode = curses.A_NORMAL

                msg = f'{index}  {item[0]}'
                self.window.addstr(1 + index, 1, msg, mode)

            key = self.window.getch()

            if key in [curses.KEY_ENTER, ord("\n")]:
                if self.current_entry == len(self.items) - 1:
                    break
                else:
                    self.items[self.current_entry][1]()

            elif key == curses.KEY_UP:
                self.navigate(-1)
            elif key == curses.KEY_DOWN:
                self.navigate(1)
            elif key == ord('q'):
                break 
    
    
def open_orders():
    pass

def new_order():
    pass

def main(stdscr):
    stdscr.clear()
    curses.curs_set(0)

    menus = {
    'home': [
        ('orders', open_orders),
        ('check/add order', new_order),
        ('exit',0)
        ],
    }

    stdscr.addstr(2, 2, 'Welcome!')

    home_menu = Menu(menus['home'], stdscr)
    home_menu.display() 

    stdscr.refresh()
    # stdscr.getkey()


curses.wrapper(main)

