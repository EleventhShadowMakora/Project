import gate
from os import system as system



Gate = input("Choose gate (AND/OR/NOT/NAND/NOR/XOR) \nTo exit type 'EXIT'\n").upper()


if Gate ==("EXIT"):
    exit()
elif Gate not in ["AND","OR","NOT","NAND","NOR","XOR"]:
    print("Please select a valid operation")
    system(r"python .\Project\main.py")
    exit()


    
a= gate.getBoolInput("Enter input 1: ")
b= gate.getBoolInput("Enter input 2: ")

match Gate:
    case "AND":
        print("Output:", gate.AndGate(a,b).output())
    case "OR":
        print("Output:", gate.OrGate(a,b).output())
    case "NOT":
        print("Output:", gate.NotGate(a,b).output())
    case "NAND":
        print("Output:", gate.NandGate(a,b).output())
    case "NOR":
        print("Output:", gate.NorGate(a,b).output())
    case "XOR":
        print("Output:", gate.XorGate(a,b).output())

        
