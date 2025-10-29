# Program to make a simple 
# login screen  


import tkinter as tk
#import main 
root=tk.Tk()

# setting the windows size
root.geometry("600x400")
 
# declaring string variable
# for storing gate1 and gate2ord
gate1_var=tk.StringVar()
gate2_var=tk.StringVar()

 
# defining a function that will
# get the gate1 and gate2ord and 
# print them on the screen
def submit():

    gate1=gate1_var.get()
    gate2=gate2_var.get()
    
    print("The gate1 is : " + gate1)
    print("The gate2ord is : " + gate2)
    
    gate1_var.set("")
    gate2_var.set("")
    
    
# creating a label for 
# gate1 using widget Label
gate1_label = tk.Label(root, text = 'gate1', font=('calibre',10, 'bold'))
 
# creating a entry for input
# gate1 using widget Entry
gate1_entry = tk.Entry(root,textvariable = gate1_var, font=('calibre',10,'normal'))
 
# creating a label for gate2ord
gate2_label = tk.Label(root, text = 'gate2', font = ('calibre',10,'bold'))
 
# creating a entry for gate2ord
gate2_entry=tk.Entry(root, textvariable = gate2_var, font = ('calibre',10,'normal'), show = '*')
 
# creating a button using the widget 
# Button that will call the submit function 
sub_btn=tk.Button(root,text = 'Submit', command = submit)
 
# placing the label and entry in
# the required position using grid
# method
gate1_label.grid(row=0,column=0)
gate1_entry.grid(row=0,column=1)
gate2_label.grid(row=1,column=0)
gate2_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)
 
# performing an infinite loop 
# for the window to display
root.mainloop()
