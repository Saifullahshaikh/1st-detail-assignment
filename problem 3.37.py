print('Saifullah, 18B-092-CS, A')
print('1st detail Assignment, Problem 3.37')
import math
def points(x1,y1,x2,y2):
    #slope = s
    s = (y2-y1)/(x2-x1)
    #distance = d
    d = math.sqrt(((x2-x1)**2)+((y2-y1)**2))
    if s > 1:
        print("The slope is"+" "+str(s)+" "+"and the distance is"+" "+str(d))
    else:
        print("The slope is infinity and the distance is " , d)
    
