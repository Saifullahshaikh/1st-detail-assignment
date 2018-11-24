print('Saifullah, 18B-092-CS, A')
print('1st detail Assignment, Problem 3.34')
def pay(x,y):
    '''It takes input hourly wage & no of hours
    of employe & Returns the payment of an
    employe for a week'''  
    if y <= 40:
        pay = x*y
    else:
        pay = (x*40)+((1.5*x)*(y-40))
    return pay
