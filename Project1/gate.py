class AndGate:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def output(self):
        return bool(self.a and self.b)
    
class OrGate:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def output(self):
        return bool(self.a or self.b)
    
class NotGate:
    def __init__(self,a,b= None):
        self.a = a
    def output(self):
        return bool(not self.a)
    
def getBoolInput(prompt):
    val = input(prompt + "0 or 1 ")
    return bool(int(val))


class NandGate(AndGate):
    def output(self):
        return not super().output()

class NorGate(OrGate):
    def output(self):
        return not super().output()

class XorGate:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def output(self):
        return self.a != self.b

def truthTable(gateClass):
    print("\nA | B | Output")
    for a in [False,True]:
        for b in [False,True]:
            result = gateClass(a,b).output()
            print(int(a), "|", int(b), "|", int(result))
            
Gates = [AndGate,OrGate,NotGate,NandGate,NorGate,XorGate]

#for i in Gates:
    #truthTable(i)