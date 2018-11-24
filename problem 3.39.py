print('Saifullah, 18B-092-CS, A')
print('1st detail Assignment, Problem 3.39')
def collision(x1,y1,r1,x2,y2,r2):
    import math
    c_dist = ((x2-x1)**2 + (y2-y1)**2)
    if c_dist <= (r1+r2)**2:
        return True
    else:
        return False


                  
