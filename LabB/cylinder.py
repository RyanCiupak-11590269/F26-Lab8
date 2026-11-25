#define the class cylinder
import math
class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
        
    def volume(self):
        # To-DO: complete this method
        volume = math.pi*(self.radius**2)*self.height
        return(f"{volume:.2f}") 
    
    def surface_area(self):
        top = 3.14 * (self.radius)**2
        return (2*top) + (2*3.14*self.radius*self.height)
