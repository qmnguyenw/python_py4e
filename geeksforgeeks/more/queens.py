from itertools import permutations, combinations

text = input('How big is your chess board?')
n = int(text)
x = range(1, n+1)

def is_diagonal(point1, point2):
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]
    gradient = (y2-y1)/(x2-x1)
    if gradient == -1 or gradient == 1:
        return(True)
    else:
        return(False)

list_of_permutations = []

for permuation in permutations(range(1, n+1)):
    y = permuation
    all_permutations = list(zip(x,y))
    list_of_permutations.append(all_permutations)

for possible_solution in list_of_permutations:
    solutions = []
    for piece1, piece2 in combinations(possible_solution, 2):
        solutions.append(is_diagonal(piece1, piece2))

    if True not in solutions:
        print(possible_solution)