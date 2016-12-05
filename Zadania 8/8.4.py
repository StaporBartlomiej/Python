

def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
    Herona. Długości boków trójkąta wynoszą a, b, c."""

    if(not isinstance(a,int)):
        if(not isinstance(a,float)):
            raise ValueError("Bad arguments")

    if (not isinstance(b, int)):
        if (not isinstance(b, float)):
            raise ValueError("Bad arguments")

    if (not isinstance(c, int)):
        if (not isinstance(c, float)):
            raise ValueError("Bad arguments")

    if (a<=0) or (b<=0) or (c<=0):
        raise ValueError("Arguments can't be negative")
    if(a+b<=c) or (a+c<=b) or (b+c<=a):
        raise ValueError("Triangle can't be build")
    temp = (a+b+c)/2
    result = round((temp*(temp-a)*(temp-b)*(temp-c)) ** 0.5,2)
    print("Triangle Area = " + str(result))
print("heron(2,2,3)")
heron(2,2,3)
print("\nheron(6,3,8)")
heron(6,3,8)
print("\nheron(3,5,5)")
heron(3,5,5)
print("\nheron(12,14,23))")
heron(12,14,23)