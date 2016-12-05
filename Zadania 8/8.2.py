# lista krokow:
# 1.Czytaj: a,b,c
# 2. czy a = 0?
# 3.1 tak
#   a) to nie jest rownanie kwadratowe
# 3.2 nie
#   3.2.1 delta = b*b - 4*a*c,czy d<0?
#   3.2.2 tak
#       3.2.2.1 nie ma rozwiazan w dziedzinie liczb rzeczywistych
#   3.2.3 nie
#       3.2.3.1 czy d = 0?
#       3.2.3.2 nie
#           a) x1 = (-b+sqrt(delta))/(2*a)
#           b) x2 = (-b-sqrt(delta))/(2*a)
#       3.2.3.3 tak
#           a) x1 = x2 = (-b)/(2*a)
#
#
#schemat blokowy:
#                         start
#                           |
#                           |
#                    czytaj a, b, c
#                           |
#                           |
#        ________________ a == 0 _____
#    tak|                             |nie
#       |                             |
#  rownanie nie jest           delta = b*b - 4*a*c, d < 0__
#  kwadratowe              tak|                            |nie
#       |                     |                            |
#       |                brak                         __ d == 0 __
#     stop               rozwiazan w dziedzinie   tak|            |nie
#                        liczb rzeczywistych         |            |
#                             |                x1=(-b)/(2*a))   x1 = (-b+sqrt(delta))/(2*a)
#                             |                      |          x2 = (-b-sqrt(delta))/(2*a)
#                           stop                     |            |
#                                                    |            |
#                                                    stop --------
#

# drzewo:
#                                a = 0
#                                 /\
#                            tak /  \ nie
#                               /    \
#                              /      \
#                             /        \
#                            /          \
#                rownanie nie        delta = b*b - 4*a*c, d < 0
#                jest kwadratowe         /\
#                                   tak /  \ nie
#                                      /    \
#                                     /      \
#                                    /        \
#                                   /          \
#          brak rozwiazan w dziedzinie          d == 0
#          liczb rzeczywistych                  /\
#                                          tak /  \ nie
#                                             /    \
#                                            /      \
#                                           /        \
#                                          /          \
#                                x1=(-b)/(2*a))        x1 = (-b+sqrt(delta))/(2*a)
#                                                      x2 = (-b-sqrt(delta))/(2*a)


from math import sqrt
def solve2(a,b,c, * args):
    """Rozwiązywanie równania kwadratowego a * x * x + b * x + c = 0."""
    if(not isinstance(a,float)):
        if (not isinstance(a,int)):
            raise ValueError("Bad arguemnts")
    if (not isinstance(b,float)):
        if(not isinstance(b,int)):
            raise ValueError("Bad arguments")
    if (not isinstance(c,float)):
        if(not isinstance(c,int)):
            raise ValueError("Bad arguments")
    if (a==0):
        return ("To nie jest rownanie kwadratowe")

    delta = (b*b - 4*a*c)
    if(delta<0):
        return("Rownanie nie ma rozwiazan w dziedzinie liczb rzeczywistych")
    elif(delta == 0):
        x1 = round(( (-b) / (2*a) ),2)
        return "x1 = " + str(x1)
    else:
        x1 = round(((-b+sqrt(delta))/(2*a)),2)
        x2 = round(((-b-sqrt(delta))/(2*a)),2)
        return "x1 = "+str(x1) + "\nx2 = "+ str(x2)

print("solve2(0,2,3)\n"+solve2(0,2,3))

print("solve2(2,2,2)\n"+solve2(2,2,2))

print("solve2(1,2,1)\n"+solve2(1,2,1))

print("solve2(2,1,-1)\n"+solve2(2,1,-1))

