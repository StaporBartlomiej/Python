import random
from sys import maxsize

def calc_pi(n):
    """Obliczanie liczby pi metodą Monte Carlo.
        n oznacza liczbę losowanych punktów."""
    print("Pi("+str(n)+")")
    try:
        counter = int(n)
        summ = 0
        for i in range(0,counter):
            a = random.randint(0,int(maxsize)) / int(maxsize)
            b = random.randint(0,int(maxsize)) / int(maxsize)
            if(a*a+b*b <= 1):
                summ +=1
        print("Ilosc punktow w kole: " + str(summ))
        print("Ilosc punktow w kwadracie: "+ str(counter))
        PI = 4*summ /counter
        print("PI:"+str(PI) + "\n")
    except ValueError:
        print("Zly argument, potrzebny int")



calc_pi(100)
calc_pi(1000)
calc_pi(10000)
