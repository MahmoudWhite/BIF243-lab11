class Point :
    def __init__ ( self , x , y ) :
        self . x = x
        self . y = y
    def __str__ ( self ) :
        return "("+str(self.x)+", " + str(self.y)+")"
class Rectangle:
    def __init__(self,p,q):
        assert p != Point or p.x > q.x or p.y > q.y , "Bad input!" #used google to figure out assert (because we did'nt take it in class)
        self.p=p
        self.q=q
    def __str__(self):
        return "(p="+ str(self.p)+", "+"q="+str(self.q)+")"
    def get_width(self):
        width= self.q.x-self.p.x
        return width
    def get_height(self):
        height= self.q.y-self.p.y
        return height
    def perimeter(self):
        perimeter= 2*self.get_height() + 2*self.get_width()
        return perimeter
    def area(self):
        area=self.get_width()*self.get_height()
        return area
    def contains(self,pt):
        assert pt != Point, "Bad input!"
        if self.p.x <= pt.x <= self.q.x and self.p.y <= pt.y <= self.q.y:
            return True
        else:
            return False
        
p1 = Point (1 , 2)
p2 = Point (3.2 , 4)
R = Rectangle ( p1 , p2 )
print ( R )
print ( R . get_width () )
print ( R . get_height () )
print ( R . area () )
print ( R . perimeter () )
print ( R . contains ( Point (1.5 , 3) ) )
print ( R . contains ( Point (10.5 , 3) ) )
print ( R . contains ( Point (1 , 2) ) )
print ( R . contains ( Point (3.2 , 4) ) )