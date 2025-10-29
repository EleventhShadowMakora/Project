import gate
from os import system as system



Gate = 0#input("Choose gate (AND/OR/NOT/NAND/NOR/XOR) \nTo exit type 'EXIT'\n").upper()
def GateResult(Gate):
    
    if Gate ==("EXIT"):
        exit()
    elif Gate not in ["AND","OR","NOT","NAND","NOR","XOR"]:
        print("Please select a valid operation")
        system(r"python .\Project\Project1\main.py")
        exit()


        
    a= gate.getBoolInput("Enter input 1: ")
    b= gate.getBoolInput("Enter input 2: ")
    
    global Result;
   
    match Gate:
        case "AND":
            print("Output:", gate.AndGate(a,b).output())
            Result = gate.AndGate(a,b).output()
        case "OR":
            print("Output:", gate.OrGate(a,b).output())
            Result = gate.OrGate(a,b).output()
        case "NOT":
            print("Output:", gate.NotGate(a,b).output())
            Result = gate.NotGate(a,b).output()
        case "NAND":
            print("Output:", gate.NandGate(a,b).output())
            Result = gate.NandGate(a,b).output()
        case "NOR":
            print("Output:", gate.NorGate(a,b).output())
            Result = gate.NorGate(a,b).output()
        case "XOR":
            print("Output:", gate.XorGate(a,b).output())
            Result = gate.XorGate(a,b).output()
        
    return Result , Gate


GateResult()