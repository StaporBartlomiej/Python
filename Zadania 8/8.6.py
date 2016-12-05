
# wersja dynamiczna jest szybsza poniewaz wykorzystuje wczesniej policzone wyniki jednak kosztem pamieci
# bo musi przechowywac te wczesniej policzone wyniki aby moc z nich pozniej skorzystac
def P_recursive(i,j):
    if(i == 0) and (j == 0):
        return 0.5
    elif(i > 0) and (j ==0):
        return 0.0
    elif(i == 0) and (j > 0):
        return 1.0
    elif(i>0) and (j>0):
        return 0.5 * (P_recursive(i-1, j) + P_recursive(i, j-1))


def P_dynamic(i,j):
    dict = {(0,0): 0.5}

    def P(i,j):

        if (i, j) in dict.keys():
            print("Used already calculated P(" + str(i) + "," + str(j) + ")")
            return dict.get((i, j))
        if (i > 0) and (j == 0):
            return 0.0
        elif (i == 0) and (j > 0):
            return 1.0
        elif (i > 0) and (j > 0):
            result = 0.5 * (P(i-1,j) + P(i,j-1))
            dict[(i,j)] = result
            return result
    return P(i,j)
print("Recursive:")
print(P_recursive(0,0))
print(P_recursive(1,0))
print(P_recursive(0,1))
print(P_recursive(1,1))
print(P_recursive(3,4))
print(P_recursive(5,1))

print("Dynamic:")
print(P_dynamic(0,0))
print(P_dynamic(1,0))
print(P_dynamic(0,1))
print(P_dynamic(1,1))
print(P_dynamic(3,4))
print(P_dynamic(5,1))