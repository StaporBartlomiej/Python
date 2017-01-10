from math import floor
L = [1,2,3,4,5,6,7,8,9,10]

def binarne_rek(L, left, right, y):
    if left > right:
        return None
    mid = floor((left + right)/2)
    if L[mid] == y:
        return mid
    elif L[mid] > y:
        return binarne_rek(L,left,mid-1,y)
    else:
        return binarne_rek(L,mid+1,right,y)


assert binarne_rek(L, 0, len(L) - 1, 0) == None
assert binarne_rek(L, 0, len(L) - 1, 1) == 0
assert binarne_rek(L, 0, len(L) - 1, 6) == 5
assert binarne_rek(L, 0, len(L) - 1, 9) == 8
assert binarne_rek(L, 0, len(L) - 1, 11) == None
