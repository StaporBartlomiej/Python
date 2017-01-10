from math import floor


L = [1,51,67,45,2,35,76,3,56]

def mediana_sort(L, left, right):
    def bubble_sort(L):
        for number in range(left, right+1):
            for i in range(left, number):
                if L[i] > L[i + 1]:
                    temp = L[i]
                    L[i] = L[i + 1]
                    L[i + 1] = temp

    bubble_sort(L)
    return L[floor((left + right) / 2)]


assert mediana_sort(L,4,8) == 35
assert mediana_sort(L,0,8) == 45



