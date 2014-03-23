"""<tt095.py

Sizing windows can be a frustrating experience when working with Tkinter.  
Imagine this situation. You believe in iterative development, so first you 
carefully lay out a frame with the height and width specification that you want.  
You test it and you see that it works. Then you move on to the next step, and 
add some buttons to the frame.  You test it again, but now to your surprise 
Tkinter is acting as if there were no "height" and "width" specifications for 
the frame, and the frame has snapped down to tightly encase the buttons.

What's going on ???!!!

Well, the packer's behavior is inconsistent.  Or, shall we say: the packer's 
behavior depends on a lot of situational factors.  The bottom line is that the 
packer will honor the size request of a container if the container is empty, but 
if the container contains any other widgets, then the elastic nature of the 
container comes to the fore -- the "height" and "width" settings for the 
container are ignored, and the size of the container is adjusted to enclose the 
widgets as closely as possible.

The bottom line is that you really cannot control the size of a container that 
contains widgets.

What you CAN control is the the initial size of the entire root window, and you 
do this with the Window Manager "geometry" option.

(1)

In this program, we use the geometry option to make a nice big window around
our smaller frame.

(2) 
Note that the "title" option, which we also use in this program, is also a 
Window Manager method. "Title" controls the text of the title in the window's 
title bar.

Not also that Window Manager options can optionally be specified with a "wm_" 
prefix, e.g. "wm_geometry" and "wm_title".  In this program, just to show that
it can be done either way, we use "geometry" and "wm_title".


PROGRAM BEHAVIOR

This program puts up four windows in succession. 

Note that you will have to close each window by clicking on the "close"
widget -- the "X" in a box at the right of the title bar.

In case 1, we see what a frame looks like when height and width are specified, 
and -- NOTE -- it contains no widgets.

In case 2, we see what the exact same frame looks like when some widgets (in our 
case, three buttons) are added to it.  Note that the frame has snapped down 
tight around the three buttons.

In case 3, we again show what the empty frame looks like, only this time we use 
the geometry option to control the size of the window as a whole.  We can see 
the blue background of the frame inside the larger gray field of the window.

In case 4, we again show the frame with three buttons in it, but this time 
specifying the frame size with the geometry option.  Note that the size of the 
window is the same as it was in Case 3, but (as in Case 2) the frame has snapped 
down around the buttons, and we cannot see any of the frame's blue background at 
all.

[revised: 2002-10-01]
>"""
from Tkinter import *

class App:
	def __init__(self, root, use_geometry, show_buttons):
		fm = Frame(root, width=300, height=200, bg="blue")
		fm.pack(side=TOP, expand=NO, fill=NONE)
		
		if use_geometry:
			root.geometry("600x400")  ### (1) Note geometry Window Manager method

		if show_buttons:			
			Button(fm, text="Button 1", width=10).pack(side=LEFT)
			Button(fm, text="Button 2", width=10).pack(side=LEFT)
			Button(fm, text="Button 3", width=10).pack(side=LEFT)
		

case = 0
for use_geometry in (0, 1):
	for show_buttons in (0,1):
		case = case + 1		
		root = Tk()
		root.wm_title("Case " + str(case))  ### (2) Note wm_title Window Manager method
		display = App(root, use_geometry, show_buttons)
		root.mainloop()
				