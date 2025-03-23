class MaxValue:
    
    def __init__(self, *args, **kwargs):
        pass
    
    @staticmethod
    def max_fine(*args):
        if len(args)>1:
            print(f"Max is {max(args)}")
        else:
            print("Max is",*args)

#object
mx=MaxValue()
mx.max_fine(10,20,30,10,50)
mx.max_fine(10)



    
    