print("Hello!, I'll clear the x1 and x2 from your function, please insert the a, b and c values.")

def bhaskara(a, b, c):
    
    form1p = -b + ((b**2 - 4 * a * c)**(1/2))
    form1n = -b - ((b**2 - 4 * a * c)**(1/2))
    form2 = 2 * a
    x1 = form1p / form2   
    x2 = form1n / form2
    a *= (x1 ** 2)       # LAS VARIABLES a, b y c NO CUMPLEN NINGUNA FUNCIÓN
    b *= x1
    c = c

    if a > 0 and b > 0:
        return print("x1 = " + str(x1) + "   x2 = " + str(x2))
    else: 
        print("ERROR; Invalid Syntax")

input(bhaskara(2, 4, 5))

