# File: MyPicture.py
# Name: Sergio Ley Languren

"""Draws a sunrise with a tree in the middle."""

from pgl import GWindow, GLabel, GRect, GOval, GCompound
from typing import Optional
from random import randint

GWINDOW_WIDTH = 700        
GWINDOW_HEIGHT = 400   
RANDINT_INITIAL = 0

def _gshape_init_constructor(obj,w,h,x,y):
    if x or y:
        if x and not y:
            gobject = obj(x, 0, w, h)
        elif y and not x:
            gobject = obj(0, y, w, h)
        else:
            gobject = obj(x, y, w, h)
    else:
        gobject = obj(w, h)
    return gobject


def create_oval(w: int, h: int, x: Optional[int] = None, y: Optional[int] = None, 
color: Optional[str] = None, filled: bool = False) -> GOval:
    """Creates a oval object with the given parameters
       :param w: width
       :param h: height
       :param x: optional parameter for x coordinates
       :param y: optional parameter for y coordinates
       :param color: optional parameter for setting oval color
       :param filled: whether the oval will be filled or not. Defaults to: False
    """
    oval = _gshape_init_constructor(GOval, w, h, x, y)
    if color:
        oval.set_color(color)
    if filled:
        oval.set_filled(True)
    return oval

def create_rectangle(w: int, h: int, x: Optional[int] = None, y: Optional[int] = None, 
                    color: Optional[str] = None, filled: bool = False) -> GRect:
    """Creates a rectangle object with the given parameters
        :param w: width
        :param h: height
        :param x: optional parameter for x coordinates
        :param y: optional parameter for y coordinates
        :param color: optional paramater for setting rectangle color
        :param filled: whether the rectangle will be filled or not. Defaults to: False
    """
    rect = _gshape_init_constructor(GRect, w, h, x, y)
    if color:
        rect.set_color(color)
    if filled:
        rect.set_filled(True)
    return rect

def draw_clouds() -> GCompound:
    """Draws clouds at random x coordinates at a y cordinate of 100"""
    compound = GCompound()

    count = 10
    while count != 0:
        x_cord = randint(RANDINT_INITIAL, GWINDOW_WIDTH)
        y_cord = randint(25, 90)

        oval1 = create_oval(20, 10, x_cord, y_cord, "ghostwhite", True)
        oval2 = create_oval(20, 10, x_cord+1, y_cord, "ghostwhite", True)
        oval3 = create_oval(20, 10, x_cord-1, y_cord, "ghostwhite", True)

        compound.add(oval1)
        compound.add(oval2)
        compound.add(oval3)

        count -= 1
    return compound

def draw_tree() -> GCompound:
    """Draws the centerpiece of the picture"""
    compound = GCompound()
    count = 4
    y = 240
    while count != 0:
        rect = create_rectangle(10, 10, 350, y, "brown", True)
        compound.add(rect)
        y -= 10
        count -= 1
    
    count = 4
    y = 210
    x = 350
    while count != 0:
        if y == 200:
            y -= 10
            rect = create_rectangle(10,10, x, y, "limegreen", True)
        else:
            if y == 190:
                if x == 340:
                    x += 20
                    rect = create_rectangle(10,10, x, 200, "limegreen", True)
                else:
                    x -= 10
                    rect = create_rectangle(10,10, x, 200, "limegreen", True)
            else:
                y -= 10
                rect = create_rectangle(10,10, x, y, "limegreen", True)
        compound.add(rect)
        count -= 1
    return compound

def my_picture():
    """Describe the overall process of creating the picture."""
    gw = GWindow(GWINDOW_WIDTH, GWINDOW_HEIGHT)

    title_lbl = GLabel("Sunrise", 350, 20)
    title_lbl.set_color("white")
    title_lbl.set_font("15pt 'Montserrat', 'sans-serif'")
    title_lbl.send_to_front()

    sky = create_rectangle(700, 250, color="lightcoral", filled=True)

    top_ground = create_rectangle(700, 50, y=250, color="forestgreen", filled=True)

    bottom_ground = create_rectangle(700, 100, y=300, color="chocolate", filled=True)

    tree_compound = draw_tree()

    cloud_compound = draw_clouds()

    # picture object additions
    gw.add(sky)
    gw.add(title_lbl)
    gw.add(top_ground)
    gw.add(bottom_ground)
    gw.add(tree_compound)
    gw.add(cloud_compound)

# Startup code

if __name__ == "__main__":
    my_picture()
