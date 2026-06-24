class MinStack:

    def __init__(self):
        self.item=[]
        
        self.mitem=[]

    def push(self, val: int) -> None:
        self.item.append(val)
        val=min(val,self.mitem[-1] if len(self.mitem)!=0 else val)
        self.mitem.append(val)
    def pop(self) -> None:
        self.item.pop()
        self.mitem.pop()


    def top(self) -> int:
        
        return self.item[-1]
        

    def getMin(self) -> int:
        return self.mitem[-1]
        
