from colored import fg as cl

class Color:
    
    def __init__(self,color):
        self.c=[]
        for i in range(len(color)):
            self.c.append(cl(color[i]))
            