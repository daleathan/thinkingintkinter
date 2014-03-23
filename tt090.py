"""<tt090.py

In this program, we look at nesting of containers (frames). What we are going to 
do is to create a series of frames, nested inside each other: bottom_frame, 
left_frame, and big_frame.

These frames will contain nothing -- no widgets.  Normally, because frames are 
elastic, the would shrink down to nothing.  But we specify "height" and "width" 
attributes to provide an initial size for them.

Note that we don't provide heights or widths for all of the frames. For 
myContainer1, for instance, we don't provide either.  But we do provide heights 
and widths for its descendants, and it will stretch to accommodate the 
cumulative heights and widths of its descendants.

In a later program we will explore putting widgets into these frames, but in 
this program we will simply create the frames, and give them different different 
sizes, positions, and background colors.

We also put a ridged border around the three frames that will be of most iterest 
to us in the future: bottom_frame, left_frame, and right_frame. The other frames 
(for instance top_frame and buttons_frame) are not given a border.

PROGRAM BEHAVIOR

When you run this program, you will see the different frames, with different
background colors. 

[revised: 2005-07-15]
>"""
from Tkinter import *

class MyApp:
	def __init__(self, parent):
		
		self.myParent = parent 

		### Our topmost frame is called myContainer1
		self.myContainer1 = Frame(parent) ###
		self.myContainer1.pack()

		#------ constants for controlling layout ------
		button_width = 6      ### (1)
		
		button_padx = "2m"    ### (2)
		button_pady = "1m"    ### (2)

		buttons_frame_padx =  "3m"   ### (3)
		buttons_frame_pady =  "2m"   ### (3)        
		buttons_frame_ipadx = "3m"   ### (3)
		buttons_frame_ipady = "1m"   ### (3)
		# -------------- end constants ----------------

		### We will use VERTICAL (top/bottom) orientation inside myContainer1.
		### Inside myContainer1, first we create buttons_frame.
		### Then we create top_frame and bottom_frame.
		### These will be our demonstration frames.         
		
		# buttons frame
		self.buttons_frame = Frame(self.myContainer1) ###
		self.buttons_frame.pack( 
			side=TOP,   ###
			ipadx=buttons_frame_ipadx,   
			ipady=buttons_frame_ipady,   
			padx=buttons_frame_padx,    
			pady=buttons_frame_pady,    
			)    
		
		# top frame
		self.top_frame = Frame(self.myContainer1) 
		self.top_frame.pack(side=TOP,
			fill=BOTH, 
			expand=YES,
			)  ###

		# bottom frame
		self.bottom_frame = Frame(self.myContainer1, 
			borderwidth=5,  relief=RIDGE,
			height=50, 
			background="white",
			) ###   
		self.bottom_frame.pack(side=TOP,
			fill=BOTH, 
			expand=YES,
			)  ###


		### Now we will put two more frames, left_frame and right_frame,
		### inside top_frame.  We will use HORIZONTAL (left/right)
		### orientation within top_frame.
		
		# left_frame        
		self.left_frame = Frame(self.top_frame, background="red",
			borderwidth=5,  relief=RIDGE,
			height=250, 
			width=50, 
			) ###
		self.left_frame.pack(side=LEFT,
			fill=BOTH, 
			expand=YES,
			)  ###


		### right_frame 
		self.right_frame = Frame(self.top_frame, background="tan",
			borderwidth=5,  relief=RIDGE,
			width=250,
			)
		self.right_frame.pack(side=RIGHT,
			fill=BOTH, 
			expand=YES,
			)  ###


		# now we add the buttons to the buttons_frame	
		self.button1 = Button(self.buttons_frame, command=self.button1Click)
		self.button1.configure(text="OK", background= "green")
		self.button1.focus_force()       
		self.button1.configure( 
			width=button_width,  ### (1)
			padx=button_padx,    ### (2) 
			pady=button_pady     ### (2)
			)

		self.button1.pack(side=LEFT)    
		self.button1.bind("<Return>", self.button1Click_a)  
		
		self.button2 = Button(self.buttons_frame, command=self.button2Click)
		self.button2.configure(text="Cancel", background="red")  
		self.button2.configure( 
			width=button_width,  ### (1)
			padx=button_padx,    ### (2) 
			pady=button_pady     ### (2)
			)
	
		self.button2.pack(side=RIGHT)
		self.button2.bind("<Return>", self.button2Click_a)   
		
	def button1Click(self):      
		if self.button1["background"] == "green":  
			self.button1["background"] = "yellow"
		else:
			self.button1["background"] = "green"
	
	def button2Click(self): 
		self.myParent.destroy()     
		
	def button1Click_a(self, event):  
		self.button1Click()
				
	def button2Click_a(self, event): 
		self.button2Click() 


root = Tk()
myapp = MyApp(root)
root.mainloop()