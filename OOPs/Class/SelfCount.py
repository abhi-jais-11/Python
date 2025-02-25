class Counter:
    def __init__(self):
        self.count=0
        
    def increment(self):
        self.count+=1
        
    def decrement(self):
        self.count-=1
    
    def get_count(self):
        return self.count
    
    
count_value=Counter()
count_value.increment()
count_value.increment()
count_value.increment()
count_value.increment()
count_value.decrement()
print("Counter Value Is :",count_value.get_count())