class point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def sum(self,p):
        return point(int(self.x +p.x),int(self.y+p.y))
    def print_point(self):
        print(f"x coords are {self.x}, Y coords are {self.y}")

    def __add__(self,p):
        return point(int(self.x+p.x),int(self.y+p.y))
    def __sub__(self,p):
        return point(int(self.x-p.x),int(self.y-p.y))

P1 = point(1,2)
P2 = point(3,4)
print(P1.x)
print(P2.y)
P = P1.sum(P2)
P3 = point(6,10)
P4 = P3.sum(P2)
# P3 = P2.sum(5,6) Python internally does:Point.sum(P2, 5, 6)self = P2 p = 5 extra argument = 6
print(P.x)
print(P4.x,P4.y)
print(P4.print_point())
P5 = (P1-P2)
P6 = (P1+P3)
print(P5.x)
print(P5.y)

