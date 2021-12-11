class Mystack:
    
    def __init__(self):
        self.data=[]
    
    def lenght(self):
        return len(self.data)
        
    
    def is_full(self):
        if len(self.data)<5:
            return 'not full'
        else:
            return 'full'
    
    def insert(self,ele):
        if len(self.data)<5:
            l=self.data.append(ele)
            return l
           
        else:
            return "overflow"
    
    def pop(self):
        if len(self.data)==0:
            return "underflow"
        else:
            
            return self.data.pop()
    
    
a = Mystack() 
a.insert(10) 
a.insert(23)
a.insert(25)
a.insert(27)
a.insert(17)
print(a.data)
print(a.is_full())
a.pop()
print(a.data)
print(a.is_full())
print(a.is_full())
print(a.data)
a.insert(400)
print(a.data)
print(a.pop())
print(a.pop())
print(a.pop())
print(a.data)
print(a.pop())
print(a.pop())
print(a.pop())
print(a.insert(55))
print(a.data)
print(a.insert(25))
print(a.data)
print(a.insert(24))
print(a.data)
print(a.insert(25))
print(a.data)
print(a.insert(25))
print(a.data)
print(a.insert(25))
print(a.data)