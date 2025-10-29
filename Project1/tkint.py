# Program to make a simple 
# login screen  

from tkinter import ttk
import tkinter as tk
from main import *
root=tk.Tk()
root.title("GATE")
# setting the windows size
root.geometry("600x400")
 
# declaring string variable
# for storing gate1 and gate2ord
gate1_var=tk.StringVar()
gate2_var=tk.StringVar()
gate_type_var=tk.StringVar()
mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W,tk.E,tk.S))

 
# defining a function that will
# get the gate1 and gate2ord and 
# print them on the screen
def submit():

    gate1=gate1_var.get()
    gate2=gate2_var.get()
    gateType = gate_type_var.get()
    #if((type(gate1) != int) or (type(gate2) != int) or gateType not in ['AND', 'OR', 'NOT', 'NAND', 'NOR', 'XOR', 'XNOR']):
   #     print("Invalid Input"
     #   )
    #    return 0
    
    print("The gate1 is : " + gate1)
    print("The gate2 is : " + gate2)
    print(   "The gate type is : " + gateType)
    gate1_var.set("")
    gate2_var.set("")
    gate_type_var.set("")
    return gate1, gate2, gateType
    
    
# creating a label for 
# gate1 using widget Label
gate1_label = tk.Label(root, text = 'gate1', font=('calibre',10, 'bold'))
 
# creating a entry for input
# gate1 using widget Entry
gate1_entry = tk.Entry(root,textvariable = gate1_var, font=('calibre',10,'normal'))
 
# creating a label for gate2
gate2_label = tk.Label(root, text = 'gate2', font = ('calibre',10,'bold'))
 
# creating a entry for gate2ord
gate2_entry=tk.Entry(root, textvariable = gate2_var, font = ('calibre',10,'normal'))
 
 
 
gateType_entry_label = tk.Label(root, text = 'gate type', font = ('calibre',10,'bold'))
gateType_entry=tk.Entry(root, textvariable = gate_type_var, font = ('calibre',10,'normal'))
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
gateType_entry_label.grid(row=3,column=0)
gateType_entry.grid(row=3,column=1)
sub_btn.grid(row=4,column=1)
 
# performing an infinite loop 
# for the window to display
root.mainloop()
