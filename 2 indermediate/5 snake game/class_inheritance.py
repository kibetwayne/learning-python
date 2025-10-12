class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")
        
class Fish(Animal): # Inherit from Animal class
    def __init__(self):
        super().__init__() # Call the constructor of the parent class => Animal
        

    def swim(self):
        print("Moving in water")
        
    def breathe(self): # build ontop of the parent class method
        super().breathe() # Call the breathe method of the parent class
        print("Doing this underwater")
        
        
nemo = Fish()
nemo.breathe()