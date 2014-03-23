"""<tt100.py

In this program, we look at several pack() options for controlling layouts 
within a frame:

  * side 
  * fill 
  * expand 
  * anchor

This program is unlike the other programs in this series.  That is, you don't 
need to read the source code in order to understand how to code some feature. 
You need to RUN the program.

The purpose of the program is to show you the results of pack options. Running 
the program will allow you to set different pack options and to observe the 
effects of different combinations of options.

THE CONCEPTS UNDERLYING THE PACK OPTIONS

To understand how we can control the appearance of widgets within a container 
(that is, with a frame), we need to remember that the pack geometry manager uses 
a "cavity" model of arrangement.  That is, each container contains a cavity, and 
we pack slaves within the container.

In talking about the positioning and display of components with a container, it 
will be useful to have three concepts:

 * unclaimed space (that is, the cavity)
 * claimed but unused space 
 * claimed and used  space

When you pack a widget, such as a button, it is always packed along one of the 
four sides of the cavity.  The pack "side" option specifies which side to use.  
For example, if we specify "side=LEFT", the the widget will be packed (that is, 
positioned) on the left side of the cavity.

When a widget is packed along a side, it claims the entire side, although it may
not actually use all of the space it has claimed.  Suppose we pack a small button
called X along the left side of a large cavity, as in the following diagram.


                  -------------------
    claimed but   |   |             |
    unused -----> |   |   cavity    |
                  |   | (unclaimed) |
                  |___|             |
    claimed and   |   |             |
    used -------> | X |             |
                  |___|             |
                  |   |             |
    claimed but   |   |             |
    unused -----> |   |             |
                  |   |             |
                  -------------------

The cavity (the unclaimed area) is now to the right of the widget.  Widget X has 
claimed the entire left side, in a strip that is wide enough to hold it. But 
because widget X is small, it actually uses only a small part of the area that 
it has claimed.  That is the part that it uses to display itself.

As you can see, widget X has claimed only enough space as it needs to display 
itself. If we specify a pack option of "expand=YES", it will claim ALL of the 
available area.  No part of the cavity would be left unclaimed.  Note that 
this does not mean that widget X would *use* the whole area.  It would still 
only use the small part that it needs.  

If a widget has claimed more space than it is using, it has two choices:
 * it can move around in the unclaimed space, or
 * it can grow to fill the unclaimed space. 

If we want it to grow to use the the unclaimed space, we can use the "fill" 
option, which tells a widget whether or not it can grow to fill the unused 
space, and in which direction it can grow.  

  * "fill=NONE" means that it cannot grow. 
  * "fill=X"    means that it can grow along the X-axis (i.e. horizontally). 
  * "fill=Y"    means that it can grow along the Y-axis (i.e. vertically). 
  * "fill=BOTH" means that it can grow both horizontally and vertically.

If we want it to grow to move around in the the unclaimed space, then we can use 
the "anchor" option, which tells a widget where to position itself in the space 
it has claimed.  The values of the anchor option are like compass headings. "N" 
means "north" (i.e. centered at the top of the claimed area).  "NE" means 
"northeast" (i.e. in the upper, right corner of the claimed area), "CENTER"
means centered right in the middle of the claimed area.  And so on.


RUNNING THE PROGRAM

So now, run the program.  You don't need to read the code.  Just run the program 
and experiment with the various pack options of the three demo buttons.

Button A's frame gives it a horizontal cavity to run around in -- the frame is 
no taller than the button.  

Button B's cavity gives it a vertical cavity to run around in -- the frame is no 
wider than the button.  

And button C's frame gives it a big cavity -- much wider and taller than the 
button itself -- to play in. 

If the appearance of any of the buttons under certain settings surprises 
you, try to figure out why the button looks the way it does.

And finally....

A USEFUL DEBUGGING TIP

Note that packing is a complicated business, because the positioning of a widget 
with respect to other widgets that were packed earlier depends in part on how 
the other widgets were packed.  That is, if the other widgets were packed to the 
left, then the cavity within which the next widget can be packed will be to 
their right.  But if they were packed to the top of the cavity, then the cavity 
within which the next widget can be packed will be below them. It can all get 
very confusing.

Here is a useful debugging tip.  If you are developing your layout and hit a 
problem -- things aren't acting the way you think they should -- then give each 
of your containers (that is, each of your frames) a different background color, 
for example: 

      bg="red"
or 
      bg="cyan"
or  
      bg="tan"
      
... or yellow, or blue, or red, and so on.

This will allow you to see how the frames are actually arranging themselves.  Often,
what you see will give you a clue as to what the problem is.

[revised: 2004-04-26]
>"""
from Tkinter import *

class MyApp:
	def __init__(self, parent):
		
		#------ constants for controlling layout of buttons ------
		button_width = 6       		
		button_padx = "2m"     
		button_pady = "1m"     
		buttons_frame_padx =  "3m"    
		buttons_frame_pady =  "2m"    		
		buttons_frame_ipadx = "3m"    
		buttons_frame_ipady = "1m"   
		# -------------- end constants ----------------


		# set up Tkinter variables, to be controlled by the radio buttons
		self.button_name   = StringVar()
		self.button_name.set("C")
		
		self.side_option = StringVar()
		self.side_option.set(LEFT)
		
		self.fill_option   = StringVar()
		self.fill_option.set(NONE)

		self.expand_option = StringVar()
		self.expand_option.set(YES)
		
		self.anchor_option = StringVar()		
		self.anchor_option.set(CENTER)
		
		
		# -------------- end constants ----------------
		
		self.myParent = parent 
		self.myParent.geometry("640x400")

		### Our topmost frame is called myContainer1
		self.myContainer1 = Frame(parent) ###
		self.myContainer1.pack(expand=YES, fill=BOTH)


		### We will use HORIZONTAL (left/right) orientation inside myContainer1.
		### Inside myContainer1, we create control_frame and demo_frame.
		
		# control frame - basically everything except the demo frame
		self.control_frame = Frame(self.myContainer1) ###
		self.control_frame.pack(side=LEFT, expand=NO,  padx=10, pady=5, ipadx=5, ipady=5)  	
		
		# inside control_frame we create a header label 
		# and a buttons_frame at the top,
		# and demo_frame at the bottom
		
		myMessage="This window shows the effects of the \nexpand, fill, and anchor packing options.\n"
		Label(self.control_frame, text=myMessage, justify=LEFT).pack(side=TOP, anchor=W)
		
		# buttons frame
		self.buttons_frame = Frame(self.control_frame) ###
		self.buttons_frame.pack(side=TOP, expand=NO, fill=Y, ipadx=5, ipady=5)    

		# demo frame
		self.demo_frame = Frame(self.myContainer1) ###
		self.demo_frame.pack(side=RIGHT, expand=YES, fill=BOTH)  			


		### Inside the demo frame, we create top_frame and bottom_frame.
		### These will be our demonstration frames.  						
		# top frame
		self.top_frame = Frame(self.demo_frame) 
		self.top_frame.pack(side=TOP, expand=YES, fill=BOTH)  ###    

		# bottom frame
		self.bottom_frame = Frame(self.demo_frame,
			borderwidth=5, 	relief=RIDGE,
			height=50, 
			bg="cyan",
			) ###	
		self.bottom_frame.pack(side=TOP, fill=X)    


		### Now we will put two more frames, left_frame and right_frame,
		### inside top_frame.  We will use HORIZONTAL (left/right)
		### orientation within top_frame.
		
		# left_frame		
		self.left_frame = Frame(self.top_frame,	background="red",
			borderwidth=5, 	relief=RIDGE,
			width=50, 
			) ###		
		self.left_frame.pack(side=LEFT, expand=NO, fill=Y)    


		### right_frame 
		self.right_frame = Frame(self.top_frame, background="tan",
			borderwidth=5, 	relief=RIDGE,
			width=250
			)
		self.right_frame.pack(side=RIGHT, expand=YES, fill=BOTH) 	


		# now put a button in each of the interesting frames
		button_names = ["A", "B", "C"]	
		side_options = [LEFT, TOP, RIGHT, BOTTOM]	
		fill_options = [X, Y, BOTH, NONE]
		expand_options = [YES, NO]
		anchor_options = [NW, N, NE, E, SE, S, SW, W, CENTER]
		
	
		self.buttonA = Button(self.bottom_frame, text="A")
		self.buttonA.pack()
		self.buttonB = Button(self.left_frame, text="B")
		self.buttonB.pack()
		self.buttonC = Button(self.right_frame, text="C")
		self.buttonC.pack()	
		self.button_with_name = {"A":self.buttonA, "B":self.buttonB, "C":self.buttonC}	

		# now we some subframes to the buttons_frame
		self.button_names_frame   = Frame(self.buttons_frame, borderwidth=5)
		self.side_options_frame   = Frame(self.buttons_frame, borderwidth=5)
		self.fill_options_frame   = Frame(self.buttons_frame, borderwidth=5)
		self.expand_options_frame = Frame(self.buttons_frame, borderwidth=5)
		self.anchor_options_frame = Frame(self.buttons_frame, borderwidth=5)

		self.button_names_frame.pack(  side=LEFT, expand=YES, fill=Y, anchor=N)
		self.side_options_frame.pack(  side=LEFT, expand=YES, anchor=N)		
		self.fill_options_frame.pack(  side=LEFT, expand=YES, anchor=N)
		self.expand_options_frame.pack(side=LEFT, expand=YES, anchor=N)
		self.anchor_options_frame.pack(side=LEFT, expand=YES, anchor=N)
					
		Label(self.button_names_frame, text="\nButton").pack()
		Label(self.side_options_frame, text="Side\nOption").pack()
		Label(self.fill_options_frame, text="Fill\nOption").pack()
		Label(self.expand_options_frame, text="Expand\nOption").pack()
		Label(self.anchor_options_frame, text="Anchor\nOption").pack()		
		
		for option in button_names:
			button = Radiobutton(self.button_names_frame, text=str(option), indicatoron=1, 
				value=option, command=self.button_refresh, variable=self.button_name)
			button["width"] = button_width
			button.pack(side=TOP)

		for option in side_options:
			button = Radiobutton(self.side_options_frame, text=str(option), indicatoron=0, 
				value=option, command=self.demo_update, variable=self.side_option)
			button["width"] = button_width
			button.pack(side=TOP)
								
		for option in fill_options:
			button = Radiobutton(self.fill_options_frame, text=str(option), indicatoron=0, 
				value=option, command=self.demo_update, variable=self.fill_option)
			button["width"] = button_width
			button.pack(side=TOP)

		for option in expand_options:
			button = Radiobutton(self.expand_options_frame, text=str(option), indicatoron=0, 
				value=option, command=self.demo_update, variable=self.expand_option)
			button["width"] = button_width 
			button.pack(side=TOP)
	
		for option in anchor_options:
			button = Radiobutton(self.anchor_options_frame, text=str(option), indicatoron=0, 
				value=option, command=self.demo_update, variable=self.anchor_option)
			button["width"] = button_width
			button.pack(side=TOP)

		self.cancelButtonFrame = Frame(self.button_names_frame)
		self.cancelButtonFrame.pack(side=BOTTOM, expand=YES, anchor=SW)
		
		self.cancelButton = Button(self.cancelButtonFrame,
			text="Cancel", background="red", 
			width=button_width,   
			padx=button_padx,     
			pady=button_pady      
			)				
		self.cancelButton.pack(side=BOTTOM, anchor=S)
		

		
		self.cancelButton.bind("<Button-1>", self.cancelButtonClick)   
		self.cancelButton.bind("<Return>", self.cancelButtonClick) 
		
		# set up the buttons in their initial position
		self.demo_update()


	def button_refresh(self):
		button = self.button_with_name[self.button_name.get()]
		properties = button.pack_info()
		self.fill_option.set  (  properties["fill"] )
		self.side_option.set  (  properties["side"] )
		self.expand_option.set(  properties["expand"] )
		self.anchor_option.set(  properties["anchor"] )


	def demo_update(self):
		button = self.button_with_name[self.button_name.get()]
		button.pack(fill=self.fill_option.get()
			, side=self.side_option.get()
			, expand=self.expand_option.get()
			, anchor=self.anchor_option.get()
			)
		
		
	def cancelButtonClick(self, event): 
		self.myParent.destroy()      


root = Tk()
myapp = MyApp(root)
root.mainloop()