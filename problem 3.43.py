print('Saifullah, 18B-092-CS, A')
print('1st detail Assignment, Problem 3.43')
def hit(x1,y1,r1,x2,y2):
    import math
    #distance
    d = ((x2-x1)**2)+((y2-y1)**2)
    if d <= (r1**2):
        return True
    else:
        return False
